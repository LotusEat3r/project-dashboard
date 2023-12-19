import os
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns

st.title('Deaths in the United States from Pneumonia and Influenza')
deaths = pd.read_csv('./deaths.csv')

decades_natl = deaths[(deaths['geo_level']  == 'National') & (deaths['age'] == 'All')].groupby('year').sum(numeric_only = True).reset_index()

st.markdown("One of the first things we can see is the number of national deaths due to influenza and pneumonia for the United States between the years 2010 and 2018.")
disease = st.selectbox("Select One:", ["Pneumonia", "Influenza"])

if disease == "Pneumonia":
    dcd_pneu_plt = sns.barplot(decades_natl, x = 'year', y = 'pneu_deaths', color = 'skyblue')
    dcd_pneu_plt.set(xlabel = "Year", ylabel = "Deaths From Pneumonia", title = "Deaths due to Pneumonia by Year")
    st.pyplot(dcd_pneu_plt.figure)
if disease == "Influenza":
    dcd_flu_plt = sns.barplot(decades_natl, x = 'year', y = 'flu_deaths', color = 'firebrick')
    dcd_flu_plt.set(xlabel = "Year", ylabel = "Deaths From Influenza", title = "Deaths due to Influenza by Year")
    st.pyplot(dcd_flu_plt.figure)

st.markdown("We can also see trends across a single year for either pneumonia or influenza")
year = st.selectbox("Select a Year:", [2010,2011,2012,2013,2014,2015,2016,2017,2018])
dis = st.selectbox("Select One:", ["Pneumonia", "Influenza"])

graph_year = deaths[(deaths['year'] == year) & (deaths['geo_level'] == "National") & (deaths['age'] == "All")]
if dis == "Pneumonia":
    year_plt = sns.lineplot(graph_year, x = 'week', y = 'pneu_deaths', color = 'skyblue')
if dis == "Influenza":
    year_plt = sns.lineplot(graph_year, x = 'week', y = 'flu_deaths', color = 'firebrick')


#plot = sns.scatterplot(graph_penguins, x = 'bill_depth_mm', y = 'bill_length_mm')
#plot.set(title = f"Bill Length vs. Bill Depth for {species} Penguins from {island} Island", xlabel = "Bill Depth (mm)", ylabel = "Bill Length (mm)")


#st.pyplot(plot.figure)