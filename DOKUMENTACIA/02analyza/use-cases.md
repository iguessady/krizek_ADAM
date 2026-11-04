# Prípady použitia (use cases)

## Aktéri

- **Návštevník**: neprihlásený človek.
- **Študent**: prihlásený používateľ.

## Diagram prípadov použitia

> Do práce treba nakresliť ako obrázok (napr. draw.io alebo PlantUML). Toto je textová predloha.

```
Návštevník ── (Registrácia)            F01
Návštevník ── (Prihlásenie)            F02

Študent ── (Odhlásenie)                F02
Študent ── (Zobrazenie dashboardu)     F21
Študent ── (Nastavenie triedy)         F05
Študent ── (Správa predmetov)          F06
Študent ── (Zadanie rozvrhu)           F07, F08
Študent ── (Správa zadaní)             F09, F10, F11
Študent ── (Správa známok)             F12, F13
Študent ── (Zobrazenie priemerov)      F14, F15
Študent ── (Správa udalostí)           F16, F17, F18
Študent ── (Zobrazenie upozornení)     F19, F20
```

## User stories

Formát: *Ako [kto] chcem [čo], aby [prečo].*

1. Ako návštevník chcem vytvoriť účet, aby som si mohol ukladať svoje údaje. (F01)
2. Ako študent sa chcem prihlásiť z ľubovoľného zariadenia, aby som mal údaje vždy pri sebe. (F02, F04)
3. Ako študent chcem po prihlásení vidieť dashboard, aby som hneď vedel, čo ma čaká. (F21)
4. Ako študent chcem pridať svoje predmety, aby som k nim mohol priraďovať zadania a známky. (F06)
5. Ako študent chcem zadať rozvrh, aby som ho mal stále po ruke. (F07, F08)
6. Ako študent chcem pridať domácu úlohu s termínom, aby som na ňu nezabudol. (F09)
7. Ako študent chcem označiť úlohu ako hotovú, aby som videl, čo mi ešte zostáva. (F10)
8. Ako študent chcem vidieť úlohy podľa predmetov, aby som sa vedel sústrediť na jeden predmet. (F11)
9. Ako študent chcem zapísať známku, aby som mal prehľad o výsledkoch. (F12)
10. Ako študent chcem vidieť priemer z predmetu, aby som vedel, ako na tom som. (F14, F15)
11. Ako študent chcem pridať do kalendára aj tréning, aby som videl školu aj voľný čas spolu. (F16)
12. Ako študent chcem byť upozornený na test o 2 dni, aby som sa stihol pripraviť. (F19)

## Podrobný príklad: Pridanie známky

| | |
|---|---|
| **Aktér** | Študent |
| **Predpoklad** | Študent je prihlásený a má vytvorený aspoň jeden predmet. |
| **Hlavný scenár** | 1. Študent otvorí stránku Známky. 2. Klikne na „Add grade". 3. Vyberie predmet, zadá známku, váhu a dátum. 4. Klikne na „Save". 5. Aplikácia uloží známku a prepočíta priemer. |
| **Alternatíva** | 3a. Študent zadá známku mimo 1–5 → aplikácia zobrazí chybu a známku neuloží. |
| **Výsledok** | Známka je uložená, priemer predmetu aj celkový priemer sú aktualizované. |
