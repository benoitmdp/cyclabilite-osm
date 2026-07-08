#code pour extraire les périmètres des territoires qui nous intéressent par la suite

import os, sys, subprocess
from datetime import datetime
import geopandas as gpd
import pandas as pd

# -------------------------------------------------------------
# Détection Jupyter
# -------------------------------------------------------------
try:
    from IPython.display import display, clear_output
    import ipywidgets as widgets
    JUPYTER = True
except ImportError:
    JUPYTER = False

# -------------------------------------------------------------
# Configuration
# -------------------------------------------------------------
conda_prefix = sys.prefix
osmium_exe = os.path.join(conda_prefix, "Library", "bin", "osmium.exe")
if not os.path.exists(osmium_exe):
    raise FileNotFoundError(f"osmium.exe introuvable :\n{osmium_exe}")

os.environ["GDAL_DATA"] = os.path.join(conda_prefix, "Library", "share", "gdal")
os.environ["PROJ_DATA"] = os.path.join(conda_prefix, "Library", "share", "proj")

INPUT_PBF = "ile-de-france-internal.osh.pbf"
SNAPSHOT, EXPORT_OSM, EXPORT_GEOJSON = "temp_snapshot.osm.pbf", "temp_export.osm.pbf", "temp_export.geojson"
TERRITOIRES_FILE, COMMUNES_FILE, MGP_FILE = "territoires_mgp.geojson", "communes_arrondissements.geojson", "mgp.geojson"
# L'identifiant de la relation peut être trouvé via le site osm.org, clic droit, "interroger les objets", "Objets englobant" 
MGP_OSM = "r5814660"


# -------------------------------------------------------------
# Utilitaires
# -------------------------------------------------------------
def check_input():
    if not os.path.exists(INPUT_PBF): raise FileNotFoundError(f"Fichier absent : {INPUT_PBF}")

def cleanup():
    for f in (SNAPSHOT, EXPORT_OSM, EXPORT_GEOJSON):
        if os.path.exists(f):
            try: os.remove(f)
            except OSError: pass

def ensure_columns(gdf):
    for col in ["admin_level", "boundary", "name", "ref:FR:MGP"]:
        if col not in gdf.columns: gdf[col] = None
    return gdf

# -------------------------------------------------------------
# Pipeline principal
# -------------------------------------------------------------
def run_pipeline(target_date):
    check_input()
    date_iso = f"{target_date}T00:00:00Z"
    print(f"\n{'='*60}\nExtraction au {target_date}\n{'='*60}")
    try:
        subprocess.run([osmium_exe, "time-filter", INPUT_PBF, date_iso, "-o", SNAPSHOT, "--overwrite"], check=True)
        subprocess.run([osmium_exe, "getid", SNAPSHOT, MGP_OSM, "-r", "-o", EXPORT_OSM, "--overwrite"], check=True)
        subprocess.run([osmium_exe, "export", EXPORT_OSM, "-o", EXPORT_GEOJSON, "--overwrite"], check=True)
        
        gdf = gpd.read_file(EXPORT_GEOJSON)
        if gdf.empty: raise ValueError("Le GeoJSON exporté est vide.")
        if gdf.crs is None: gdf = gdf.set_crs(4326)
        
        gdf = ensure_columns(gdf)
        gdf = gdf[gdf.geometry.geom_type.isin(["Polygon", "MultiPolygon"])].copy()
        gdf["admin_level"] = pd.to_numeric(gdf["admin_level"], errors="coerce")
        
        # Territoires
        territoires = gdf[gdf["ref:FR:MGP"].str.contains(r"^T\d+$", na=False)].copy()
        if territoires.empty: raise ValueError("Aucun territoire MGP trouvé.")
        territoires[["name", "geometry"]].to_file(TERRITOIRES_FILE, driver="GeoJSON")
        print(f"✓ {TERRITOIRES_FILE}")
        
        # Métropole
        mgp = gpd.GeoDataFrame({"name": ["Métropole du Grand Paris"]}, geometry=[territoires.geometry.union_all()], crs=territoires.crs)
        mgp.to_file(MGP_FILE, driver="GeoJSON")
        print(f"✓ {MGP_FILE}")
        
        # Communes
        cond_communes = (gdf["admin_level"] == 8) & (gdf["boundary"] == "administrative") & (gdf["name"] != "Paris")
        is_special = gdf["name"].isin(["Saint-Denis", "Pierrefitte-sur-Seine"])
        is_arr = gdf["name"].str.contains("arrondissement", case=False, na=False)
        communes = gdf[cond_communes | ((gdf["admin_level"] == 9) & (is_special | is_arr))].copy()
        
        if communes.empty: raise ValueError("Aucune commune trouvée.")
        communes[["name", "geometry"]].to_file(COMMUNES_FILE, driver="GeoJSON")
        print(f"✓ {COMMUNES_FILE}\n\nExtraction terminée avec succès.")
        
    except (subprocess.CalledProcessError, Exception) as e:
        print(f"\nErreur :\n{e}")
    finally:
        cleanup()

# -------------------------------------------------------------
# Interface Jupyter / Console
# -------------------------------------------------------------
if JUPYTER:
    date_picker = widgets.DatePicker(description="Date cible :", value=datetime(datetime.now().year, 1, 1).date(), style={"description_width": "initial"}, layout=widgets.Layout(width="250px"))
    launch_button = widgets.Button(description="Lancer l'extraction", icon="play", button_style="success", layout=widgets.Layout(width="220px"))
    output_area = widgets.Output()

    def on_button_clicked(_):
        with output_area:
            clear_output()
            if date_picker.value is None: print("Veuillez sélectionner une date."); return
            run_pipeline(date_picker.value.strftime("%Y-%m-%d"))
    launch_button.on_click(on_button_clicked)
    display(widgets.VBox([widgets.HTML("<h3>📅 Extraction territoires depuis OpenStreetMap</h3>"), date_picker, launch_button, output_area]))

def console_mode():
    default_date = f"{datetime.now().year}-01-01"
    answer = input(f"Date cible (YYYY-MM-DD) [{default_date}] : ").strip() or default_date
    try:
        datetime.strptime(answer, "%Y-%m-%d")
        run_pipeline(answer)
    except ValueError: print("\nFormat invalide. Utilisez YYYY-MM-DD.")

if __name__ == "__main__" and not JUPYTER:
    console_mode()
