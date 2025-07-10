import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

water = pd.read_csv('PortlandWaterLevel2003.csv')
water['Date'] = pd.to_datetime(water['Date'])

june = water.copy()

june = june.loc[june['Date'].dt.month == 6]
june['AvgWL'] = june['WL'].rolling(window=2).mean()
june.loc[june['AvgWL'].isna(),'AvgWL'] = june['WL']

june['Hour'] = june['Time'].str.split(':').str[0]
june['Day'] = june['Date'].dt.day

y_min = june['AvgWL'].min()
y_max = june['AvgWL'].max()

# Add a small buffer to the limits (5% of range)
y_range = y_max - y_min
y_min -= 0.05 * y_range
y_max += 0.05 * y_range

# Round to nice values for ticks
y_min_rounded = np.floor(y_min)
y_max_rounded = np.ceil(y_max)

fig, axes = plt.subplots(6,5, figsize = (9,6))

plt.subplots_adjust(wspace=0.08,top=0.93,bottom=0.1,left=0.075)

fig.suptitle('Portland Hourly Water Levels (June, 2003)')
fig.supxlabel('Hour')
fig.supylabel('Water Level')

c = 0
r = 0

for i in range(1,31):
    axes[r][c].grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
    axes[r][c].set_ylim(y_min, y_max)
    axes[r][c].set_xlim(-0.5, 24.5)
    axes[r][c].text(0.02, 0.95, f"{i}", transform=axes[r][c].transAxes, 
                    fontsize=6, fontweight='bold', va='top')

    axes[r][c].set_yticks([0,1,2])
    if c != 0:
        axes[r][c].set_yticklabels([])

    axes[r][c].set_xticks([0,6,12,18,24])
    if r != 5:
        axes[r][c].set_xticklabels([])
        
    if c >= 4:
        axes[r][c].plot(range(0,24),june['AvgWL'].loc[june['Day']==i])
        c = 0
        r += 1
    else:
        axes[r][c].plot(range(0,24),june['AvgWL'].loc[june['Day']==i])
        c += 1


plt.show()