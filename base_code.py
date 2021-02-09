# importing modules
import rasterio
import matplotlib.pyplot as plt
import retrying
import requests
import os
import numpy as np

# for now: ID's the TIFF file being analyzed; may need to be turned into a for loop later to go
# through all the files in a folder or something
image_file = "test_file.tif"

# load needed bands in
with rasterio.open(image_file) as src:
    band_blue = src.read(1)
with rasterio.open(image_file) as src:
    band_green = src.read(2)
with rasterio.open(image_file) as src:
    band_red = src.read(3)
with rasterio.open(image_file) as src:
    band_nir = src.read(4)

# these just verified that the band data was able to be read/opened
# plt.imshow(band_red, cmap='pink')
# plt.show()

# this was to verify having all 4 bands together in the main file
# with rasterio.open(image_file) as src:
#    bands = src.read()
# print(bands.shape)

# incorporating the metadata: Normalizing to top of atmosphere reflectance
from xml.dom import minidom
xmldoc = minidom.parse("test_meta.xml")
nodes = xmldoc.getElementsByTagName("ps:bandSpecificMetadata")

coeffs = {}
for node in nodes:
    bn = node.getElementsByTagName("ps:bandNumber")[0].firstChild.data
    if bn in ['1', '2', '3', '4']:
        i = int(bn)
        value = node.getElementsByTagName("ps:reflectanceCoefficient")[0].firstChild.data
        coeffs[i] = float(value)

# multiple band values by TOA coeffs
band_blue = band_blue * coeffs[1]
band_green = band_green * coeffs[2]
band_red = band_red * coeffs[3]
band_nir = band_nir * coeffs[4]

