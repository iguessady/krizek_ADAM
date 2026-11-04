# Plán projektu

Fázy idú za sebou tak, aby po každej fáze existovala funkčná aplikácia.
Každá fáza = jedno nadradené **issue** na GitHube (#1–#11), každá úloha a požiadavka (F.., N..) = jeho **sub-issue**.

| Fáza | Názov | Čo sa urobí | Požiadavky | Prečo v tomto poradí |
|---|---|---|---|---|
| 0 | Plánovanie | zadanie, analýza, rozhodnutia, UX návrh, návrh databázy | — | najprv vedieť čo a ako, potom programovať |
| 1 | Základ | Flask projekt, štruktúra priečinkov, databáza, spoločný layout stránok | N01–N04 | všetko ostatné na tom stojí |
| 2 | Účty | registrácia, prihlásenie, odhlásenie, hashovanie hesiel | F01–F04, N06, N07 | všetky údaje patria konkrétnemu používateľovi |
| 3 | Trieda a predmety | trieda, predmety, rozvrh | F05–F08 | na predmety sa viažu zadania aj známky |
| 4 | Zadania | to-do list podľa predmetov | F09–F11 | potrebuje predmety |
| 5 | Známky | známky, vážený priemer | F12–F15 | potrebuje predmety (a voliteľne zadania) |
| 6 | Kalendár | udalosti + termíny zadaní v kalendári | F16–F18 | zobrazuje aj zadania z fázy 4 |
| 7 | Upozornenia | blížiace sa a zmeškané termíny | F19–F20 | počíta z údajov fáz 4–6 |
| 8 | Dashboard | súhrn všetkého na jednej stránke | F21 | zhŕňa všetky predošlé časti, preto posledný |
| 9 | Dokončenie | responzivita, kontrola vstupov, testy, hosting | N05, N08–N10 | ladenie hotovej aplikácie |
| 10 | Písomná časť a obhajoba | dopísanie práce, prezentácia | — | priebežne, dokončiť po aplikácii |

## Pevné termíny (od školy)

| Dátum | Čo |
|---|---|
| 4. 12. 2026 | 1. kontrola: 5 strán písomnej časti |
| 22. 1. 2027 | 2. kontrola: 10 strán |
| 26. 2. 2027 | 3. kontrola: 15 strán |
| 23. 3. 2027 | odovzdanie písomnej časti (min. 20 strán, zviazaná) |
| 7.–9. 4. 2027 | obhajoba |

## Harmonogram

Aplikácia má byť hotová začiatkom marca, aby zostal čas na testovanie, dopísanie práce a tlač.
Písomná časť sa píše **priebežne** popri programovaní; čo sa v danej fáze urobí, to sa hneď opíše.

| Fáza | Od | Do | Písomná časť v tomto období |
|---|---|---|---|
| 0 Plánovanie | 14. 10. 2026 | 16. 11. 2026 | úvod, popis problému, analýza |
| 1 Základ | 17. 11. 2026 | 23. 11. 2026 | popis použitých technológií (Python, Flask, SQLite, Jinja...) |
| 2 Účty | 24. 11. 2026 | 7. 12. 2026 | **do 4. 12.: 5 strán** (úvod, technológie, analýza) |
| 3 Trieda a predmety | 8. 12. 2026 | 20. 12. 2026 | návrh databázy, architektúra |
| (Vianoce) | 21. 12. 2026 | 3. 1. 2027 | rezerva |
| 4 Zadania | 4. 1. 2027 | 17. 1. 2027 | UX návrh |
| 5 Známky | 18. 1. 2027 | 31. 1. 2027 | **do 22. 1.: 10 strán** (+ teoretická časť) |
| 6 Kalendár | 1. 2. 2027 | 14. 2. 2027 | praktická časť: účty, predmety |
| 7 Upozornenia | 15. 2. 2027 | 21. 2. 2027 | praktická časť: zadania, známky |
| 8 Dashboard | 22. 2. 2027 | 7. 3. 2027 | **do 26. 2.: 15 strán** |
| 9 Dokončenie | 8. 3. 2027 | 16. 3. 2027 | testovanie, záver |
| 10 Písomná časť a obhajoba | 17. 3. 2027 | 9. 4. 2027 | **do 23. 3.: odovzdanie** (kontrola, tlač, väzba), potom prezentácia a nácvik obhajoby |
