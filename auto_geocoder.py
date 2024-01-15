import geopandas as gpd
import osmnx as ox
from pathlib import Path

in_dir = Path("./project")
data_dir = in_dir / "data"

data = gpd.read_file(data_dir / "adresses.shp")

def get_coords(row):
    try:
        return ox.geocode(row["address"]).to_crs(epsg=4326)
    except Exception as e:
        print(f"Error when geocoding {row['name']}: {e}")
        return None
    
data["address"] = data.apply(get_coords, axis=1)
