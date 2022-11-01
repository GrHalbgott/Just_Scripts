#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A DEM Difference Calculation"""

# Call with:
# $ python src/diff_calc.py


import sys
import numpy as np
import matplotlib.pyplot as plt
import rasterio
import rasterio.features
import rasterio.warp
import time


def main():
    """
    Reads raster files as NumPy-arrays, calculates the difference between them and plots them into a plot
    :return: figure
    """

    starttime = time.time()

    # Handling the input files
    # ----------
    in_dem_newer = './data/newer.tif'
    in_dem_older = './data/older.tif'


    def read_raster_rasterio(in_dem):
        """
        Read the input files as Numpy arrays and preprocess them
        param in_dem: path to input file (string)
        output: returns a Numpy array (Null values are np.nan)
        """
        try:
            dataset = rasterio.open(in_dem)
        except Exception as err:
            print('Unable to open the file because of: ', str(err), '\nPlease check your input file.')
            sys.exit()
        # Read the dataset's valid data mask as a ndarray.
        mask = dataset.dataset_mask()
        dataset.indexes
        print("...reading the raster %s..." % (in_dem))
        band = dataset.read(1)
        print("...reading worked.")
        # data_dem = np.where(band == band.GetNoDataValue(), np.nan, band)
        # Extract feature shapes and values from the array.
        for geom, val in rasterio.features.shapes(mask, transform=dataset.transform):
            # Transform shapes from the dataset's own coordinate reference system to CRS84 (EPSG:4326).
            geom = rasterio.warp.transform_geom(dataset.crs, 'EPSG:4326', geom, precision=6)
        return band, geom
        

    # Calculation of elevation difference
    print("Deriving difference...")
    try:
        new, new_geom = read_raster_rasterio(in_dem_newer)
        old, old_geom = read_raster_rasterio(in_dem_older)
        dem_diff = new - old 
    except Exception as err:
        print("Error occured when calculating the difference: " + str(err))
        sys.exit()

    stoptime = time.time()

    # Print out the information to user
    print ("Finished computing the difference of the DEMs with inputs %s & %s. \n The script took %.2f seconds to run." % (in_dem_newer, in_dem_older, stoptime-starttime))

    # Print statistics of the difference calculation 
    print("--- STATISTICS OF DIFFERENCES ---")
    print("Minimum difference: %.2f m" % np.nanmin(dem_diff))
    print("Maximum difference: %.2f m" % np.nanmax(dem_diff))
    print("Mean difference: %.2f m" % np.nanmean(dem_diff))
    print("Median difference: %.2f m" % np.nanmedian(dem_diff))
    print("Std.dev. of difference: %.2f m" % np.nanstd(dem_diff))
    print("---------------------------")

    # Plotting the nDSM with correct coordinates
    # fig, ax = plt.subplots()
    # # this is in data coordinates
    # ax.set_xlim(0, 2000)
    # ax.set_ylim(0, 2000)
    # point = (1000, 1000)
    # # this takes us from the data coordinates to the display coordinates and to axes coordinates
    # trans = (ax.transData + ax.transAxes.inverted()).transform(point)
    # ax.plot(*trans, 'o', transform=ax.transAxes)
    # fig.show()

    plt.figure(figsize=(20,20))
    plt.imshow(dem_diff, cmap='seismic_r', vmin=-25, vmax=25)
    plt.title("Difference of DEMs in a glacial scence in Norway between 2009 and 2017")
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    # Plot a colorbar with the same height as the plot
    im_ratio = dem_diff.shape[0]/dem_diff.shape[1]
    plt.colorbar(fraction=0.04625*im_ratio)
    plt.show()

if __name__ == "__main__":
    main()
