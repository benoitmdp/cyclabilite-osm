# 🚲 OSM Cyclability Scoring

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-green)
![OpenStreetMap](https://img.shields.io/badge/data-OpenStreetMap-orange)

*An open-source methodology for assessing bicycle network quality.*

---

## 📸 Overview

![Screenshot](docs/capture.png)

## English


## 🇫🇷 Français

### Présentation
**OSM Cyclability Scoring** est une méthodologie et un ensemble d'outils open source permettant d'évaluer la qualité des infrastructures cyclables à partir des données **OpenStreetMap**. 

Initialement développé pour analyser le réseau de la **Métropole du Grand Paris**, cet outil permet de qualifier finement chaque segment de voirie pour aider à la planification et au suivi du développement du vélo.

### Fonctionnalités principales
- ✅ **Analyse automatisée** des réseaux routiers OSM.
- ✅ **Détection intelligente** des aménagements (pistes, bandes, voies vertes, vélorues).
- ✅ **Analyse avancée** : doubles sens cyclables, chaussées séparées, analyse de proximité spatiale.
- ✅ **Sorties exploitables** : scores par segment, exports GeoParquet, cartes interactives HTML.

### Public visé
Ce projet s'adresse aux collectivités, métropoles, autorités de mobilité, urbanistes, chercheurs et contributeurs OpenStreetMap souhaitant évaluer leur territoire de manière objective.

---

## 🇬🇧 English

### Overview
**OSM Cyclability Scoring** is an open-source methodology and toolkit designed to assess bicycle-friendliness using **OpenStreetMap** data.

Designed and refined for the **Greater Paris Metropolis (Métropole du Grand Paris)**, this project computes cyclability scores for road segments by integrating road hierarchy, dedicated cycling infrastructure, contraflow cycling, and spatial proximity analysis.

### Main Features
- ✅ **Automatic analysis** of OSM road networks.
- ✅ **Infrastructure detection** (tracks, lanes, greenways, cycle streets).
- ✅ **Advanced metrics**: contraflow assessment, dual carriageway detection, spatial proximity.
- ✅ **Actionable outputs**: segment-level scoring, GeoParquet datasets, and interactive web maps.

### Intended Users
The project serves local authorities, metropolitan governments, transport agencies, urban planners, researchers, and OpenStreetMap contributors interested in data-driven cycle network assessment.

---

## 🛠 Workflow

```mermaid
graph TD
    A[OpenStreetMap Data] --> B[GeoParquet Conversion]
    B --> C[Cyclability Scoring Engine]
    C --> D[GeoParquet Exports]
    C --> E[Interactive HTML Maps]
