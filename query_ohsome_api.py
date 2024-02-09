#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Queries filtered data from OSM for an aoi"""


import sys
import osmnx as ox
from pathlib import Path
import pandas as pd
import geopandas as gpd
from ohsome import OhsomeClient


CLIENT = OhsomeClient()

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Change stuff here
aoi_list = ["Greece", "Turkey"]

filter = "amenity=refugee_site or social_facility:for=migrant or social_facility:for=refugee or social_facility:for=displaced"
time = "2016-01-01/2023-08-01/P1W"


# Functions
def query_aoi(aoi: str):
    """Queries the bounding polygon of the area of interest (aoi) from OSM"""
    bpolys = ox.geocode_to_gdf(aoi)

    return bpolys


def query_data(bpolys: gpd.GeoDataFrame, filter: str, time: str):
    """Queries the data from OSM"""
    try:
        response_count = CLIENT.elements.count.post(
        bpolys = bpolys,
        time = time,
        filter = filter
    )
        df = response_count.as_dataframe()  

        response_geoms = CLIENT.elements.geometry.post(
        bpolys = bpolys,
        time = time,
        filter = filter,
        properties = "tags"
    )
        gdf = response_geoms.as_dataframe()
    except Exception as err:
        print(f"Could not send request to ohsome API: {err}")
        sys.exit(1)

    return df, gdf


def write_data(data_dir: Path, aoi: str, df: pd.DataFrame, gdf: gpd.GeoDataFrame):
    try:
        df.to_csv(data_dir / f"{aoi}.csv")
        gdf.to_file(data_dir / f"{aoi}.geojson", driver="GeoJSON")
    except Exception as err:
        print(f"Could not write data to file: {err}")
        sys.exit(1)


# Start of the program
if __name__ == "__main__":

    for aoi in aoi_list:
        print(f"Querying boundaries for {aoi}...")
        bpolys = query_aoi(aoi)

        print(f"Querying data for {aoi}...")
        df, gdf = query_data(bpolys, filter, time)

        print(f"Writing data for {aoi}...")
        write_data(data_dir, aoi, df, gdf)
        
    print("Done!")