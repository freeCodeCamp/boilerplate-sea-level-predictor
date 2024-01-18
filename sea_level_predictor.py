import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
     df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.7, label='Actual Data')


    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], slope * df['Year'] + intercept, color='red', label='Line of Best Fit (1880-2019)')


    # Create second line of best fit
     recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], slope_recent * df['Year'] + intercept_recent, color='green', label='Line of Best Fit (2000-2019)')

    # Extend the lines to predict the sea level rise in 2050
    plt.plot([1880, 2050], [slope * 1880 + intercept, slope * 2050 + intercept], '--', color='red', label='Predicted Rise (1880-2050)')
    plt.plot([2000, 2050], [slope_recent * 2000 + intercept_recent, slope_recent * 2050 + intercept_recent], '--', color='green', label='Predicted Rise (2000-2050)')



    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
