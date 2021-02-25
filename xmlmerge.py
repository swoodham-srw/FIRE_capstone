# need a for loop to run through all image files and do te corrections/resave
import rasterio
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
band_blue = band_blue * coeffs[1]  # bands[0,;,;] = bands[0,;,;] * coeffs[1]
band_green = band_green * coeffs[2]
band_red = band_red * coeffs[3]
band_nir = band_nir * coeffs[4]

bands = np.array([band_blue,band_green,band_red,band_nir])  # recombines ahte 4 inidiv arrays into one 3d array
# print(bands.shape)

kwargs = src.meta  # where src is our command of rasterio.open of the image, src is shorthand for source, this is
# accessing the meta data of the original starting image; kwargs is used when we don't know the amount of values
# or arguments you need to utilize; the name is not relevant but the ** later on is
kwargs.update(dtype=rasterio.float32,count=4)  # sets the spatial spread of the output image to mirror the input;
# dtype sets the data type of the dataset (float32 is good for science/decimals), count is the number of bands

# Create the new file
with rasterio.open("test_file2.tif", "w", **kwargs) as dst:  # new file name, w = writing mode,
    dst.write(bands.astype(rasterio.float32))  # defines type of file we are saving our 3d array as


