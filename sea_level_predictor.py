# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',float_precision='legacy')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(16,9))
    ax = plt.scatter(data=df, x = 'Year',
                    y = 'CSIRO Adjusted Sea Level')
    
    fit_1 = linregress(x = df.Year, 
                       y = df['CSIRO Adjusted Sea Level'])
    
    timeline = range(1880, 2050)

    # Create first line of best fit
    y1_line = fit_1[0] * timeline + fit_1[1]
    ax = plt.plot(timeline, y1_line, 'r')
    plt.xlim(1850, 2075)


    # Create second line of best fit
    df_2k = df[120:]
    fit_2 = linregress(x = df_2k.Year,
                       y = df_2k['CSIRO Adjusted Sea Level'])
    
    timeline_2k = range(2000, 2050)
    y2_line = fit_2[0] * timeline_2k + fit_2[1]
    ax = plt.plot(timeline_2k, y2_line, 'y')
    #bf_line_2 = slope_2 * timeline + y_int_2
    #plt.plot(timeline, bf_line_2)
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()