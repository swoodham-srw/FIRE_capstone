import rasterio
import os
import numpy as np
from xml.dom import minidom
os.getcwd()

path = r'/20170803'
os.chdir(path)  # playing with this to test outside the for loop that the rasterio.open worked (which it did)
image_file = "20170803/20170803_181207_0f25_3B_AnalyticMS_clip.tif"
# for filename in os.listdir(path):
#     if filename.endswith(".tif"):
#         # print(filename)
#         with rasterio.open(filename) as src:
#             band_blue = src.read(1)
        # with rasterio.open(filename) as src:
        #     band_green = src.read(2)
        # with rasterio.open(filename) as src:
        #     band_red = src.read(3)
        # with rasterio.open(filename) as src:
        #     band_nir = src.read(4)

        # name = str(filename)
        # newname = name.replace('clip.tif','metadata_clip.xml')
        # print(newname)
        # xmldoc = minidom.parse(newname)
        # nodes = xmldoc.getElementsByTagName("ps:bandSpecificMetadata")
        # coeffs = {}
        # for node in nodes:
        #     bn = node.getElementsByTagName("ps:bandNumber")[0].firstChild.data
        #     if bn in ['1', '2', '3', '4']:
        #         i = int(bn)
        #         value = node.getElementsByTagName("ps:reflectanceCoefficient")[0].firstChild.data
        #         coeffs[i] = float(value)
        # band_blue = band_blue * coeffs[1]
        # band_green = band_green * coeffs[2]
        # band_red = band_red * coeffs[3]
        # band_nir = band_nir * coeffs[4]
        # bands = np.array([band_blue, band_green, band_red, band_nir])
        # kwargs = src.meta
        # kwargs.update(dtype=rasterio.float32, count=4)
        # with rasterio.open(str(filename) + "_2.tif", "w", **kwargs) as dst:
        #     dst.write(bands.astype(rasterio.float32))
    # else:
    #     continue
