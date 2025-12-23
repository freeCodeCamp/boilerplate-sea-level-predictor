import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # 1. Read data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Line of best fit (all data)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_all = np.arange(df["Year"].min(), 2051)
    y_all = res_all.intercept + res_all.slope * x_all
    plt.plot(x_all, y_all, "r")

    # 4. Line of best fit (year 2000 onwards)
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(
        df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"]
    )
    x_2000 = np.arange(2000, 2051)
    y_2000 = res_2000.intercept + res_2000.slope * x_2000
    plt.plot(x_2000, y_2000, "green")

    # 5. Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # 6. Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()
