import os
import sys
import shutil

import pickle


newcat = 1
output_path = './catalogue_ext.p'
fou = open(output_path, 'wb')
pickle.dump(newcat, fou)
fou.close()

import openquake.sub.pickle_catalogue as pick_cat

catalog = "./../data/catalogue/Leyte_ISCGEMv10_200km.csv"
pick_cat.main(catalog)

source = "catalogue_ext.p"
destination = "../data/catalogue/wpg_Leyte_ISCGEMv10_200km.p"

shutil.move(source, destination)

if os.path.exists("catalogue_ori.p"):
    os.remove("catalogue_ori.p")



import openquake.sub.create_multiple_cross_sections as cmcs

config_fname = './../ini/create_profiles.txt'

cmcs.main(config_fname=config_fname)

source = "cs_traces.cs"
destination = "../model/cs_traces.txt"

# Ensure the destination directory exists
os.makedirs(os.path.dirname(destination), exist_ok=True)

# Move the file
shutil.move(source, destination)



# # This method doesn't work since it depends on basemap 
# !python $path/plotting/plot_multiple_cross_sections_map.py ./../ini/create_profiles.txt ./../model/cs_traces.txt\

config_file = "./../ini/create_profiles.txt"
cs_file = "./../model/cs_traces.txt"

import openquake.sub.plotting.plot_multiple_cross_sections_map as pmcs_map

pmcs_map.plot(config_file, cs_file)