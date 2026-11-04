# Plánované rozšírenia (po MVP)

MVP robí účty, prihlasovanie aj kalendár **vlastnými silami** (R11). Integrácie s inými službami prídu až po dokončení MVP,
a to v poradí od najľahšej. Architektúra je na ne pripravená:

- integrácie budú v samostatnom module (blueprint `integrations`), ostatné moduly sa nemenia,
- tabuľka používateľov dostane neskôr voliteľné stĺpce (napr. `google_id`),
- udalosti zostávajú v databáze ADAM-a; externé služby sú iba doplnok, nie zdroj dát.

| Poradie | Rozšírenie | Ako | Náročnosť | Riziká |
|---|---|---|---|---|
| 1 | **Export kalendára (.ics)** | ADAM vygeneruje súkromný odkaz vo formáte iCalendar; používateľ si ho pridá do Google/Apple kalendára | nízka | odkaz musí byť tajný (náhodný token) |
| 2 | **Prihlásenie cez Google** | OAuth 2.0 ako druhá možnosť popri hesle | stredná | Google Cloud projekt, nastavenie OAuth |
| 3 | **Synchronizácia s Google Calendar API** | obojsmerná synchronizácia udalostí | vysoká | konflikty zmien, limity API |
| 4 | **Import známok a úloh z EduPage** (rozvrh je už v MVP cez .ics, R19) | neoficiálne API | vysoká | API sa môže kedykoľvek zmeniť; treba ukladať heslo do EduPage; osobné údaje žiakov (GDPR) |

## Prečo nie hneď v MVP

- Zadanie vyžaduje vlastnú registráciu, prihlásenie a ukladanie do databázy, teda presne to, čo robí MVP.
- Vlastné riešenie viem na obhajobe vysvetliť do detailu.
- Demo na obhajobe nezávisí od internetu ani od služieb tretích strán.
