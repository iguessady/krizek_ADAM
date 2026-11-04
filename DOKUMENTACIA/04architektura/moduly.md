# Moduly (blueprinty)

| Modul | Súbor | Čo robí | Požiadavky |
|---|---|---|---|
| auth | `routes/auth.py` | registrácia, prihlásenie, odhlásenie, zmena hesla, zmazanie účtu, nastavenia upozornení | F01, F02, F22–F24, N06, N07 |
| dashboard | `routes/dashboard.py` | úvodná stránka po prihlásení: najbližšie udalosti, nehotové zadania, priemery, upozornenia | F21 |
| subjects | `routes/subjects.py` | trieda, predmety (pridať/upraviť/zmazať aj so zadaniami a známkami), týždenný rozvrh ručne alebo importom z EduPage (.ics) | F05–F08, F25 |
| tasks | `routes/tasks.py` | zadania k predmetom, hotové/nehotové, zobrazenie podľa predmetov | F09–F11 |
| grades | `routes/grades.py` | známky, vážený priemer predmetu a celkový priemer | F12–F15 |
| calendar | `routes/calendar.py` | udalosti v kalendári; stránka s FullCalendarom + JSON so zoznamom udalostí a termínov zadaní | F16–F18 |
| reminders | `routes/reminders.py` | výpočet blížiacich sa a zmeškaných termínov | F19, F20 |

## Spoločné pre všetky moduly

- Okrem `auth` sú všetky stránky chránené dekorátorom `@login_required` (N07).
- Každý dotaz do databázy filtruje podľa prihláseného používateľa (`current_user`) (F03).
- Každá zmena sa hneď ukladá do databázy (F04).

## Závislosti medzi modulmi

```
auth ──▶ (všetky ostatné potrebujú prihláseného používateľa)
subjects ──▶ tasks, grades, calendar (zadania a známky patria k predmetu)
tasks + calendar ──▶ reminders ──▶ dashboard
grades ──▶ dashboard
```

Z toho vychádza aj poradie fáz v [plan.md](../01planovanie/plan.md).
