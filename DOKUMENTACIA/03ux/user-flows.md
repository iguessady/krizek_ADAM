# User flows

User flow = cesta, ktorou používateľ prejde aplikáciou, aby niečo dosiahol. Z týchto ciest sa potom kreslia wireframy:
každý rámček `[Obrazovka]` je jedna obrazovka, ktorú treba nakresliť.

> Návrh (2026-11-05). Texty v aplikácii sú po anglicky (R05), preto sú názvy tlačidiel v úvodzovkách po anglicky.

## Zoznam obrazoviek (mapa aplikácie)

```
Neprihlásený                 Prihlásený (menu: Dashboard · Timetable · Tasks · Grades · Calendar · Account)
─────────────                ────────────────────────────────────────────────────────────────────────────
[Login]                      [Dashboard]
[Register]                   [Timetable]            [Timetable import]
                             [Tasks]                [Task form]       (pridať / upraviť)
                             [Grades]               [Grade form]      (pridať / upraviť)
                             [Subjects]             [Subject form]
                             [Calendar]             [Event form]
                             [Account]              [Change password] [Delete account]
```

## 1. Registrácia a prvé spustenie (F01, F25, F26)

```
[Register] ── vyplní e-mail, nick, heslo 2× ── "Sign up"
     │  chyba (e-mail už existuje, heslá sa nezhodujú) → zostane na [Register] s hláškou
     ▼
[Timetable import]  ← povinné, z tejto obrazovky sa nedá odísť inam (F26)
     │  návod: „V EduPage: Rozvrh → Export do kalendára → skopíruj odkaz"
     │  vloží odkaz ── "Import"
     │  chyba (zlý odkaz, EduPage neodpovedá) → zostane s hláškou
     ▼
Súhrn importu: „Imported 13 subjects, 31 lessons, 6 school events, 2 assignments"
     ▼
[Dashboard]
```

## 2. Prihlásenie (F02)

```
[Login] ── e-mail + heslo ── "Log in"
     │  chyba → hláška „Wrong e-mail or password" (nehovoríme, ktoré z nich je zlé)
     ▼
nemá rozvrh? ──áno──▶ [Timetable import]
     │ nie
     ▼
[Dashboard]
```

## 3. Ranný prehľad (F21, F19, F20) – najčastejšia cesta

```
[Dashboard]
  ├─ Upozornenia: zmeškané (červené) a blížiace sa (oranžové) zadania
  ├─ Dnešný rozvrh
  ├─ Najbližšie udalosti (dnes + niekoľko dní)
  ├─ Nehotové zadania  ── klik na ☐ ──▶ označené ako hotové (zostáva na [Dashboard])
  └─ Priemery predmetov + celkový priemer ── klik ──▶ [Grades]
```

## 4. Pridanie zadania (F09, F22)

```
[Dashboard] alebo [Tasks] ── "+ Add task"
     ▼
[Task form]  predmet ▾, názov, typ ▾ (homework/test/project/other), termín, upozorniť X dní vopred (3), popis
     │ "Save"   (chyba → zostane s hláškou pri poli)
     ▼
[Tasks] s novým zadaním + hláška „Task added"
```

## 5. Hotové zadanie a známka k nemu (F10, F12)

```
[Tasks] ── ☐ pri zadaní ──▶ hotové
     │  (pri type test/project) ponuka: „Add a grade for this task?"
     ▼ áno
[Grade form]  predmet a zadanie už vyplnené; druh ▾ (mark / points / percent) → zobrazia sa len potrebné polia; váha, dátum
     │ "Save"
     ▼
[Grades] s prepočítaným priemerom
```

## 6. Pridanie známky (F12–F15)

```
[Grades] ── "+ Add grade" ──▶ [Grade form] ── "Save" ──▶ [Grades]
[Grades]: tabuľka predmetov → klik na predmet → zoznam známok, priemer v % aj ako známka
```

## 7. Kalendár (F16–F18, F27)

```
[Calendar] (mesiac/týždeň, FullCalendar)
  ├─ klik na prázdny deň ──▶ [Event form] (dátum predvyplnený) ── "Save" ──▶ [Calendar]
  ├─ klik na udalosť ──▶ [Event form] (upraviť / "Delete")
  └─ klik na termín zadania ──▶ [Task form]
```

## 8. Opätovný import rozvrhu (F25, F27, F28)

```
[Timetable] ── "Re-import from EduPage"
     ▼
potvrdenie: „Your timetable will be replaced. Your tasks, grades and events stay."
     ▼
súhrn importu ──▶ [Timetable]
```

## 9. Predmety (F06, R16)

```
[Subjects] ── klik na predmet ──▶ [Subject form] (názov, skratka, farba) ── "Save"
[Subjects] ── "Delete" ──▶ potvrdenie: „Delete MAT with 4 tasks and 7 grades?" ── "Delete" ──▶ [Subjects]
[Subjects] ── "+ Add subject" ──▶ predmet mimo rozvrhu (R22)
```

## 10. Účet (F23, F24)

```
[Account] ── "Change password" ──▶ staré heslo + nové 2× ── "Save" ──▶ [Account] + hláška
[Account] ── "Delete account" ──▶ zadá heslo + potvrdí ──▶ odhlásený, [Login] + hláška „Account deleted"
[ktorákoľvek] ── "Log out" ──▶ [Login]
```
