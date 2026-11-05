# Čo obsahuje export rozvrhu z EduPage (.ics)

Analýza vlastného exportu (stiahnutý 2026-11-05). Súbor samotný **nie je v repozitári**, obsahuje osobné údaje.
Príklady nižšie sú upravené (iniciály učiteľov nahradené `Xy`).

## Celkovo

- Formát **iCalendar** (`PRODID:-//aSc//Edupage//EN`), časové pásmo `Europe/Bratislava`.
- Jedna **udalosť (VEVENT) = jedna konkrétna vyučovacia hodina s dátumom**, nie týždenná šablóna.
- Môj export: **714 udalostí** od 6. 10. 2026 do 3. 5. 2027. Bežné hodiny sú v ňom iba **do 12. 2. 2027** (dovtedy je rozvrh zverejnený), neskôr už len krúžky.
- Pri každej zmene rozvrhu treba import zopakovať.

## Polia jednej hodiny

```
BEGIN:VEVENT
UID:2026-10-06:e0807c53_1@spsezoska.edupage.org
DTSTART:20261006T060000Z
DTEND:20261006T064500Z
SUMMARY:EMA
LOCATION:103
DESCRIPTION:IV.C\nXy
END:VEVENT
```

| Pole | Čo obsahuje | Použitie v ADAM-ovi |
|---|---|---|
| `UID` | dátum + ID hodiny + **číslo hodiny** za podčiarkovníkom (`_1` = 1. hodina) | `lesson_number` |
| `DTSTART`, `DTEND` | začiatok a koniec v **UTC** (`Z`) | prepočítať na miestny čas (zimný/letný čas!) → `start_time`, `end_time`, `weekday` |
| `SUMMARY` | **iba skratka predmetu** (`MAT`, `ANJ`, `UMIcv`), nie celý názov | `subjects.short_name`; celý názov si doplní používateľ |
| `LOCATION` | učebňa (niekedy prázdne alebo viac učební `210 \, 211`) | `room` |
| `DESCRIPTION` | trieda, prípadne skupina (`IV.C 1. Skupina`) a **iniciály učiteľa** | `teacher` (iba iniciály, R26) |

Zistené časy hodín (miestny čas): 0. hodina 7:10, 1. 8:00, 2. 8:50, 3. 9:45, 4. 10:35, 5. 11:50, 6. 12:40, 7. 13:30, 8. 14:20.

## Zvláštne prípady

| Prípad | Ako vyzerá | Čo s tým |
|---|---|---|
| **Suplovanie / zmena predmetu** | `SUMMARY:ANK -> TRH`, `PXA -> MAT` | pri tvorbe šablóny ignorovať |
| **Zmena učiteľa** | `DESCRIPTION:… Xy -> Yz` | pri tvorbe šablóny ignorovať |
| **Školské akcie** | napr. divadlo, stužková, e-maturita, ako celodenné (00:00–00:00 miestneho času) alebo cez hodiny | importujú sa do `events` (F27, R26) |
| **Zadania od učiteľa** | celodenná udalosť s `DESCRIPTION:Predmet: UMIcv\nTriedy: …\nUčitelia: …` | importujú sa ako `tasks` k danému predmetu (F28, R26) |
| **Krúžky** | `SUMMARY:Krúžok` | importujú sa do rozvrhu ako predmet (R26) |

## Ako z toho vznikne týždenný rozvrh

1. Prepočítať čas z UTC na `Europe/Bratislava`.
2. Vynechať suplovania (`->`) a celodenné udalosti.
3. Pre každú dvojicu (deň v týždni, číslo hodiny) vybrať predmet, ktorý sa vyskytuje **najčastejšie**.
4. Z rôznych skratiek vytvoriť predmety (`subjects`), z dvojíc záznamy v `timetable_entries`.
