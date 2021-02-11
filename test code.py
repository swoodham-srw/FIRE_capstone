#importing modules
import rasterio
import matplotlib.pyplot as plt
import retrying
import requests
import os

#opening tif file
image_file = plt.imread("test_code.tif")
plt.imshow(image_file, cmap='Blues')
plt.show()