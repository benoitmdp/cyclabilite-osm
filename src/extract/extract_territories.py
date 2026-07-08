#code pour extraire les périmètres des territoires qui nous intéressent par la suite

import os
import sys
import subprocess
import geopandas as gpd
import pandas as pd

# 1. Localisation dynamique de l'exécutable osmium
# Sous Conda, il est dans le dossier Library\bin de l'environnement
osmium_exe = os.path.join(sys.prefix, 'Library', 'bin', 'osmium.exe')

# Vérification manuelle
if not os.path.exists(osmium_exe):
    raise FileNotFoundError(f"Impossible de trouver osmium à cet emplacement : {osmium_exe}")

print(f"Osmium localisé avec succès : {osmium_exe}")

# Chemins
try:
    # Si exécuté dans un script .py
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    # Si exécuté dans un Notebook, utilise le dossier de travail courant
    BASE_DIR = os.getcwd()
INPUT_PBF = os.path.join(BASE_DIR, "ile-de-france-internal.osh.pbf")
SNAPSHOT = os.path.join(BASE_DIR, "temp_snapshot.osm.pbf")
EXPORT_OSM = os.path.join(BASE_DIR, "temp_export.osm.pbf")
EXPORT_GEOJSON = os.path.join(BASE_DIR, "temp_export.geojson")

TERRITOIRES_FILE = os.path.join(BASE_DIR, "territoires_mgp.geojson")
COMMUNES_FILE = os.path.join(BASE_DIR, "communes_arrondissements.geojson")

def run_pipeline():
    try:
        # 1. Extraction globale de la zone MGP (Relation 5814660)
        print("Extraction de la relation MGP...")
        subprocess.run([osmium_exe, "time-filter", INPUT_PBF, "2026-06-01T00:00:00Z", "-o", SNAPSHOT], check=True)
        subprocess.run([osmium_exe, "getid", SNAPSHOT, "r5814660", "-r", "-o", EXPORT_OSM, "--overwrite"], check=True)
        subprocess.run([osmium_exe, "export", EXPORT_OSM, "-o", EXPORT_GEOJSON, "--overwrite"], check=True)

        # 2. Chargement via GeoPandas
        gdf = gpd.read_file(EXPORT_GEOJSON)
        
        # FILTRE : Ne garder que les entités qui sont des polygones ou des multipolygones
        # Cela élimine automatiquement toutes les rues, chemins et places (qui sont des LineString)
        from shapely.geometry import Polygon, MultiPolygon
        gdf = gdf[gdf.geometry.type.isin(['Polygon', 'MultiPolygon'])].copy()
               
        # --- A. Extraction des Territoires (T1 à T12) ---
        territoires = gdf[gdf['ref:FR:MGP'].str.contains(r'^T\d+$', na=False)].copy()
        territoires[['name', 'geometry']].to_file(TERRITOIRES_FILE, driver="GeoJSON")
        print(f"✅ {TERRITOIRES_FILE} généré.")

        # Génération du périmètre extérieur (MGP) ---
        print("Génération du contour global MGP...")
        # Dissout tous les territoires en une seule forme géométrique
        mgp_contour = territoires.unary_union
        
        # On crée un nouveau GeoDataFrame pour ce contour unique
        mgp_gdf = gpd.GeoDataFrame(
            {'name': ['Métropole du Grand Paris']}, 
            geometry=[mgp_contour], 
            crs=territoires.crs
        )
        mgp_gdf.to_file("mgp.geojson", driver="GeoJSON")
        print("✅ mgp.geojson généré (périmètre extérieur).")

        # --- B. Extraction Communes / Arrondissements ---
        # Critères :
        # 1. admin_level 8 (communes) ET boundary=administrative, sauf Paris
        # 2. OU admin_level 9 (arrondissements) ET (Saint-Denis, Pierrefitte, ou 'arrondissement' dans name)
        
        gdf['admin_level'] = pd.to_numeric(gdf['admin_level'], errors='coerce')
        
        cond_commune = (
            (gdf['admin_level'] == 8) & 
            (gdf['boundary'] == 'administrative') & 
            (gdf['name'] != 'Paris')
        )
        
        cond_arr = (
            (gdf['admin_level'] == 9) & 
            (
                gdf['name'].isin(['Saint-Denis', 'Pierrefitte-sur-Seine']) | 
                gdf['name'].str.contains('arrondissement', case=False, na=False)
            )
        )
        
        communes_gdf = gdf[cond_commune | cond_arr].copy()
        communes_gdf[['name', 'geometry']].to_file(COMMUNES_FILE, driver="GeoJSON")
        print(f"✅ {COMMUNES_FILE} généré.")

    except Exception as e:
        print(f"❌ Erreur : {e}")
    finally:
        for f in [SNAPSHOT, EXPORT_OSM, EXPORT_GEOJSON]:
            if os.path.exists(f):
                os.remove(f)

if __name__ == "__main__":
    run_pipeline()
