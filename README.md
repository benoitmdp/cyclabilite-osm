# 🚲 OSM Cyclability Scoring

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-green)
![OpenStreetMap](https://img.shields.io/badge/data-OpenStreetMap-orange)

*An open-source methodology for assessing bicycle network quality.*

---

## 👨‍💻 À propos de l'auteur
Ce projet a été développé par **Benoît Chaumeret**, au sein de la **Mission Vélo de la Ville de Paris**, afin de fournir des outils d'aide à la décision basés sur la donnée ouverte et collaborative.

---

## 📸 Aperçu / Overview
![Screenshot](docs/capture.png)

## 🇫🇷 Français

### Présentation
**OSM Cyclability Scoring** est une méthodologie et un ensemble d'outils open source permettant d'évaluer la qualité des infrastructures cyclables à partir des données **OpenStreetMap**. 

Initialement développé dans le cadre des travaux de la **Mission Vélo de la Ville de Paris** pour analyser le réseau de la **Métropole du Grand Paris**, cet outil permet de qualifier finement chaque segment de voirie pour aider à la planification, au suivi du développement du vélo et à l'évaluation des politiques cyclables.

### Fonctionnalités principales
- ✅ **Analyse automatisée** des réseaux routiers OSM via `osmium`.
- ✅ **Détection intelligente** des aménagements (pistes, bandes, voies vertes, vélorues).
- ✅ **Analyse avancée** : doubles sens cyclables, chaussées séparées, analyse de proximité spatiale et chronologie des aménagements.
- ✅ **Sorties exploitables** : scores par segment, exports GeoParquet pour SIG, cartes interactives HTML.

---
## 🛠 Installation et Prérequis
Avant d'utiliser les scripts, vous devez configurer votre environnement de calcul (Python 3.10+ requis) :

1. **Cloner le projet** : `git clone <URL>`
2. **Créer l'environnement** :
   ```bash
   conda env create -f environment.yml
   conda activate mgp-extraction-env


## 🏗 Architecture du projet

Le projet est structuré en deux modules principaux pour garantir la reproductibilité des données et l'efficacité des traitements :

### 1. Module d'extraction des données (`osm-data-extract`)
Dédié à la préparation lourde des données :
* **Traitement Geofabrik** : Consommation des extraits historiques bruts d'OpenStreetMap.
* **Découpage temporel** : Extraction du réseau routier à des dates spécifiques (via `time-filter`) pour permettre des analyses comparatives.
* **Découpage spatial** : Définition des zones d'étude (MGP, Communes, Arrondissements) à partir des contours administratifs.
* **Optimisation** : Conversion des données nettoyées au format `GeoParquet` pour assurer la performance des calculs.

### 2. Moteur de calcul de la cyclabilité
Le cœur analytique du projet :
* **Scoring des infrastructures** : Application de la méthodologie de scoring par segment de voirie.
* **Calcul des indicateurs** : Gestion des doubles sens cyclables, détection des chaussées séparées et analyse de proximité.
* **Visualisation** : Génération de cartes web interactives et exports de données décisionnelles.


---

## 🇬🇧 English

### Overview
**OSM Cyclability Scoring** is an open-source methodology and toolkit designed to assess bicycle-friendliness using **OpenStreetMap** data.

Designed and refined by **Benoît Chaumeret (Mission Vélo, City of Paris)** for the **Greater Paris Metropolis (Métropole du Grand Paris)**, this project computes cyclability scores by integrating road hierarchy, infrastructure types, contraflow analysis, and spatial metrics to support data-driven urban planning.

### Main Features
- ✅ **Automatic analysis** of OSM road networks.
- ✅ **Infrastructure detection** (tracks, lanes, greenways, cycle streets).
- ✅ **Advanced metrics**: contraflow assessment, dual carriageway detection, spatial proximity.
- ✅ **Actionable outputs**: segment-level scoring, GeoParquet datasets, and interactive web maps.

---
## 🛠 Setup & Requirements
Before running the scripts, you need to configure your computing environment (Python 3.10+ required):

1. **Clone the project** : `git clone <URL>`
2. **Setup environment**:
   ```bash
   conda env create -f environment.yml
   conda activate mgp-extraction-env


## 🏗 Project Architecture

The project is structured into two main modules to ensure data reproducibility and efficient processing:

### 1. Module d'extraction des données (`osm-data-extract`)
Dédié à la préparation lourde des données :
* **Geofabrik Processing**: Consumes raw OSM historical extracts.
* **Temporal Slicing**: Extracts the road network at specific dates (via `time-filter`) to enable comparative analysis.
* **Spatial Clipping**: Defines study areas (MGP, Communes, Arrondissements) using administrative boundaries.
* **Optimization**: Converts cleaned data into `GeoParquet` format to ensure computational performance.

### 2. Cyclability Scoring Engine
The core logic for analysis:
* **Infrastructure Scoring:** : Applies the methodology to compute segment-level quality scores.
* **Metrics Calculation:** : Handles contraflow cycling, dual carriageway detection, and spatial proximity analysis.
* **Visualization:** : Generates interactive HTML web maps and exports decision-making data.
