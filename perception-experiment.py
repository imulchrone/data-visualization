import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from horizonplot import horizonplot

perception = pd.read_csv('PerceptionExperiment.csv')
perception['Error'] = perception['Response'] - perception['TrueValue']

# print(perception.head())

# print(perception['Test'].unique())
fig, ax = plt.subplots(1,1, figsize=(10,7))

for test in perception['Test'].unique():
    error = perception['Error'].loc[perception['Test']==test]
    ax.plot(range(len(error)),error.rolling(window=10).mean(),label=test)
    # smoothed = sm.nonparametric.lowess(range(len(error)),error,frac=0.2)
    # plt.plot(smoothed[:,0],smoothed[:,1],label=test)


plt.xlabel('n')
plt.ylabel('Error (moving average, window=5)')
plt.title('Test Perception Error')
plt.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0)
plt.tight_layout()
plt.show()
# print(perception['Error'].loc[perception['Test']=='Slope'])
