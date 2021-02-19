# i image the base code will basically have to have a massive for loop after the mosaicing that has
# smaller loops under it: one for reading in the band values for each mosaicied image, one that averages the
# 3 visual bands, and then one that then subtracts the post-fre values from the pre-fire values. I would say
# for now we should work on it for having one single post-fire each week and one single pre-fire to make it easier


import numpy as np
import subprocess
import os

prefire = "__name__.tif"
# all the stuff in base_code.py to read in the band values and make corrections
postimages = [] # creating an empty list for all the mosaiced post fire tif files
# should still have variable 'sp0' saved as directory from earlier
for r, d, f in os.walk(sp0):# this walks through a directory; r = string path to directory, d = list of names
    # of folders in r, f = list of names of files in r
    for image in f: #this will collect all the postfire images in the directory and put into the empty list
        postimages.append(os.path.join(r,image))

i = 0
for x in postimages: # creating a loop to repeat through all of the post fire images




# allow division by zero, not sure if we need but does not hurt
# np.seterr(divide="ignore", invalid="ignore")

# base equations
# NIRmap = band_nir_post.astype(float) - band_nir_pre.astype(float)

# visual: ((band_blue_post.astype(float) + band_green_post.astype(float) + band_red_post.astype(float))/3) -
# ((band_blue_pre.astype(float) + band_green_pre.astype(float) + band_red_pre.astype(float))/3)