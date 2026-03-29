# Runbook — Service Flask indisponible

## Sévérité
P1 — Critique

## Systèmes impactés
Application Flask, Nginx

## Symptômes
- http://localhost ne répond plus
- Courbe Grafana s'aplatit
- healthcheck.log affiche DOWN

## Diagnostic

1. Vérifier l'état des containers :
   docker compose ps

2. Lire les logs du service Flask :
   docker compose logs flask

3. Vérifier si le container est arrêté ou en erreur

## Résolution

1. Relancer le service Flask :
   docker compose start flask

2. Vérifier que le service répond :
   curl http://localhost

3. Confirmer la remontée sur Grafana

## Critères de clôture
- http://localhost répond avec statut 200
- Courbe Grafana repart à la hausse

## Escalade
Si le service ne repart pas après 3 tentatives :
   docker compose up -d --build flask