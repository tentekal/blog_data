import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

file = pd.read_csv('/home/tentakel/Documents/Blog Data/samesmarriage-master/ssm.csv', header=None)
data = pd.DataFrame(file)


years = data.iloc[0,2:]
summed_df = pd.DataFrame(index = ('no_law','stat_ban','con_ban','legal'), columns=years)

# calculate number of states with x legal status of ssm
def number_states(index, string):
    number = (data.iloc[:,index]).str.contains(string).sum()
    return number


for index, year in enumerate(years):
    
    index += 2
    summed_df.loc['no_law' , year] = number_states(index, 'No Law')
    summed_df.loc['stat_ban', year] = number_states(index, 'Statutory Ban')
    summed_df.loc['con_ban', year] = number_states(index, 'Constitutional Ban')
    summed_df.loc['legal', year] = number_states(index, 'Legal')



# calculate percentages, transpose
data_perc = summed_df.divide(summed_df.sum(axis=0), axis=1)
trans = data_perc.transpose()

# hacky fix for passing 'object' type to plt
no_law = np.array(trans['no_law'], dtype=float)
con_ban = np.array(trans['con_ban'], dtype=float)
stat_ban = np.array(trans['stat_ban'], dtype=float)
legal = np.array(trans['legal'], dtype=float)

plt.figure(figsize=(15,15))
plt.stackplot(years, no_law, con_ban, stat_ban, legal, labels=['No Law', 'Statutory Ban', 'Constitutional Ban', 'Legal'])
plt.legend(loc='upper left')
plt.margins = (100,100)
plt.xlim(1995,2015)


plt.xlabel('Years', fontsize = 30)
plt.ylabel('Percentage of States', fontsize = 30)
plt.ylim(0,1)
plt.title('Same Sex Marriage Legal Status', fontsize = 35)
#plt.style.use('muted')
plt.show()

