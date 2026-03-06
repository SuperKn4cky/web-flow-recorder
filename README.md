# web-flow-recorder

Outil Python prêt à être étendu pour automatiser des parcours QA d'inscription via Selenium sur un environnement autorisé.

## Démarrage rapide

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m web_flow_recorder.runner
```

## Variables d'environnement

- `WFR_BASE_URL` (default `http://localhost:3000`)
- `WFR_SIGNUP_PATH` (default `/signup`)
- `WFR_BROWSER` (`chrome`/`firefox`)
- `WFR_HEADLESS` (`true`/`false`)
- `WFR_TIMEOUT_SECONDS` (default `20`)
- `WFR_OUTPUT_DIR` (default `artifacts`)

## Documentation

- PRD (format RALPH): `docs/RALPH_PRD.md`
- Plan de build: `docs/BUILD_PLAN.md`

## Workflow Ralph (PRD + build)

```bash
ralph prd "Créer un outil Python Selenium pour automatiser des tests QA d'inscription sur environnement autorisé (staging/dev), avec reporting JSON et screenshots en échec."
ralph build 1 --no-commit --prd .agents/tasks/prd-qa-signup-selenium.json
```

Le PRD Ralph utilisé pour le build est versionné ici : `.agents/tasks/prd-qa-signup-selenium.json`.
