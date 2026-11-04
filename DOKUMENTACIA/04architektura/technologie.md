# Použité technológie

| Technológia | Na čo | Prečo práve táto |
|---|---|---|
| **Python 3** | jazyk back endu | vyžaduje zadanie (T1) |
| **Flask** | webový framework | malý a jednoduchý, každej časti rozumiem; na rozdiel od Djanga nič „nerobí za mňa" (R01) |
| **Jinja** | šablóny HTML | súčasť Flasku; HTML sa vytvára na serveri, netreba samostatný front end (R07) |
| **SQLite** | databáza | vyžaduje zadanie (T3); jeden súbor, netreba databázový server (R02) |
| **Flask-SQLAlchemy** | práca s databázou (ORM) | tabuľky sú Python triedy, menej ručného SQL (R08) |
| **Flask-Login** | prihlasovanie a sessions | overené riešenie, dekorátor `@login_required` (R09) |
| **Werkzeug** (súčasť Flasku) | hashovanie hesiel | `generate_password_hash` / `check_password_hash`, netreba ďalšiu knižnicu |
| **HTML5, CSS, JavaScript** | front end | vyžaduje zadanie (T2) |
| **Bootstrap** | vzhľad a responzivita | hotové komponenty a mriežka pre mobil (R12) |
| **Flask-WTF** | formuláre | validácia vstupov a ochrana CSRF (R13) |
| **FullCalendar** | zobrazenie kalendára | hotový mesačný/týždenný pohľad, údaje dostane z Flasku vo formáte JSON (R14) |
| **icalendar** | čítanie .ics súborov | import rozvrhu z EduPage (R19) |
| **requests** | stiahnutie .ics z odkazu | jednoduché HTTP požiadavky z Pythonu |
| **pytest** | automatické testy | štandard v Pythone |
| **Git + GitHub** | verzovanie, zálohovanie, Kanban | história zmien, prepojenie úloh s commitmi (R06) |
| **Visual Studio Code** | vývojové prostredie | vyžaduje zadanie (T4) |
