# Návrh databázy

> Návrh (2026-11-03). ER diagram treba ešte nakresliť ako obrázok (napr. dbdiagram.io).

Databáza: **SQLite**, prístup cez **Flask-SQLAlchemy** (R02, R08).
Názvy tabuliek a stĺpcov sú **po anglicky** (sú súčasťou kódu, R05).

## Hlavné pravidlá

- **Rozvrh je povinný.** Po registrácii musí používateľ rozvrh importovať z EduPage (F25) alebo zadať ručne (F07), až potom sa dostane na dashboard (R20).
- **Predmety vznikajú z rozvrhu.** Pri importe/zadaní rozvrhu sa vytvorí zoznam predmetov; používateľ ich potom môže upraviť (farba, skratka) alebo pridať ďalší (F06).
- **Každý údaj patrí jednému používateľovi.** Zmazanie používateľa zmaže všetko jeho (F24); zmazanie predmetu zmaže jeho rozvrh, zadania a známky (R16).

## ER diagram (textová predloha)

```
users 1 ──── N subjects 1 ──── N timetable_entries
  │                │
  │                ├──── N tasks 1 ──── 0..1 grades
  │                │
  │                └──── N grades
  │
  └──── N events
```

Čítaj: jeden používateľ má veľa predmetov; jeden predmet má veľa hodín v rozvrhu, veľa zadaní a veľa známok;
známka môže (ale nemusí) byť výsledkom konkrétneho zadania.

## Tabuľky

### users
| Stĺpec | Typ | Poznámka |
|---|---|---|
| id | INTEGER, PK | |
| email | TEXT, UNIQUE, NOT NULL | prihlasovacie meno |
| nick | TEXT, NOT NULL | iba zobrazované meno, nemusí byť jedinečný |
| password_hash | TEXT, NOT NULL | nikdy nie heslo samotné (N06) |
| class_name | TEXT | napr. „IV.C" (F05) |
| school_name | TEXT | (F05) |
| school_year | TEXT | napr. „2026/2027" (F05) |
| reminder_days | INTEGER, NOT NULL, default 3 | koľko dní dopredu upozorňovať (F22) |
| edupage_ics_url | TEXT, NULL | odkaz na rozvrh z EduPage, citlivý údaj (N11) |
| created_at | DATETIME, NOT NULL | |

### subjects
| Stĺpec | Typ | Poznámka |
|---|---|---|
| id | INTEGER, PK | |
| user_id | INTEGER, FK → users.id, NOT NULL | ON DELETE CASCADE |
| name | TEXT, NOT NULL | napr. „Matematika" |
| short_name | TEXT | napr. „MAT" |
| color | TEXT | farba v rozvrhu/kalendári, napr. `#3b82f6` |
| | UNIQUE(user_id, name) | jeden používateľ nemá dva rovnaké predmety |

### timetable_entries (jedna hodina v týždennom rozvrhu)
| Stĺpec | Typ | Poznámka |
|---|---|---|
| id | INTEGER, PK | |
| subject_id | INTEGER, FK → subjects.id, NOT NULL | ON DELETE CASCADE |
| weekday | INTEGER, NOT NULL | 0 = pondelok … 4 = piatok |
| lesson_number | INTEGER, NOT NULL | 0.–8. hodina |
| start_time | TIME, NOT NULL | z importu alebo zadané ručne |
| end_time | TIME, NOT NULL | |
| room | TEXT | učebňa |

### tasks (zadania)
| Stĺpec | Typ | Poznámka |
|---|---|---|
| id | INTEGER, PK | |
| subject_id | INTEGER, FK → subjects.id, NOT NULL | ON DELETE CASCADE |
| title | TEXT, NOT NULL | |
| description | TEXT | |
| type | TEXT, NOT NULL | `homework` / `test` / `project` / `other` |
| due_date | DATE, NOT NULL | termín |
| done | BOOLEAN, NOT NULL, default false | (F10) |
| created_at | DATETIME, NOT NULL | |

### grades (známky)

Známka môže byť troch druhov (R21). Pri výpočte priemeru sa každá prevedie na **percentá**.

