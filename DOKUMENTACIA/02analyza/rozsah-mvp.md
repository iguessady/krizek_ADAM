# Rozsah MVP

MVP (minimum viable product) je najmenšia verzia aplikácie, ktorá **splní celé zadanie**.
Všetko ostatné je až po MVP, ak zostane čas. Tento zoznam chráni projekt pred nekonečným pridávaním funkcií.

## Patrí do MVP

Všetky požiadavky F01 až F26 a N01 až N11 z [poziadavky.md](poziadavky.md):

- registrácia, prihlásenie, odhlásenie,
- trieda, predmety, týždenný rozvrh (importom z EduPage cez .ics odkaz),
- zadania podľa predmetov (pridať, upraviť, zmazať, hotové),
- známky s automatickým (váženým) priemerom,
- kalendár udalostí,
- upozornenia **priamo v aplikácii** (na dashboarde),
- dashboard,
- responzívny dizajn.

## Nepatrí do MVP (možné rozšírenia)

| Funkcia | Prečo nie teraz |
|---|---|
| Upozornenia e-mailom alebo push notifikácie | potrebujú e-mailový server alebo službu, zadanie hovorí len o upozorneniach |
| Zdieľaná trieda pre viacerých študentov | zložitejšie práva a dáta; „vlastná trieda" v zadaní stačí pre jedného používateľa |
| Export kalendára (.ics), prihlásenie cez Google, synchronizácia s Google Calendar | rozšírenia po MVP, pozri [rozsirenia.md](../04architektura/rozsirenia.md) |
| Import známok a úloh z EduPage | EduPage nemá oficiálne API; neoficiálne je rizikové (pozri R11). Rozvrh sa importuje cez oficiálny .ics export už v MVP (R19). |
| Obnovenie zabudnutého hesla e-mailom | potrebuje e-mailový server |
| Komunikácia medzi používateľmi (správy, zdieľanie) | nie je v zadaní |
| Tmavý režim | kozmetika |
| Párny/nepárny týždeň v rozvrhu | v MVP netreba (R15) |
| Ručné zadávanie rozvrhu | rozvrh sa iba importuje z EduPage; hodiny navyše sa pridajú do kalendára (R23) |
| Opakované udalosti v kalendári (napr. každý utorok) | zložitá logika; dá sa doplniť neskôr |
| Štatistiky a grafy vývoja známok | pekné, ale nie v zadaní |
| Mobilná aplikácia | stačí responzívny web |

## Predpoklady, ktoré treba potvrdiť

- „Vlastná trieda" = študent si zadá svoju triedu a rozvrh len pre seba (nie zdieľaná s inými).
- Známky môžu byť známka 1–5, body alebo percentá; priemer sa počíta v percentách (R21). Váha je voliteľná (predvolená 1).
