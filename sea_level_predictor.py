import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    # Importar datos
    df = pd.read_csv('epa-sea-level.csv')

    # Crear diagrama de dispersión
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Primera línea de mejor encaje: datos desde el inicio
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Extender la línea hasta el año 2050
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    ax.plot(
        years_extended,
        res.intercept + res.slope * years_extended,
        'r',
        label='Best fit line (1880-2013)'
    )

    # Segunda línea de mejor encaje: desde el año 2000
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(
        years_recent,
        res_recent.intercept + res_recent.slope * years_recent,
        'green',
        label='Best fit line (2000-2013)'
    )

    # Etiquetas y título
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()

    # Guardar y devolver la imagen
    plt.savefig('sea_level_plot.png')
    return plt.gca()
