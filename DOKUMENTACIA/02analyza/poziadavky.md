# Požiadavky

Každá funkčná požiadavka má číslo (F01, F02, ...) a odkaz na vetu zo zadania, z ktorej vychádza.
Tak sa dá ukázať, že zadanie je pokryté na 100 %. Čísla požiadaviek sa neskôr použijú ako názvy issues na GitHube.

## Vety zo zadania

| Kód | Veta zo zadania ([Zadanie_PCOZ.pdf](../00zadanie/Zadanie_PCOZ.pdf)) |
|---|---|
| Z1 | „Navrhnite a vytvorte webovú aplikáciu pre študentov na organizáciu školských povinností a voľného času." |
| Z2 | „Má obsahovať dashboard, v ktorom je kalendár, … to-do list zadaní, priemer známok a dôležité upozornenia ako testy, či domáce úlohy." |
| Z3 | „… kalendár, kde si vie používateľ upraviť udalosti …" |
| Z4 | „Používateľ si vie pridať svoju vlastnú triedu, rozvrh …" |
| Z5 | „… a rozdeliť si zadania podľa predmetov a pridať ich výsledky." |
| Z6 | „Aplikácia umožní používateľovi registráciu, prihlásenie a ukladanie údajov do databázy." |
| T1 | „Programovanie back-end v Python." |
| T2 | „Programovanie front-end v HTML5, CSS, JavaScript." |
| T3 | „Databáza SQLite" |
| T4 | „Vývojové prostredie Visual Studio Code." |

## Funkčné požiadavky (čo aplikácia robí)

### Účty používateľov
| ID | Požiadavka | Zo zadania |
|---|---|---|
| F01 | Používateľ sa vie zaregistrovať (meno, e-mail, heslo). | Z6 |
| F02 | Používateľ sa vie prihlásiť a odhlásiť. | Z6 |
| F03 | Každý používateľ vidí iba svoje údaje. | Z6 |
| F04 | Všetky údaje sa ukladajú do databázy a zostanú zachované aj po odhlásení. | Z6 |
| F23 | Používateľ si vie zmeniť heslo (R18). | Z6 |
| F24 | Používateľ si vie zmazať účet aj so všetkými údajmi (R18). | Z6 |

### Trieda, predmety, rozvrh
| ID | Požiadavka | Zo zadania |
|---|---|---|
| F05 | Používateľ si vie nastaviť svoju triedu (napr. „IV.C", škola, školský rok). | Z4 |
| F06 | Používateľ si vie pridať, upraviť a zmazať predmety (názov, skratka, farba). Zmazanie predmetu po potvrdení zmaže aj jeho zadania a známky (R16). | Z4, Z5 |
| F07 | Používateľ si vie zadať týždenný rozvrh (deň, hodina, predmet, prípadne učebňa). | Z4 |
| F08 | Aplikácia zobrazí rozvrh v prehľadnej tabuľke. | Z4 |
| F25 | Používateľ si vie importovať rozvrh vložením svojho odkazu na kalendár z EduPage (.ics); predmety, ktoré ešte nemá, sa vytvoria automaticky (R19). | Z4 |
| F26 | Po registrácii musí používateľ zadať alebo importovať rozvrh, inak sa nedostane na dashboard; z rozvrhu sa vytvorí zoznam predmetov (R20). | Z4 |

### Zadania (to-do list)
| ID | Požiadavka | Zo zadania |
|---|---|---|
| F09 | Používateľ si vie pridať zadanie k predmetu (názov, popis, termín, typ: domáca úloha / test / projekt). | Z2, Z5 |
| F10 | Používateľ vie zadanie upraviť, zmazať a označiť ako hotové. | Z2 |
| F11 | Zadania sa dajú zobraziť rozdelené podľa predmetov. | Z5 |

### Známky
| ID | Požiadavka | Zo zadania |
|---|---|---|
| F12 | Používateľ si vie pridať známku k predmetu ako známku 1–5 (aj s +/-), body (získané/maximum) alebo percentá, s váhou, dátumom a poznámkou, prípadne priamo k zadaniu ako jeho výsledok (R21). | Z5 |
| F13 | Používateľ vie známku upraviť a zmazať. | Z5 |
| F14 | Aplikácia automaticky vypočíta vážený priemer z každého predmetu: všetky známky prevedie na percentá a priemer zobrazí v percentách aj ako známku (R21). | Z2 |
| F15 | Aplikácia zobrazí celkový priemer zo všetkých predmetov. | Z2 |

### Kalendár
| ID | Požiadavka | Zo zadania |
|---|---|---|
| F16 | Používateľ si vie pridať udalosť do kalendára (názov, dátum, čas, popis), aj mimoškolskú. | Z1, Z3 |
| F17 | Používateľ vie udalosť upraviť a zmazať. | Z3 |
| F18 | Kalendár zobrazuje udalosti aj termíny zadaní (mesačný/týždenný pohľad). | Z2, Z3 |

### Upozornenia
| ID | Požiadavka | Zo zadania |
|---|---|---|
| F19 | Aplikácia upozorní na blížiace sa testy a domáce úlohy (termín do X dní, X podľa nastavenia, predvolené 3). | Z2 |
| F20 | Aplikácia upozorní na zadania po termíne, ktoré nie sú hotové. | Z2 |
| F22 | Používateľ si vie nastaviť, koľko dní dopredu chce upozornenia (R17). | Z2 |

### Dashboard
| ID | Požiadavka | Zo zadania |
|---|---|---|
| F21 | Po prihlásení sa zobrazí dashboard s: kalendárom (najbližšie dni), to-do listom, priemerom známok a upozorneniami. | Z2 |

## Nefunkčné požiadavky (ako aplikácia funguje)

| ID | Požiadavka | Zo zadania |
|---|---|---|
| N01 | Back end je napísaný v Pythone (framework Flask). | T1 |
| N02 | Front end je napísaný v HTML5, CSS (Bootstrap) a JavaScripte. | T2 |
| N03 | Údaje sú uložené v databáze SQLite. | T3 |
| N04 | Projekt sa vyvíja vo Visual Studio Code. | T4 |
| N05 | Aplikácia beží vo webovom prehliadači a dá sa používať aj na mobile (responzívny dizajn). | Z1 |
| N06 | Heslá sú uložené iba ako hash (nikdy nie v čitateľnej podobe). | Z6 |
| N07 | Stránky okrem registrácie a prihlásenia sú dostupné iba prihlásenému používateľovi. | Z6 |
| N08 | Formuláre kontrolujú vstupy (povinné polia, platný dátum, známka 1–5, body ≤ maximum, percentá 0–100). | — |
| N09 | Texty v aplikácii sú v angličtine (pozri [rozhodnutia](../01planovanie/rozhodnutia.md)). | — |
| N10 | Bežná akcia (pridanie úlohy, známky) zaberie najviac pár kliknutí. | — |
| N11 | Odkaz na kalendár z EduPage sa považuje za citlivý údaj (funguje ako heslo): nezobrazuje sa celý, nie je v kóde ani v gite. | — |

## Kontrola pokrytia zadania

| Veta zo zadania | Požiadavky |
|---|---|
| Z1 | F16, N05 |
| Z2 | F09, F10, F14, F15, F18, F19, F20, F21, F22 |
| Z3 | F16, F17, F18 |
| Z4 | F05, F06, F07, F08, F25, F26 |
| Z5 | F06, F09, F11, F12, F13 |
| Z6 | F01, F02, F03, F04, F23, F24, N06, N07 |
| T1–T4 | N01–N04 |

Každá veta zadania je pokrytá aspoň jednou požiadavkou.
