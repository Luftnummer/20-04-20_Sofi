# -*- coding: utf-8 -*-
"""
Credits
Johannes Allgaier, M. Sc. Wirtschaftswissenschaften
Research Associate
Health informatics

Institute of Clinical Epidemiology and Biometry (ICE-B
*****************************************************

Visualize data

"""
# location
# cd C:\Users\Johannes Allgaier\Documents\20-04-20_Sofi

# import required packages
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# read in the df
df = pd.read_excel('data/dataset.xlsx')



# create a pairplot of the data using seaborn 
sns.set(style = 'darkgrid',
        context = 'paper', 
        color_codes = True)

ax = plt.subplot()
ax = sns.pairplot(df.drop(index = 50),
                  plot_kws= {'s':20, 
                             'linewidth':1,
                             'color' : '#444444',
                             'alpha' : .5,
                             'edgecolor': None},
                  diag_kind='kde',
                  diag_kws= {'shade' : True})

ax.set_title('Pairplot of dependant and independant variables')
plt.show()

# scatterplots
plt.style.use('seaborn')

variables = df.loc[:, df.columns != 'DPR']
target = df['DPR']

for var in variables.columns:
    plt.scatter(variables[f'{var}'],target,
                edgecolor = 'black',
                linewidth = 1, # of the edge
                alpha = .75) # size of the scatter plots
    
    plt.xscale('log')
    plt.yscale('log')
    
    plt.title('Scatterplot for log data')
    plt.xlabel(f'{var}')
    plt.ylabel('DPR')
    
    plt.tight_layout()
    
    plt.show()
    
    plt.savefig(f'plots/scatter_{var}_DPR_seaborn.svg')
    
    plt.clf()


