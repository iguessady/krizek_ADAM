# Zoznam URL

GET = zobrazí stránku, POST = odošle formulár. Všetky stránky okrem `/login` a `/register` vyžadujú prihlásenie.
`<id>` je číslo záznamu v databáze.

> Návrh. Upraví sa podľa wireframov a otvorených otázok.

## auth
| URL | Metóda | Čo robí | Požiadavka |
|---|---|---|---|
| `/register` | GET, POST | registrácia | F01 |
| `/login` | GET, POST | prihlásenie | F02 |
| `/logout` | POST | odhlásenie | F02 |
| `/account` | GET | stránka účtu (odkazy na zmenu hesla a zmazanie účtu) | F23, F24 |
| `/account/password` | GET, POST | zmena hesla | F23 |
| `/account/delete` | POST | zmazanie účtu (vyžaduje heslo) | F24 |

## dashboard
| URL | Metóda | Čo robí | Požiadavka |
|---|---|---|---|
| `/` | GET | dashboard (neprihláseného presmeruje na `/login`) | F21, F19, F20 |

## subjects
| URL | Metóda | Čo robí | Požiadavka |
|---|---|---|---|
| `/class` | GET, POST | zobrazenie a úprava triedy | F05 |
| `/subjects` | GET | zoznam predmetov | F06 |
| `/subjects/add` | GET, POST | pridanie predmetu | F06 |
| `/subjects/<id>/edit` | GET, POST | úprava predmetu | F06 |
| `/subjects/<id>/delete` | POST | zmazanie predmetu aj s jeho zadaniami a známkami (po potvrdení) | F06 |
| `/timetable` | GET | rozvrh ako tabuľka | F08 |
| `/timetable/import` | GET, POST | import rozvrhu z odkazu EduPage (.ics) | F25 |

## tasks
| URL | Metóda | Čo robí | Požiadavka |
|---|---|---|---|
| `/tasks` | GET | zoznam zadaní (filter podľa predmetu: `?subject=<id>`) | F11 |
| `/tasks/add` | GET, POST | pridanie zadania | F09 |
| `/tasks/<id>/edit` | GET, POST | úprava zadania | F10 |
| `/tasks/<id>/toggle` | POST | označiť hotové / nehotové | F10 |
| `/tasks/<id>/delete` | POST | zmazanie zadania | F10 |

## grades
| URL | Metóda | Čo robí | Požiadavka |
|---|---|---|---|
| `/grades` | GET | známky podľa predmetov + priemery | F14, F15 |
| `/grades/add` | GET, POST | pridanie známky (voliteľne `?task=<id>`) | F12 |
| `/grades/<id>/edit` | GET, POST | úprava známky | F13 |
| `/grades/<id>/delete` | POST | zmazanie známky | F13 |

## calendar
| URL | Metóda | Čo robí | Požiadavka |
|---|---|---|---|
| `/calendar` | GET | stránka s kalendárom (FullCalendar) | F18 |
| `/calendar/events` | GET | udalosti a termíny zadaní vo formáte JSON pre FullCalendar (`?start=…&end=…`) | F18 |
| `/calendar/add` | GET, POST | pridanie udalosti | F16 |
| `/calendar/<id>/edit` | GET, POST | úprava udalosti | F17 |
| `/calendar/<id>/delete` | POST | zmazanie udalosti | F17 |

**Prečo je mazanie a odhlásenie cez POST:** odkaz (GET) môže prehliadač alebo iná stránka otvoriť aj bez kliknutia používateľa. Zmena údajov preto ide vždy cez formulár (POST).
