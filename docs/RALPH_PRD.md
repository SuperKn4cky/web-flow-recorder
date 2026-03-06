# RALPH PRD — Outil Python d'automatisation QA du parcours d'inscription

## R — Requirements (Besoins)

### Problème
Les validations manuelles du parcours d'inscription sont lentes et peu fiables d'un sprint à l'autre.

### Objectif produit
Créer un outil Python basé sur Selenium pour exécuter automatiquement des scénarios d'inscription sur un environnement autorisé (staging/dev), avec reporting exploitable.

### Utilisateurs
- QA engineers
- Développeurs front/back
- Release managers

### Exigences fonctionnelles
1. Exécuter des scénarios positifs et négatifs d'inscription.
2. Utiliser des données de test générées.
3. Produire un rapport JSON d'exécution.
4. Capturer des captures d'écran en cas d'échec.
5. Permettre un lancement CLI simple.

### Exigences non fonctionnelles
- Configurable via variables d'environnement
- Compatible Chrome/Firefox
- Logs lisibles en CI
- Structure prête pour extension (Page Object Model)

## A — Architecture

### Composants
- `config.py` : charge la configuration runtime.
- `driver_factory.py` : instancie le WebDriver selon le navigateur.
- `pages/` : objets pages Selenium (POM).
- `data_factory.py` : génération de données d'inscription.
- `runner.py` : orchestration des scénarios et reporting.

### Flux principal
1. Charger la configuration.
2. Initialiser le navigateur.
3. Ouvrir la page d'inscription.
4. Exécuter le scénario.
5. Reporter le résultat.
6. Fermer proprement le navigateur.

## L — Lifecycle (Roadmap)

### Milestone 1 (actuel)
- Squelette projet Python
- PRD et documentation build
- Runner CLI + scénario de base

### Milestone 2
- Scénarios d'erreur complets
- Intégration Pytest/Allure
- Exécution CI

### Milestone 3
- Matrice multi-navigateurs
- Dashboard de métriques qualité

## P — Plan d'implémentation

1. Initialiser la structure du package Python.
2. Ajouter gestion de configuration par variables d'environnement.
3. Ajouter Page Objects du flux signup.
4. Ajouter un runner CLI et un export JSON.
5. Documenter usage, limites et prochaines étapes.

## H — Hypothèses et risques

### Hypothèses
- Le site cible est autorisé et contrôlé (staging/dev).
- Les sélecteurs HTML sont stables.

### Risques
- Flakiness UI liée au timing.
- Divergence des environnements.

### Mitigation
- Utiliser des attentes explicites Selenium.
- Isoler les données de test.
- Ajouter des retries ciblés si nécessaire.
