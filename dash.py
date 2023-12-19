import os
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns

st.title('Deaths in the United States from Pneumonia and Influenza')
deaths = pd.read_csv('./deaths.csv')

decades_natl = deaths[(deaths['geo_level']  == 'National') & (deaths['age'] == 'All')].groupby('year').sum(numeric_only = True).reset_index()

dcd_flu_plt = sns.barplot(decades_natl, x = 'year', y = 'flu_deaths', color = 'firebrick')
dcd_flu_plt.set(xlabel = "Year", ylabel = "Deaths From Influenza", title = "Deaths due to Influenza by Year")

st.pyplot(dcd_flu_plt.figure)

dcd_pneu_plt = sns.barplot(decades_natl, x = 'year', y = 'pneu_deaths', color = 'skyblue')
dcd_pneu_plt.set(xlabel = "Year", ylabel = "Deaths From Pneumonia", title = "Deaths due to Pneumonia by Year")

st.pyplot(dcd_pneu_plt.figure)

#species = st.selectbox("Select a Species", penguins['species'].unique())
#island = st.selectbox("Select an Island", penguins[penguins['species'] == species]['island'].unique())
#graph_penguins = penguins[(penguins['species'] == species) & (penguins['island'] == island)]

#plot = sns.scatterplot(graph_penguins, x = 'bill_depth_mm', y = 'bill_length_mm')
#plot.set(title = f"Bill Length vs. Bill Depth for {species} Penguins from {island} Island", xlabel = "Bill Depth (mm)", ylabel = "Bill Length (mm)")


#st.pyplot(plot.figure)