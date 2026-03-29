# Mini-NOC

A self-hosted production environment featuring a Python/Flask API, Docker Compose
orchestration, GitHub Actions CI/CD pipeline, and real-time monitoring with
Prometheus & Grafana — including incident simulation, runbook, and post-mortem.

## Architecture
```
Internet → Nginx (port 80) → Flask API (port 5000)
                                    ↓
                            Prometheus (port 9090)
                                    ↓
                            Grafana (port 3000)
```

## Lancer le projet

Prérequis : Docker Desktop installé
```
git clone https://github.com/TON-PSEUDO/mini-noc.git
cd mini-noc
docker compose up -d
```

## Services disponibles

| Service | URL |
|---------|-----|
| Application | http://localhost |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

## CI/CD

Chaque push sur main déclenche automatiquement le pipeline GitHub Actions :
build de l'image Docker → test de démarrage → validation.

## Monitoring

Prometheus scrape les métriques Flask toutes les 15 secondes.
Grafana affiche un dashboard en temps réel avec statut, requêtes et erreurs.
Une alerte se déclenche automatiquement si l'app est indisponible.

## Documentation opérationnelle

- Runbook : [service Flask indisponible](runbooks/runbook-service-down.md)
- Post-mortem : [incident #01](runbooks/postmortem-incident-01.md)