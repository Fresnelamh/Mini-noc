# Post-mortem — Incident #01 : arrêt du service Flask

## Résumé
Le service Flask a été arrêté manuellement pour simuler une panne de production.
L'incident a duré environ 2 heures avant résolution complète.

## Chronologie
- 18h00 — Arrêt du container Flask (docker compose stop flask)
- 18h01 — Courbe Grafana s'aplatit, app ne répond plus
- 19h50 — Relance du service (docker compose up -d)
- 19h50 — Remontée confirmée sur Grafana

## Cause racine
Arrêt manuel du container sans procédure de redémarrage automatique en place.

## Impact
- Application indisponible pendant 2 heures
- 0 utilisateurs réels impactés (environnement de test)

## Ce qui a bien fonctionné
- Grafana a détecté la panne via le graphique
- L'alerte configurée s'est déclenchée
- La résolution a été rapide grâce au runbook

## Ce qui peut être amélioré
- Ajouter restart: always sur tous les services
- Mettre en place une notification email automatique

## Actions correctives
| Action | Responsable | Deadline |
|--------|------------|----------|
| Ajouter restart policy sur tous les services | Fresnel |
| Configurer alerte email Grafana | Fresnel |