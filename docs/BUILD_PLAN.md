# Build plan (terrain préparé)

## 1) Pré-requis
- Python 3.10+
- Chrome ou Firefox
- Driver navigateur (chromedriver/geckodriver) accessible

## 2) Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 3) Configuration
Variables d'environnement supportées :
- `WFR_BASE_URL` (default: `http://localhost:3000`)
- `WFR_SIGNUP_PATH` (default: `/signup`)
- `WFR_BROWSER` (`chrome`/`firefox`, default: `chrome`)
- `WFR_HEADLESS` (`true`/`false`, default: `true`)
- `WFR_TIMEOUT_SECONDS` (default: `20`)
- `WFR_OUTPUT_DIR` (default: `artifacts`)

## 4) Exécution
```bash
python -m web_flow_recorder.runner
```

## 5) Sorties
- `artifacts/report.json`
- `artifacts/screenshots/*.png` (en cas d'échec)

## 6) Durcissement recommandé
- Ajouter une étape CI dédiée.
- Mettre en place pytest + markers smoke/regression.
- Versionner les jeux de données de test.


## 7) Orchestration Ralph
```bash
ralph prd "Créer un outil Python Selenium pour automatiser des tests QA d'inscription sur environnement autorisé (staging/dev), avec reporting JSON et screenshots en échec."
ralph build 1 --no-commit --prd .agents/tasks/prd-qa-signup-selenium.json
```

Notes:
- La commande `ralph build` consomme un PRD au format JSON contenant des `stories`.
- Le PRD d'exemple pour ce dépôt est: `.agents/tasks/prd-qa-signup-selenium.json`.
