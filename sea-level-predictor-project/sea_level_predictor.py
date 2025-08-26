import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='1880-2013')

    regress_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope_full = regress_full.slope
    intercept_full = regress_full.intercept
    x_full = np.arange(df['Year'].min(), 2051)
    y_full = x_full * slope_full + intercept_full
    plt.plot(x_full, y_full, color='red', label='1880-2050')
   
    df_2000 = df[df['Year']>= 2000]

    regress_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    slope_2000 = regress_2000.slope
    intercept_2000 = regress_2000.intercept
    x_2000 = np.arange(2000, 2051)
    y_2000 = x_2000 * slope_2000 + intercept_2000

    plt.plot(x_2000, y_2000, color='green', label='2000-2050')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()