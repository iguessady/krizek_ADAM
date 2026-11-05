# Denník rozhodnutí

Každé dôležité rozhodnutie o projekte: čo, prečo a kedy. Pri obhajobe sa dá ku každému vrátiť.

| # | Dátum | Rozhodnutie | Prečo | Zamietnuté možnosti |
|---|---|---|---|---|
| R01 | 2026-10-14 | Back end: **Python + Flask** | zadanie vyžaduje Python (T1); Flask je malý a jednoduchý, každej časti kódu rozumiem | Django (príliš veľký pre tento projekt), Node.js + Express (pôvodný návrh v README, nespĺňa zadanie) |
| R02 | 2026-10-14 | Databáza: **SQLite** | vyžaduje zadanie (T3); jeden súbor, netreba server | — |
| R03 | 2026-10-14 | Hosting sa rieši **až na konci** | hlavná je aplikácia; hosting nie je v zadaní | — |
| R04 | 2026-11-03 | Dokumentácia je **v repozitári** v priečinku `DOKUMENTACIA/` | má históriu zmien a zálohu na GitHube spolu s kódom | dokumentácia mimo repozitára |
| R05 | 2026-11-03 | Jazyk: dokumentácia a jej súbory/priečinky **po slovensky**, komentáre v kóde **po slovensky**, všetko ostatné (kód, názvy, commity, texty v aplikácii) **po anglicky** | práca je po slovensky; kód a texty v aplikácii v angličtine sa ľahšie udržiavajú konzistentné | aplikácia po slovensky |
| R06 | 2026-11-03 | Úlohy sa evidujú na **GitHub Projects (Kanban)**: každá fáza = nadradené issue (#1–#11), úlohy a požiadavky = jeho sub-issues | prehľad o postupe, prepojenie s commitmi („Closes #12"), dá sa ukázať v práci | samostatný zoznam úloh v súbore |
| R07 | 2026-11-03 | Stránky sa tvoria cez **Flask šablóny (Jinja)** + trochu JavaScriptu | jednoduchšie, menej kódu, celá aplikácia je v jednom projekte | samostatný JS front end volajúci API |
| R08 | 2026-11-03 | Práca s databázou cez **Flask-SQLAlchemy** (ORM) nad SQLite | tabuľky sú Python triedy, menej ručne písaného SQL, menšie riziko chýb | modul `sqlite3` s vlastným SQL |
| R09 | 2026-11-03 | Prihlasovanie cez **Flask-Login** | overené riešenie pre sessions a ochranu stránok (N07) | vlastné sessions |
| R10 | 2026-11-03 | Termíny: kontroly písomnej časti **4. 12. 2026** (5 strán), **22. 1. 2027** (10 strán), **26. 2. 2027** (15 strán); odovzdanie **do 23. 3. 2027**; obhajoba **7.–9. 4. 2027** | termíny od školy/vedúceho projektu | — |
| R11 | 2026-11-03 | Účty, prihlasovanie a kalendár sú v MVP **vlastné**; integrácie (export .ics → prihlásenie cez Google → Google Calendar API → EduPage) až **po MVP** v tomto poradí | zadanie vyžaduje vlastnú registráciu a databázu; vlastné riešenie viem vysvetliť; demo nezávisí od tretích strán; EduPage API je neoficiálne a rizikové (heslá, GDPR) | prihlásenie cez Google a import z EduPage už v MVP |
| R12 | 2026-11-03 | CSS: **Bootstrap** (+ vlastné CSS na úpravy) | rýchlejší vývoj, responzivita (N05) bez veľa práce; CSS ovládam, takže viem Bootstrap upraviť | iba vlastné CSS |
| R13 | 2026-11-03 | Formuláre: **Flask-WTF** | validácia vstupov (N08) a ochrana proti CSRF zabudovaná | obyčajné HTML formuláre |
| R14 | 2026-11-03 | Kalendár: knižnica **FullCalendar** (vyskúšať) | hotový mesačný/týždenný pohľad; ak nebude vyhovovať, vlastné riešenie v Jinja | vlastný kalendár od začiatku |
| R15 | 2026-11-03 | Rozvrh **bez párneho/nepárneho týždňa** | v MVP netreba, zjednodušuje rozvrh | striedanie týždňov |
| R16 | 2026-11-03 | Predmet sa dá **zmazať aj so zadaniami a známkami** (po potvrdení) | jednoduché pre používateľa; potvrdzovacie okno zabráni omylu | zákaz mazania predmetu so záznamami |
| R17 | 2026-11-03 | Upozornenia sú **nastaviteľné** (koľko dní dopredu) | každý študent potrebuje iný predstih | pevne 3 dni |
| R18 | 2026-11-03 | Používateľ si môže **zmeniť heslo a zmazať účet** | kontrola nad vlastnými osobnými údajmi (GDPR) | — |
| R19 | 2026-11-03 | **Import rozvrhu z EduPage cez odkaz (.ics) je v MVP**, ručné zadanie (F07) zostáva | EduPage má oficiálny export kalendára (webcal/.ics), ktorý si vygeneruje každý študent; štandardný formát, netreba heslo do EduPage ani neoficiálne API; ručné zadanie pre školy bez EduPage a na úpravy | import až po MVP |
| R20 | 2026-11-03 | **Rozvrh je povinný**: po registrácii ho používateľ musí importovať alebo zadať; **predmety vznikajú z rozvrhu** | zoznam predmetov sa nemusí zadávať zvlášť, všetko ďalšie (zadania, známky) stojí na predmetoch | predmety zadávané samostatne |
| R21 | 2026-11-03 | Známka môže byť **známka 1–5 (aj s +/-), body alebo percentá**; priemer sa vždy počíta v **percentách** a zobrazí sa aj ako známka | v škole sa hodnotí rôzne (testy na body, ústne známkou); percentá sú spoločná jednotka | iba známky 1–5 |
| R22 | 2026-11-03 | Databáza: trieda je stĺpec v `users`; nick iba zobrazovaný; predmet sa dá pridať aj mimo rozvrhu; udalosť môže byť voliteľne priradená k predmetu | jednoduchosť; jeden používateľ = jedna trieda | samostatná tabuľka tried, jedinečný nick |
| R23 | 2026-11-04 | **Rozvrh iba importom z EduPage** (F25); ručné zadávanie rozvrhu (F07) sa ruší. Hodiny navyše si používateľ pridá ako udalosti do kalendára (F16) | rozvrh je povinný a import ho vytvorí celý; ručné zadávanie by bola zbytočná práca navyše | ručné zadávanie rozvrhu popri importe (pôvodne v R19) |
| R24 | 2026-11-04 | Počet dní pre upozornenie sa nastavuje **pri každom zadaní zvlášť** (predvolene 3 dni, dá sa zmeniť); nahrádza jedno nastavenie pre celý účet z R17 | test treba vidieť skôr ako bežnú domácu úlohu | jedno nastavenie pre celý účet |
| R26 | 2026-11-05 | Import z EduPage (.ics) prenesie **rozvrh vrátane krúžkov**, **školské akcie** (do kalendára) a **zadania od učiteľov** (do zadaní); v rozvrhu sa ukladá aj **učiteľ, iba skratka** (iniciály); predmet dostane ako názov skratku z EduPage | v exporte to už je, používateľ nemusí nič prepisovať; iniciály stačia a sú menej osobný údaj ako celé meno (pozri `05databaza/edupage-ics.md`) | import iba rozvrhu |
| R27 | 2026-11-05 | **Bez wireframov a štýlového manuálu vopred**; dizajn sa robí priebežne počas programovania (na Bootstrape). Podkladom pre UX sú [user flows](../03ux/user-flows.md) | dizajn sa ľahšie rozhoduje, keď vidím hotovú stránku; Bootstrap dáva rozumný základný vzhľad | wireframy každej obrazovky pred programovaním |

## Otvorené rozhodnutia

Momentálne žiadne.