| Stĺpec | Typ | Poznámka |
|---|---|---|
| id | INTEGER, PK | |
| subject_id | INTEGER, FK → subjects.id, NOT NULL | ON DELETE CASCADE |
| task_id | INTEGER, FK → tasks.id, NULL | ak je známka výsledkom zadania; ON DELETE SET NULL |
| kind | TEXT, NOT NULL | `mark` (známka 1–5) / `points` (body) / `percent` (percentá) |
| mark | INTEGER, NULL | 1–5, iba pri `mark` (CHECK) |
| mark_modifier | TEXT, NULL | `+`, `-` alebo nič (napr. „2-"), iba pri `mark` |
| points | REAL, NULL | získané body, iba pri `points` |
| max_points | REAL, NULL | maximum bodov (> 0), iba pri `points` |
| percent | REAL, NULL | 0–100, iba pri `percent` |
| weight | REAL, NOT NULL, default 1 | váha pre vážený priemer |
| date | DATE, NOT NULL | |
| note | TEXT | |

Ktoré stĺpce musia byť vyplnené, závisí od `kind`; kontroluje to formulár (Flask-WTF) aj CHECK v databáze.

### events (udalosti v kalendári)
| Stĺpec | Typ | Poznámka |
|---|---|---|
| id | INTEGER, PK | |
| user_id | INTEGER, FK → users.id, NOT NULL | ON DELETE CASCADE |
| subject_id | INTEGER, FK → subjects.id, NULL | voliteľne, ak súvisí s predmetom |
| title | TEXT, NOT NULL | |
| description | TEXT | |
| start | DATETIME, NOT NULL | |
| end | DATETIME | |
| all_day | BOOLEAN, NOT NULL, default false | |

## Prečo tak (do práce)

- **Normalizácia:** `user_id` majú iba `subjects` a `events`. Zadania, známky a rozvrh patria používateľovi cez predmet,
  takže tá istá informácia nie je uložená dvakrát (3. normálna forma). Pri dotazoch sa tabuľky spoja cez `subject_id`.
- **Vážený priemer** sa neukladá, počíta sa vždy z aktuálnych známok (pozri nižšie).
  Keby sa ukladal, mohol by sa po zmene známky „rozísť" so skutočnosťou.
- **Upozornenia** nemajú vlastnú tabuľku: počítajú sa z `tasks.due_date`, `tasks.done` a `users.reminder_days`.
- **Termíny zadaní v kalendári** sa nekopírujú do `events`; kalendár ich načíta z `tasks` (F18).
- **`ON DELETE CASCADE`** zabezpečí mazanie predmetu so zadaniami/známkami (R16) a účtu so všetkým (F24).
  V SQLite treba zapnúť `PRAGMA foreign_keys = ON`.

## Výpočet priemeru (R21)

1. Každá známka sa prevedie na percentá:
   - `percent` → priamo hodnota,
   - `points` → `points / max_points * 100`,
   - `mark` → podľa tabuľky nižšie (`+` pridá, `-` uberie 5 %).
2. Vážený priemer predmetu = `SUM(percent × weight) / SUM(weight)`.
3. Priemer sa zobrazí v percentách **aj ako známka** podľa tabuľky.
4. Celkový priemer (F15) = priemer z percentuálnych priemerov všetkých predmetov, ktoré majú aspoň jednu známku.

| Známka | Rozsah percent (prevod % → známka) | Hodnota pri prevode známka → % |
|---|---|---|
| 1 | 90–100 % | 95 % |
| 2 | 75–89 % | 82 % |
| 3 | 50–74 % | 62 % |
| 4 | 30–49 % | 40 % |
| 5 | 0–29 % | 15 % |

> Rozsahy sú bežná stupnica; treba ich overiť podľa klasifikačného poriadku školy. Hodnota pri prevode známka → % je stred rozsahu.

Prevod sa robí v Pythone (metóda modelu `Grade`), nie v databáze, a dá sa otestovať unit testami.

## Zodpovedané otázky (2026-11-03)

| Otázka | Odpoveď |
|---|---|
| Údaje o triede | stĺpce v `users` |
| Druhy známok | ľubovoľné (známka, body, percentá), priemer cez percentá (R21) |
| Typy zadaní | `homework`, `test`, `project`, `other` |
| Nick | iba zobrazované meno, nemusí byť jedinečný |
| Predmet mimo rozvrhu | áno, dá sa pridať ručne (F06) |
| Udalosť priradená k predmetu | áno, voliteľne |
