
#* Elaborate by lmlimasd
#* Version 0.4
#* Date: 2022-06-14
#* function for Notebook Jupyter and Notebook Jupyter extension of Visual Study Code 
#* see the requirements.txt for more details about the libreries version

#dataframe libraries
import pandas as pd
import numpy as np

#plot libraries
import seaborn as sns
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.pyplot as plt

#* Function by plot bar distribution of data by column

def plot_distribution_clm(data_in  #dataframe 
                         ,clm_name #column of dataframe
                         ,order_A_Z  = False #parameter for sort the table by unique values names
                         ,notplot = list() #list with the name of the unique values that you dont want to plot
                         ,dif_colors = False #parameter for different the min and max values by colour
                         ,point = 10 #parameter for indicate the number of column to visualize
                         ,porcentage = False # parametert for normalise the count of unique value
                         ,pst = 'v' #parameter for indicate if plot the graphic in vertical position (h) or horizontal position (h)
                         ):

    longitud_data = data_in.shape[0]

    tmp_dt = pd.DataFrame()

    tmp_dt = data_in[clm_name].copy(deep=True).dropna().value_counts().reset_index()
    tmp_dt.rename(columns = {clm_name:'Count','index':clm_name}, inplace=True)
    tmp_dt['(%) of total data'] = round((tmp_dt['Count']*100)/longitud_data,2)

    #delete the bars without interest
    for elem in notplot:
        if elem in set(tmp_dt[clm_name]):
            tmp_dt = tmp_dt[tmp_dt[clm_name] != elem]
  
    #Plot values sort by column of interest
    if order_A_Z  == True:
        tmp_dt = tmp_dt.sort_values(clm_name)

    fig, ax=plt.subplots(1,1, figsize=(8,8))
    plt.suptitle('Distribution of data by column ' + str(clm_name),fontsize=16)
    sns.set_color_codes("muted")

    tmp_dt = tmp_dt.head(point)
    if porcentage == False:
        #* PLOT BY MAGNITUDE

        if pst == "v":
            axe_x = clm_name
            axe_y = 'Count'
            axe_line = 'y'
        else:
            axe_x = 'Count' 
            axe_y = clm_name
            axe_line = 'x'

        ax = sns.barplot( x = axe_x, y = axe_y, data = tmp_dt, label="distribucion", color = '#2258B6')#, ax=ax[0])
        ax.grid(b =True, which='major', color='black', linewidth = 0.3, axis= axe_line)
        # ax[0].bar_label(ax[0].containers[0]) #add label with value of bar in the graphic # * dont work in VSC
    else:
        #* PLOT BY PERCENTAGE
        
        if pst == "v":
            axe_x = clm_name
            axe_y = '(%) of total data'
            axe_line = 'y'
        else:
            axe_x = '(%) of total data' 
            axe_y = clm_name
            axe_line = 'x'

        ax = sns.barplot( x = axe_x, y = axe_y, data = tmp_dt, label="distribucion", color = '#2258B6')#, ax=ax[0])
        ax.grid(b =True, which='major', color='black', linewidth = 0.3, axis= axe_line)
        # ax[0].bar_label(ax[0].containers[0]) #add label with value of bar in the graphic # * dont work in VSC

    #scale colors
    if dif_colors == True:
        palette_colors = list()
        for row_cat, bar  in zip(tmp_dt['Count'], ax.patches):
            if row_cat == tmp_dt['Count'].max():
                bar.set_color('#7EC5CE') #red pastel
            elif row_cat == tmp_dt['Count'].min():
                bar.set_color('#DAB6F1') #green paster
            # else:
            #     bar.set_color('') #blue pastel

    return tmp_dt