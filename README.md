# Automation Project

This project includes UI and API automation using Python.

## 🔧 Requirements

- Python 3.8+

## 📦 Install dependencies

```bash
py -m pip install playwright pytest requests
py -m playwright install
```

## 🚀 Run Tests

```bash
py -m pytest tests/
```

## ✅ Tests Covered

### UI
- Google Search for "synot games"
  - Checks results returned
  - Checks one contains "synot games"

### API
- Dog CEO (random dog image)
- Cat Fact (random cat fact)
