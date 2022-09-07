echo Enter name of raster with extension:
set /p raster=

echo Enter name of vector with extension:
set /p vector=

echo Enter EPSG of CRS:
set /p crs=

gdalwarp -cutline ./%vector% -crop_to_cutline -t_srs EPSG:%crs% -dstnodata -9999 ./%raster% ./%raster%_clipped.tif
