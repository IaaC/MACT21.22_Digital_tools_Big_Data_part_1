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
london_ward_geojson = '../data/london/london_ward.geojson'
ward = geopandas.read_file(london_ward_geojson)
# read CSV data
london_house_price = '../data/london/land-registry-house-prices-ward.csv'
price = pd.read_csv(london_house_price)

# Create a view using geospatial data
ward.plot(color='None', edgecolor='gray', linewidth=0.8)
plt.show()

price_geo = ward.merge(price, right_on='Code', left_on='GSS_CODE', how='right')
price_geo.plot(color='None', edgecolor='gray', linewidth=0.8)
plt.show()

print('done')
