#importing modules
import rasterio
import matplotlib.pyplot as plt
import retrying
import requests
import os
import time


#opening tif file
image_file = plt.imread("test_code.tif")
plt.imshow(image_file, cmap='Blues')
plt.show()

#some calcul
#save calc in file
#Put file in directory
#loop directory

directory = "/Users/stonewoodham/Documents/PycharmProjects/capstone/FIRE_capstone"
for filename in os.listdir(directory):
    if filename.endswith(".tif"):
        image_file = plt.imread(filename)
        plt.imshow(image_file, cmap='Blues')
        plt.show()
        time.sleep(1)
        continue
    else:
        continue

#after calcul
#save calc in file
#put file in directory
#repeat loop for after

#new calcul = delta NDVI
#plot delta NDVI 
#save new file as delta NDVI
