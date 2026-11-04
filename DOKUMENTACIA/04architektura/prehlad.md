# Prehľad architektúry

> Živý dokument: opisuje **MVP**. Plánované rozšírenia sú v [rozsirenia.md](rozsirenia.md) a po ich pridaní sa tento dokument doplní.

## Tri vrstvy

ADAM je klasická webová aplikácia typu klient–server. Všetko (logika aj vytváranie stránok) beží na serveri vo Flasku,
prehliadač iba zobrazuje hotové HTML stránky.

```
┌────────────────────┐     HTTP požiadavka      ┌─────────────────────────────────────────┐        SQL        ┌──────────────┐
│     PREHLIADAČ     │ ───────────────────────▶ │              FLASK (Python)              │ ────────────────▶ │    SQLite    │
│  HTML, CSS, JS     │                          │                                          │                   │  (adam.db)   │
│                    │ ◀─────────────────────── │  routes (blueprints) → modely → šablóny  │ ◀──────────────── │              │
└────────────────────┘     HTML odpoveď         └─────────────────────────────────────────┘      dáta         └──────────────┘
```

> Do práce treba diagram nakresliť ako obrázok (napr. draw.io).

| Vrstva | Technológia | Úloha |
|---|---|---|
| Prezentačná (klient) | HTML5, CSS, JavaScript | zobrazenie stránok, formuláre, drobná interaktivita |
| Aplikačná (server) | Python, Flask, Jinja, Flask-Login | spracovanie požiadaviek, logika (napr. výpočet priemeru), overenie prihlásenia, vytváranie HTML |
| Dátová | SQLite cez Flask-SQLAlchemy | trvalé uloženie údajov |

## Ako prebehne jedna požiadavka

Príklad: prihlásený študent pridá známku.

1. Študent vyplní formulár „Add grade" a klikne na **Save**.
2. Prehliadač pošle požiadavku `POST /grades/add` s údajmi z formulára.
3. Flask nájde funkciu (route), ktorá patrí k tejto adrese v module `grades`.
4. Flask-Login overí, že je používateľ prihlásený. Ak nie, presmeruje ho na `/login`.
5. Route skontroluje vstup (známka 1–5, platný dátum, predmet patrí tomuto používateľovi).
6. Cez model `Grade` (Flask-SQLAlchemy) sa známka uloží do SQLite.
7. Route presmeruje na `GET /grades`. Tam sa z databázy načítajú známky, vypočíta sa priemer
   a šablóna Jinja `grades/list.html` z nich vytvorí HTML.
8. Prehliadač zobrazí stránku s novou známkou a novým priemerom.

## Vzor MVC

Rozdelenie zodpovedá vzoru **Model–View–Controller**:

| Časť MVC | V ADAM-ovi | Kde v kóde |
|---|---|---|
| Model (dáta) | SQLAlchemy modely | `app/models.py` |
| View (zobrazenie) | Jinja šablóny | `app/templates/` |
| Controller (riadenie) | routes v blueprintoch | `app/routes/` |

Výhoda: zmena vzhľadu nemení logiku a zmena databázy nemení šablóny.
