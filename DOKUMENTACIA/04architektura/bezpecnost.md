# Bezpečnosť

| Hrozba | Ochrana v ADAM-ovi | Požiadavka |
|---|---|---|
| Únik hesiel z databázy | heslá sa ukladajú iba ako **hash** so soľou (Werkzeug), nikdy v čitateľnej podobe | N06 |
| Prístup bez prihlásenia | `@login_required` na všetkých stránkach okrem `/login` a `/register` | N07 |
| Prístup k cudzím údajom | každý dotaz filtruje podľa `current_user`; pri úprave/mazaní sa overí, že záznam patrí prihlásenému používateľovi (inak chyba 404) | F03 |
| SQL injection | dotazy cez SQLAlchemy (parametrizované), žiadne skladanie SQL z textu | — |
| XSS (vloženie skriptu do stránky) | Jinja automaticky escapuje výstup | — |
| Podvrhnutý formulár (CSRF) | Flask-WTF pridá do každého formulára tajný token a overí ho (R13) | — |
| Zmena údajov cez odkaz | mazanie a odhlásenie iba cez POST | — |
| Ukradnutie session | podpísané cookies (SECRET_KEY mimo kódu v gite) | — |
| Zmazanie účtu omylom | zmazanie účtu vyžaduje zadanie hesla | F24 |
| Únik odkazu na rozvrh z EduPage | odkaz sa nezobrazuje celý, nie je v logoch ani v gite; kto ho má, vidí rozvrh | N11 |
| Zneužitie importu na sťahovanie iných stránok | povolené sú iba adresy `https://*.edupage.org/webcal…`, s časovým limitom a obmedzenou veľkosťou | F25 |
| Neplatné vstupy | kontrola vstupov na serveri (povinné polia, známka 1–5, dátum) | N08 |
