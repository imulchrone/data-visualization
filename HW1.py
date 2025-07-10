import pandas as pd
import matplotlib.pyplot as plt

cellPlans = [["ATT", "Sprint", "Verizon", "ATT", "Sprint", 
"Verizon", "ATT", "Sprint", "Verizon", "ATT", 
"Verizon", "Sprint", "Verizon", "ATT", 
"Verizon", "Sprint", "ATT", "ATT", "Sprint"], 
[1, 1, 2, 3, 3, 4, 6, 6, 8, 10, 12, 12, 16, 16, 
24, 24, 25, 30, 40], 
[30, 20, 35, 40, 30, 50, 60, 45, 70, 80, 80, 60, 
90, 90, 110, 80, 110, 135, 100]]
names = ["Company", "DataGB", "Price"]

celldata = pd.DataFrame({
                    names[0] : cellPlans[0],
                    names[1] : cellPlans[1],
                    names[2] : cellPlans[2]
})

att = celldata.loc[celldata['Company']=='ATT']
# print(att)
sprint = celldata.loc[celldata['Company']=='Sprint']
# print(sprint)
verizon = celldata.loc[celldata['Company']=='Verizon']
# print(verizon)

#Price vs Data Line Graph
plt.plot(att['DataGB'],att['Price'], label='ATT', color='blue', marker='o')
plt.plot(sprint['DataGB'],sprint['Price'], label='Sprint', color='yellow', marker='o')
plt.plot(verizon['DataGB'],verizon['Price'], label='Verizon', color='red', marker='o')
plt.xlabel('Data GB per Month')
plt.ylabel('Price')
plt.title('Cell Carriers Price vs Data Allowed')
plt.legend()
plt.grid()
plt.show()

#Carrier plan bar charts
fig, axes = plt.subplots(1,3, figsize = (7,4))
w=0.9
#Sprint
axes[0].bar(range(sprint['DataGB'].shape[0]),sprint['Price'], color='yellow', edgecolor = 'black', width = w)
axes[0].set_title('Sprint')
axes[0].set_ylabel("Price")
axes[0].set_xticks(range(sprint['DataGB'].shape[0]))
axes[0].set_xticklabels(sprint['DataGB'])

#Verizon
axes[1].bar(range(verizon['DataGB'].shape[0]),verizon['Price'], color='red', edgecolor = 'black', width = w)
axes[1].set_title('Verizon')
axes[1].set_xticks(range(verizon['DataGB'].shape[0]))
axes[1].set_xticklabels(verizon['DataGB'])

#ATT
axes[2].bar(range(att['DataGB'].shape[0]),att['Price'], color='blue', edgecolor = 'black', width = w)
axes[2].set_title('AT&T')
axes[2].set_xticks(range(att['DataGB'].shape[0]))
axes[2].set_xticklabels(att['DataGB'])

plt.setp(axes, yticks = range(0,141,10))
plt.tight_layout()
fig.suptitle('Cell Carrier Plans Prices')
fig.supxlabel('Data GB per Month')
plt.show()

