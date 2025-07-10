import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import geopandas as gpd
import geoplot as gplt

food = pd.read_csv('FoodSrvcByCounty.txt', sep = '\t')
# print(food.head())

states = food.copy()
# print(states['State'].head())

states = states.loc[states['State'].isna()]
states = states[states['County'] != 'UNITED STATES']
# print(states.head())

# geoplot.cartogram(states['County'],)

contiguous_usa = gpd.read_file(gplt.datasets.get_path('contiguous_usa'))
gplt.polyplot(contiguous_usa)