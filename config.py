import os

class Config:
    # tajný kľúč na podpisovanie cookies; v produkcii sa nastaví cez premennú prostredia
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-zmen-ma")