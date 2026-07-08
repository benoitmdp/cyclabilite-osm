# 🚲 OSM Cyclability Scoring

An open-source methodology for assessing bicycle network quality from OpenStreetMap data.

docs/capture.png

---

## English

### Overview

OSM Cyclability Scoring is an open-source methodology and toolkit for assessing bicycle-friendliness from OpenStreetMap data.

The project computes a cyclability score for each road segment by combining:

- road hierarchy;
- cycling infrastructure (cycle tracks, cycle lanes, greenways and cycle streets);
- traffic direction and contraflow cycling;
- dual carriageway detection;
- spatial proximity analysis between roads and cycling facilities.

The resulting scores can be used for:

- monitoring cycling networks;
- infrastructure planning;
- territorial benchmarking;
- open-data publication;
- interactive web mapping.

---

### Main Features

✅ Automatic analysis of OpenStreetMap road networks

✅ Detection of cycling infrastructure

✅ Contraflow cycling assessment

✅ Dual carriageway detection

✅ Segment-level cyclability scoring

✅ GeoParquet exports

✅ Interactive comparative web maps

---

### Technology Stack

- Python
- GeoPandas
- Shapely
- Pandas
- Folium
- Jupyter Notebooks

---

### Input Data

The methodology is designed to work with OpenStreetMap extracts converted to GeoParquet format.

---

### Output Data

The tool produces:

- cyclability scores for road segments;
- GeoParquet datasets;
- interactive HTML maps for exploration and comparison.

---

### Intended Users

This project is intended for:

- local authorities;
- metropolitan governments;
- transport agencies;
- urban planners;
- researchers;
- OpenStreetMap contributors.

---

### License

This project is distributed under the MIT License.

---

## 🇫🇷 Français

### Présentation

Cyclabilité OSM est une méthodologie et un ensemble d'outils open source permettant d'évaluer les conditions de circulation à vélo à partir des données OpenStreetMap.

Le projet calcule un score de cyclabilité pour chaque segment de voirie en prenant notamment en compte :

- la hiérarchie du réseau routier ;
- les aménagements cyclables (pistes, bandes, voies vertes et vélorues) ;
- les sens de circulation ;
- les doubles sens cyclables ;
- la détection des chaussées séparées ;
- l'analyse spatiale de proximité entre les rues et les aménagements cyclables.

Les scores obtenus peuvent être utilisés pour :

- le suivi des réseaux cyclables ;
- la planification des infrastructures ;
- les comparaisons territoriales ;
- la publication de données ouvertes ;
- la création de cartes interactives.

---

### Fonctionnalités principales

✅ Analyse automatique des données OpenStreetMap

✅ Détection des aménagements cyclables

✅ Évaluation des doubles sens cyclables

✅ Détection des chaussées séparées

✅ Calcul d'un score de cyclabilité par segment

✅ Export GeoParquet

✅ Cartographie web comparative interactive

---

### Technologies utilisées

- Python
- GeoPandas
- Shapely
- Pandas
- Folium
- Jupyter Notebooks

---

### Données d'entrée

La méthode s'appuie sur des données OpenStreetMap converties au format GeoParquet.

---

### Données produites

Le projet génère :

- un score de cyclabilité par segment de voirie ;
- des jeux de données GeoParquet ;
- des cartes HTML interactives permettant l'exploration et la comparaison temporelle des résultats.

---

### Public visé

Ce projet s'adresse notamment :

- aux collectivités territoriales ;
- aux métropoles ;
- aux autorités organisatrices de mobilité ;
- aux urbanistes ;
- aux chercheurs ;
- à la communauté OpenStreetMap.

---

### Licence

Ce projet est distribué sous licence MIT

---

## Example Workflow

```text
OpenStreetMap
      ↓
GeoParquet conversion
      ↓
Cyclability scoring
      ↓
GeoParquet exports
      ↓
Interactive HTML maps
```

---

## Author

Developed by Benoît Chaumeret - Mission vélo - Ville de Paris.

Contributions, suggestions and feedback are welcome.
