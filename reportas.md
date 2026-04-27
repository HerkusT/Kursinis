# Spam žinučių aptikimo sistema

## 1. Įvadas

Šio kursinio darbo tikslas yra sukurti spam žinučių aptikimo sistemą naudojant Python programavimo kalbą ir objektinio programavimo (OOP) principus.

Programa nuskaito žinutes iš failo ir nustato, ar jos yra spam, ar ne. Tam naudojami skirtingi aptikimo metodai.

### Kaip paleisti programą
- Atidaryti terminalą
- Pereiti į projekto aplanką
- Paleisti komandą:
  python main.py

### Kaip naudotis programa
- Programa nuskaito žinutes iš CSV failo
- Kiekviena žinutė yra patikrinama
- Rezultatai išsaugomi į kitą failą

---

## 2. Darbo analizė

### Programos struktūra

Sistema sudaryta iš kelių klasių:
- Message klasė saugo žinutės tekstą
- Detector klasės tikrina, ar žinutė yra spam
- SpamDetectionSystem valdo visą procesą

---

### OOP principų taikymas

#### Enkapsuliacija
Duomenys saugomi klasėse ir pasiekiami per metodus.

#### Paveldėjimas (Inheritance)
Skirtingi detektoriai paveldi bendrą bazinę klasę.

#### Polimorfizmas (Polymorphism)
Visi detektoriai naudoja tą patį metodą detect(), bet veikia skirtingai.

#### Abstrakcija (Abstraction)
Naudojama abstrakti klasė, kuri apibrėžia bendrus metodus.

---

### Naudotas dizaino šablonas

Buvo panaudotas Factory Method šablonas.

Jis leidžia lengvai kurti skirtingus detektorius nekeičiant pagrindinės programos logikos.

---

### Kompozicija

SpamDetectionSystem klasė turi detektorių sąrašą.

Sistema naudoja kelis objektus kartu, kad priimtų sprendimą.

---

### Darbas su failais

- Žinutės nuskaitomos iš CSV failo
- Rezultatai išsaugomi į CSV failą

---

### Testavimas

Naudotas unittest modulis.

Testai tikrina, ar detektoriai veikia teisingai.

---

## 3. Rezultatai

- Sistema gali aptikti paprastas spam žinutes
- Keli detektoriai padidina tikslumą
- Buvo sunkumų organizuojant klases
- Failų nuskaitymas ir išsaugojimas veikia

---

## 4. Išvados

Sukurta veikianti spam aptikimo sistema.

Buvo pritaikyti pagrindiniai OOP principai.

Ateityje būtų galima:
- pridėti sudėtingesnius aptikimo metodus
- pagerinti tikslumą
- sukurti vartotojo sąsają
