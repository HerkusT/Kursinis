# Spam Messages Detecting System

## Kaip paleisti programą

Atidaryk terminalą projekto aplanke ir paleisk:

```bash
python main.py
```

Kai programa paprašys CSV failo kelio, gali tiesiog spausti Enter.
Tada bus naudojamas numatytasis failas:

```text
data/messages.csv
```

Kai programa paprašys rezultatų failo kelio, taip pat gali spausti Enter.
Rezultatai bus išsaugoti čia:

```text
results/detection_results.csv
```

## Kaip paleisti testus

```bash
python -m unittest discover tests
```

## Projekto struktūra

```text
main.py
spam_detection/
    detectors/
    models/
    services/
    utils/
data/
results/
tests/
reportas.md
```
