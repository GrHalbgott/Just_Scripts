echo Enter the region of interest (roi): 
set /p roi=

echo Enter the EPSG number of your roi: 
set /p crs=

ogr2ogr -f "ESRI Shapefile" ./%roi%.shp -lco ENCODING=UTF-8 -t_srs EPSG:%crs% -sql "SELECT * FROM gadm36_DEU_3 WHERE NAME_3='%roi%'" ./gadm36_DEU.gpkg
