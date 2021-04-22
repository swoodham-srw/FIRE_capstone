import os
import glob
import gdal
import subprocess
import rasterio
import numpy as np
from xml.dom import minidom

#  first: metadata TOA corrections
sp = os.getcwd()
# image_folders = []
# xmlfiles = []
# for r, d, f in os.walk(sp):  # will walk through our main directory where all the folders of data are stored
#     for folder in d:  # all folders of images appended to this empty list
#         image_folders.append(os.path.join(r, folder))
# print(image_folders)
#
# i = 0
# for x in image_folders:  # runs through each folder of images in a loop
#     image_list = glob.glob(image_folders[i] + '/*.tif')  # creating a list of all the tif files in the folder (full
#     # path name and adding tif file extension)
#     # print(image_list)
#     xmlfiles_list = glob.glob(image_folders[i] + '/*.xml')  # creating a list of all xml files in the folder, full name
#     # and adding the xml file extension
#     # print(xmlfiles_list)
#     path = 'E:\\FIRE_Capstone_Data\\Image_Collection\\Geomorph_Code\\'
#     # 'C:\\Users\\vgfro\\PycharmProjects\\geomorph\\' old  # setting out path to the working directory
#     count = 0
#     for obj in image_list:  # loop to run through all individual tifs in the list and call the band values
#         with rasterio.open(obj) as src:
#             band_blue = src.read(1)
#             band_green = src.read(2)
#             band_red = src.read(3)
#             band_nir = src.read(4)
#             # bands = src.read()
#         # print(bands.shape)
#         xmldoc = minidom.parse(xmlfiles_list[count])  # pulling up the correct xml file for each tif in the loop
#         nodes = xmldoc.getElementsByTagName("ps:bandSpecificMetadata")
#         coeffs = {}
#         for node in nodes:  # pulling the correction coefficients for each band from the metadata
#             bn = node.getElementsByTagName("ps:bandNumber")[0].firstChild.data
#             if bn in ['1', '2', '3', '4']:
#                 num = int(bn)
#                 value = node.getElementsByTagName("ps:reflectanceCoefficient")[0].firstChild.data
#                 coeffs[num] = float(value)
#         band_blue = band_blue * coeffs[1]  # correcting all the band arrays
#         band_green = band_green * coeffs[2]
#         band_red = band_red * coeffs[3]
#         band_nir = band_nir * coeffs[4]
#
#         bands = np.array([band_blue, band_green, band_red, band_nir])  # recombines the 4 indiv arrays into one 3d array
#         # print(bands.shape)
#
#         kwargs = src.meta  # where src is our command of rasterio.open of the image, src is shorthand for source, this
#         # accesses the meta data of the original starting image; kwargs is used when we don't know the amount of values
#         # or arguments you need to utilize; the name is not relevant but the ** later on is
#         kwargs.update(dtype=rasterio.float32,count=4)  # sets the spatial spread of the output image to mirror the input
#         # dtype sets the data type of the dataset (float32 is good for science/decimals), count is the number of bands
#
#         # Create the new file:
#         name = obj.replace(".tif", "_new.tif")  # takes the full name of the corrected original file and renames
#         #  the new tif file as _new so we know the difference
#         with rasterio.open(name, "w", **kwargs) as dst:  # new file name, w = writing mode,
#             dst.write(bands.astype(rasterio.float32))  # defines type of file we are saving our 3d array as
#         count = count + 1
#
#     i = i + 1


# # Mosaicing Chunk:
# folders = []  # empty list of folders
# for r, d, f in os.walk(sp):  # this walks through a directory; r = string path to directory, d = list of names
#     # of folders in r, f = list of names of files in r
#     for folder in d:  # this will collect all the folders of images in the directory and put into the empty list
#         folders.append(os.path.join(r,folder))
# # print(folders)
#
# i = 0  # this next loop will go through each folder and apply the gdal_merge command to mosaic all the corrected tifs
# for x in folders:
#     files_to_mosaic = glob.glob(folders[i] + '/*_new.tif')  # makes a list of all the corrected tif full filepaths in
#     # the folder and adding the tif extension, filters to only include the _new files
#     # print(files_to_mosaic)
#     files_string = " ".join(files_to_mosaic)  # takes all the file paths and joins them into a single string
#     # print(files_string)
#     command = "python " + sp + "\gdal_merge.py -o " + folders[i][-16:] + ".tif" + " -of gtiff " + files_string
#     # combining all tifs to form a single command to pass to gdal to merge; starts w/ python + source path, then
#     # doing the merge and creating an output ( -o) of the mosaic file with 16 characters of the full file name as a tif
#     # with the input being the string of files to mosaic
#     print(command)
#     i = i + 1
#     output = subprocess.getoutput(command)  # passes the created command to python to carry out
#     print(output)
#     # should save the mosaiced tif file to the main directory


#  Beginning Equation chunk:
#  At this point we need to manually rename the prefire mosaic as ending in 'prefire'

# creating an empty list for all the files in the directory folder, tif files, and pre_fire
tif_file_list = []
pre_fire_list = []
new_tif_file_list = []
# Creating my directory variable. This implies that I am using my current working directory to store desired folders
directory = os.getcwd()

# creating tif files list
for tif_file in glob.glob("*.tif"):  # this should look through directory only for all files ending in .tif
    tif_file_list.append(tif_file)
# print(tif_file_list)
# The pre fire file I want is named with "_prefire" at the end. MAY NEED TO EDIT THIS FOR A DATE. Removes it from
#  tif list of all the post fire images
for i in tif_file_list:
    name = str(i)
    if name.endswith("_prefire.tif"):  # ist there a name.startswith?? may need to change
        pre_fire_list.append(name)
        tif_file_list.pop()
    else:
        continue
print(tif_file_list)
print(pre_fire_list)
# sets prefire variable as our one prefire image
pre_fire = pre_fire_list[0]

with rasterio.open(pre_fire) as src:
    pre_band_blue = src.read(1)
    pre_band_green = src.read(2)
    pre_band_red = src.read(3)
    pre_band_nir = src.read(4)

count = 1

for file in tif_file_list:  # this will iterate through all post fire images in the list
    with rasterio.open(file) as src:
        post_band_blue = src.read(1)
        post_band_green = src.read(2)
        post_band_red = src.read(3)
        post_band_nir = src.read(4)

        # Applying equations visual
        pre_fire_average = (pre_band_blue + pre_band_red + pre_band_green) / 3
        post_fire_average = (post_band_blue + post_band_red + post_band_green) / 3
        new_tif_file_visual = post_fire_average - pre_fire_average

        # applying NIR
        new_tif_file_nir = post_band_nir - pre_band_nir

        # saving as new tifs
        kwargs = src.meta
        kwargs.update(dtype=rasterio.float32, count=1)

        variable = "visual_map_" + str(file) + ".tif"  # used to be str(count)
        with rasterio.open(variable, 'w', **kwargs) as dst:
            dst.write_band(1, new_tif_file_visual.astype(rasterio.float32))
            # tifffile.imsave(variable, new_tif_file_visual)

        variable2 = "nir_map_" + str(file) + ".tif"
        with rasterio.open(variable2, 'w', **kwargs) as dst:
            dst.write_band(1, new_tif_file_nir.astype(rasterio.float32))
            # tifffile.imsave(variable2, new_tif_file_nir)

        count = count + 1

