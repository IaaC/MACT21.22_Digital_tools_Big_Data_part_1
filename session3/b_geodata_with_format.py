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

# Merging the two dataframes, starting from the geodataframe
price_geo = ward.merge(price, right_on='Code', left_on='GSS_CODE', how='right')

for period in price_geo['Year'].unique():
    print('Generating map for period: ' + period)
    price_period = price_geo[price_geo['Year'] == period]
    price_period_mean = price_period[price_period['Measure'] == 'Mean']
    price_period_mean.plot(column='Value', scheme='quantiles', cmap='OrRd', edgecolor='k', legend=True)
    plt.title(period)
    plt.axis('off')
    plt.show()
    # plt.savefig('/maps/map ' + period + '.png')

print('done')

#
fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20, 16))
ax1 = geodataframe.plot(ax=ax1, column='obs', legend=True)
ax2 = geodataframe.plot(ax=ax2, column='pred', legend=True)