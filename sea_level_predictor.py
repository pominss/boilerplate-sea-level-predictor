import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label = "data")

    # Create first line of best fit
    res1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred1 = np.arange(df['Year'].min(),2051,1)
    y_pred1 = res1.intercept + res1.slope * pd.Series(x_pred1)

    plt.plot(x_pred1, y_pred1)
    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]

    res2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred2 = np.arange(2000, 2051, 1)
    y_pred2 = res2.intercept + res2.slope * pd.Series(x_pred2)

    plt.plot(x_pred2, y_pred2)
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()