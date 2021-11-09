# encoding: utf-8

##################################################
# This script summarises text variables by creating wordclouds. It uses a python library that needs to be installed
# in the virtual environment beforehand through anaconda. This exercise aims to show the basic analysis tool
# used for text as well as to test the work environment.
# To install wordcloud see the documentation here https://pypi.org/project/wordcloud/
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2019, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# Libraries
import geopandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# read geospatial data
london_ward_geojson = '../data/london/london_ward_projected.geojson'
ward = geopandas.read_file(london_ward_geojson)

# Select a single ward based on its name
selected_ward_name = 'Bridge'
selected_ward = ward[ward['NAME'] == selected_ward_name]

ward_aoi = selected_ward.buffer(500)

ax = ward["geometry"].boundary.plot()
ward_aoi.plot(ax=ax)
ax.set_title("An example of using Buffer functions")
ward_aoi.plot()
plt.show()
print('Done')




