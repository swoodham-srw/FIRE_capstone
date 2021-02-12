# start by installing package "gdal" in the terminal
import os
import glob
import gdal
import subprocess

folders = [] #empty list of folders
sp0 = os.getcwd() # set variable as the directory where the image folders are
for r, d, f in os.walk(sp0): # this walks through a directory; r = string path to directory, d = list of names
    # of folders in r, f = list of names of files in r
    for folder in d: #this will collect all the folders of images in the directory and put into the empty list
        folders.append(os.path.join(r,folder))

i = 0 #this next loop will go through each folder and apply the gdal_merge command
for x in folders:
    files_to_mosaic = glob.glob(folders[i] + '/*.tif') # creates a list of filepaths in the folder ending in .tif
    files_string = " ".join(files_to_mosaic) # takes all the file paths and joins them into a single string
    command = "python " + sp0 + "\gdal_merge.py -o " + folders[i][-8:] + ".tif" + " -of gtiff " + files_string
    # all combined to form a single command to pass to gdal to merge; starts w/ python + source path, then doing
    # the merge and creating an output ( -o) of the mosaiced file with the date ([-8:]) in a geotiff, with the input
    # being the string of files to mosaic
    print(command)
    i = i + 1
    output = subprocess.getoutput(command) # passes the created command to python to carry out
    print(output)