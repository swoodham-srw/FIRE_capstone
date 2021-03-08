import os
import glob
import gdal
import subprocess
import rasterio
import numpy as np
from xml.dom import minidom

#  first: metadata TOA corrections
sp = os.getcwd()
image_folders = []
xmlfiles = []
for r, d, f in os.walk(sp):  # will walk through our main directory where all the folders of data are stored
    for folder in d:  # all folders of images appended to this empty list
        image_folders.append(os.path.join(r, folder))

i = 0
for x in image_folders:
    image_list = glob.glob(image_folders[i] + '/*.tif')  # creating a list of all the tif files in each folder
    # print(image_list)
    xmlfiles_list = glob.glob(image_folders[i] + '/*.xml')  # creating a list of all xml files in each folder
    # print(xmlfiles_list)
    path = 'C:\\Users\\vgfro\\PycharmProjects\\geomorph\\'  # setting out path to the working directory
    count = 0
    for obj in image_list:  # loop to run through all individual tifs in the list and call the band values
        with rasterio.open(obj) as src:
            band_blue = src.read(1)
            band_green = src.read(2)
            band_red = src.read(3)
            band_nir = src.read(4)
            # bands = src.read()
        # print(bands.shape)
        xmldoc = minidom.parse(xmlfiles_list[count])  # pulling the correct xml file for each tif in the loop
        nodes = xmldoc.getElementsByTagName("ps:bandSpecificMetadata")
        coeffs = {}
        for node in nodes:  # pulling the correction coefficients for each band from the metadata
            bn = node.getElementsByTagName("ps:bandNumber")[0].firstChild.data
            if bn in ['1', '2', '3', '4']:
                num = int(bn)
                value = node.getElementsByTagName("ps:reflectanceCoefficient")[0].firstChild.data
                coeffs[num] = float(value)
        band_blue = band_blue * coeffs[1]  # correcting all the band arrays
        band_green = band_green * coeffs[2]
        band_red = band_red * coeffs[3]
        band_nir = band_nir * coeffs[4]

        bands = np.array([band_blue, band_green, band_red, band_nir])  # recombines the 4 indiv arrays into one 3d array
        # print(bands.shape)

        kwargs = src.meta  # where src is our command of rasterio.open of the image, src is shorthand for source, this
        # accesses the meta data of the original starting image; kwargs is used when we don't know the amount of values
        # or arguments you need to utilize; the name is not relevant but the ** later on is
        kwargs.update(dtype=rasterio.float32,count=4)  # sets the spatial spread of the output image to mirror the input
        # dtype sets the data type of the dataset (float32 is good for science/decimals), count is the number of bands

        # Create the new file:
        name = obj.replace(".tif", "_new.tif")  # renames the new tif file as _new so we know the difference
        with rasterio.open(name, "w", **kwargs) as dst:  # new file name, w = writing mode,
            dst.write(bands.astype(rasterio.float32))  # defines type of file we are saving our 3d array as
        count = count + 1

    i = i + 1


# Mosaicing Chunk:
folders = []  # empty list of folders
sp0 = os.getcwd()  # set variable as the directory where the image folders are; may need to set at beginning
for r, d, f in os.walk(sp0):  # this walks through a directory; r = string path to directory, d = list of names
    # of folders in r, f = list of names of files in r
    for folder in d:  # this will collect all the folders of images in the directory and put into the empty list
        folders.append(os.path.join(r,folder))

i = 0  # this next loop will go through each folder and apply the gdal_merge command to mosaic all the corrected tifs
for x in folders:
    files_to_mosaic = glob.glob(folders[i] + '/*_new.tif')  # makes a list of the corrected tif filepaths in the folder
    files_string = " ".join(files_to_mosaic)  # takes all the file paths and joins them into a single string
    command = "python " + sp0 + "\gdal_merge.py -o " + folders[i][-8:] + ".tif" + " -of gtiff " + files_string
    # all combined to form a single command to pass to gdal to merge; starts w/ python + source path, then doing
    # the merge and creating an output ( -o) of the mosaic file with the date ([-8:]) in a geotiff, with the input
    # being the string of files to mosaic
    print(command)
    i = i + 1
    output = subprocess.getoutput(command)  # passes the created command to python to carry out
    print(output)

#  Beginning Equation chunk:
pre_fire = "name_here.tif"
