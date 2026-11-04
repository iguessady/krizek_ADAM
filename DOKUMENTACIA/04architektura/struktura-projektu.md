# Štruktúra projektu

```
krizek_ADAM/
├── README.md                 popis projektu, inštalácia, spustenie
├── requirements.txt          zoznam Python knižníc (pip install -r requirements.txt)
├── .gitignore                čo git ignoruje (databáza, venv/, __pycache__/)
├── run.py                    spustenie aplikácie (python run.py)
├── config.py                 nastavenia (SECRET_KEY, cesta k databáze)
│
├── app/
│   ├── __init__.py           create_app(): vytvorí aplikáciu, pripojí databázu, Flask-Login a blueprinty
│   ├── models.py             databázové tabuľky ako Python triedy
│   ├── routes/               jeden súbor = jeden modul (blueprint)
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   ├── subjects.py       trieda, predmety, rozvrh
│   │   ├── tasks.py
│   │   ├── grades.py
│   │   ├── calendar.py
│   │   └── reminders.py      výpočet upozornení (používa ho dashboard)
│   ├── templates/
│   │   ├── base.html         spoločný layout: hlavička, menu, správy (flash)
│   │   ├── auth/  dashboard/  subjects/  tasks/  grades/  calendar/
│   └── static/
│       ├── css/style.css
│       ├── js/
│       └── img/
│
├── instance/
│   └── adam.db               databáza SQLite (nie je v gite)
├── tests/                    automatické testy (pytest)
└── DOKUMENTACIA/             dokumentácia projektu
```

## Prečo takto

- **Application factory (`create_app`)**: aplikácia sa dá vytvoriť viackrát s rôznym nastavením, napr. pre testy s prázdnou databázou.
- **Blueprinty**: každá funkcia má vlastný súbor, kód sa dá ľahko nájsť a rozširovať (nový modul = nový blueprint).
- **`instance/` mimo gitu**: databáza obsahuje údaje používateľov a nepatrí na GitHub.
- **`config.py`**: tajné hodnoty (SECRET_KEY) sa nenachádzajú priamo v kóde a dajú sa zmeniť pri hostingu.
