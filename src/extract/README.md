# 🏗 Data Extraction Module

## 🇫🇷 Français

Ce module permet d'extraire les contours administratifs et le réseau viaire de la **Métropole du Grand Paris** à partir des données historiques d'OpenStreetMap (Geofabrik).

### Fonctionnement
Le script `extract_territories.py` réalise les étapes suivantes :
1. **Extraction par ID** : Utilise `osmium` pour isoler la relation MGP (5814660) depuis un fichier `.osh.pbf`.
2. **Filtrage géométrique** : Nettoie les données pour ne conserver que les surfaces (polygones/multipolygones).
3. **Traitement spatial** :
   - Génère le contour global de la MGP via une union géométrique.
   - Filtre les communes (`admin_level=8`) et les arrondissements spécifiques (`admin_level=9`) incluant une gestion particulière pour Saint-Denis et Pierrefitte-sur-Seine.
4. **Export** : Sauvegarde les résultats au format `GeoJSON` pour les analyses ultérieures.

### Prérequis
- `osmium-tool` installé sur votre système.
- Environnement Python tel que proposé dans environment.yml


### 📥 Préparation des données
Pour exécuter le pipeline d'extraction, vous devez fournir les données sources :

1. **Téléchargement** : Récupérez l'extrait historique OSM (ex: `ile-de-france-internal.osh.pbf`) sur le serveur de [Geofabrik](https://download.geofabrik.de/).
2. **Emplacement** : Placez ce fichier dans le dossier `data/raw/` à la racine du projet.
3. **Configuration** : Vérifiez que le nom du fichier correspond à celui défini dans votre script (ou mettez à jour la variable `INPUT_PBF` dans `extract_territories.py`).

### 🚀 Lancement de l'extraction
Une fois l'environnement activé, lancez le script d'extraction des territoires :

```bash
python src/extract/extract_territories.py
```

---

## 🇬🇧 English

This module extracts administrative boundaries and road network data for the **Greater Paris Metropolis (Métropole du Grand Paris)** from historical OpenStreetMap (Geofabrik) datasets.

### Workflow
The `extract_territories.py` 

---

## 🇬🇧 English

This module extracts administrative boundaries and road network data for the **Greater Paris Metropolis (Métropole du Grand Paris)** from historical OpenStreetMap (Geofabrik) datasets.

### Workflow
The `extract_territories.py` script performs the following steps:
1. **ID Extraction**: Uses `osmium` to isolate the MGP relation (5814660) from a raw `.osh.pbf` file.
2. **Geometric Filtering**: Cleans the data to keep only surface features (polygons/multipolygons).
3. **Spatial Processing**:
   - Generates the global MGP boundary via geometric union.
   - Filters communes (`admin_level=8`) and specific arrondissements (`admin_level=9`), including specific fixes for Saint-Denis and Pierrefitte-sur-Seine.
4. **Export**: Saves results in `GeoJSON` format for subsequent analysis.

### Prerequisites
- `osmium-tool` installed on your system.
- Python environment with `geopandas` and `shapely`.

### 📥 Data Preparation
To run the extraction pipeline, you need to provide the raw OSM data:

1. **Download**: Obtain the historical OSM extract (e.g., `ile-de-france-internal.osh.pbf`) from the [Geofabrik download server](https://download.geofabrik.de/).
2. **Placement**: Place the file in the `data/raw/` directory at the root of the project.
3. **Configuration**: Ensure the file name matches the one defined in your script (or update the `INPUT_PBF` variable in `extract_territories.py`).

---

## 🚀 Usage

```bash
python src/extract/extract_territories.py
