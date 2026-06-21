# IT Parc — Module Odoo 18

Module de gestion de parc informatique développé pour **TECHPARK CI** dans le cadre du cours de développement Odoo 18.

---

## Informations générales

| Champ | Valeur |
|---|---|
| Nom du module | IT Parc - Gestion de Parc Informatique |
| Version | 18.0.1.0.0 |
| Auteur | Djea Seasiekan Nelikah |
| Odoo | 18.0 |
| Licence | LGPL-3 |
| GitHub | [nelykah-dev/it_parc](https://github.com/nelykah-dev/it_parc) |

---

## Fonctionnalités

1. **Gestion des équipements** — Suivi complet avec workflow 4 états (Disponible, Affecté, En Maintenance, Hors Service)
2. **Affectation des employés** — Lien avec le module RH, historique des affectations
3. **Suivi des interventions** — Gestion des interventions techniques avec calcul automatique de la durée
4. **Contrats fournisseurs** — Suivi des contrats avec calcul automatique des jours restants
5. **Alertes automatiques** — Génération automatique via cron job (contrats expirants, maintenances dues)
6. **Rapports PDF** — 3 rapports QWeb (Fiche équipement, Inventaire global, Rapport interventions)
7. **Exports Excel** — 3 exports via xlsxwriter (Équipements, Interventions, Contrats)
8. **Dashboard OWL** — Tableau de bord avec 8 KPIs et 1 graphique en barres

---

## Prérequis

- Odoo 18.0
- Python 3.11+
- PostgreSQL 14+
- wkhtmltopdf (pour les rapports PDF)
- xlsxwriter (inclus dans requirements.txt)

---

## Installation

### Étape 1 — Cloner le dépôt

```bash
git clone https://github.com/nelykah-dev/it_parc.git
```

### Étape 2 — Copier le module dans le dossier addons

Sur Linux/Mac :
```bash
cp -r it_parc /chemin/vers/odoo-18.0/addons/
```

Sur Windows :
```bash
xcopy /E /I it_parc C:\chemin\vers\odoo-18.0\addons\it_parc
```

### Étape 3 — Installer les dépendances Python

```bash
pip install -r requirements.txt
```

### Étape 4 — Installer le module

```bash
python odoo-bin -c odoo.conf -d NOM_BASE -i it_parc
```

Ou via l'interface : **Apps** → rechercher `it_parc` → **Activer**

---

## Structure du module

it_parc/ 

├── init.py

 ├── manifest.py ├── 

README.md 

├── models/ 

│ ├── init.py

 │ ├── it_equipement.py │ 

├── 

it_intervention.py 

│ ├── it_contrat.py │ ├── it_alerte.py 

│ └── it_parc_excel.py 

├── views/ 

│ ├── it_equipement_views.xml 

│ ├── it_intervention_views.xml 

│ ├── it_contrat_views.xml 

│ ├── it_alerte_views.xml 

│ └── menu_views.xml 

├── report/ 

│ └── it_parc_reports.xml 

├── security/ 

│ └── ir.model.access.csv 

├── data/ 

│ ├── it_parc_cron.xml 

│ └── it_parc_demo.xml 

└── static/ 

└── src/ 

└── components/ 

├── dashboard.js 

├── dashboard.xml 

└── dashboard.css

---

## Données de démonstration

Le fichier `it_parc_demo.xml` contient :
- **10 équipements** (ordinateurs, imprimantes, serveurs, équipements réseau)
- **3 contrats fournisseurs**
- **5 interventions techniques**

---

## Groupes de sécurité

| Groupe | Droits |
|---|---|
| Utilisateur (base.group_user) | Lecture seule |
| Administrateur (base.group_system) | Lecture, Écriture, Création, Suppression |

---

## Modèles

| Modèle | Description |
|---|---|
| it.equipement | Équipements informatiques |
| it.intervention | Interventions techniques |
| it.contrat | Contrats fournisseurs |
| it.alerte | Alertes automatiques |

---

## Cron Job

**IT Parc : Générer les alertes automatiques**
- Fréquence : 1 fois par jour
- Fonction : `it.alerte._cron_generer_alertes()`
- Génère automatiquement des alertes pour les contrats expirant dans moins de 30 jours

---

## Auteur

**Djea Seasiekan Nelikah** — Étudiante L2 Génie Logiciel, Institut Ivoirien de Technologie (IIT)

- GitHub : [nelykah-dev](https://github.com/nelykah-dev)
- LinkedIn : [nelikah-djea](https://www.linkedin.com/in/nelikah-djea-0038a8407/)
- Email : floredjea4@gmail.com