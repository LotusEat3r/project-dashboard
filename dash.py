import os
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns

st.title('Deaths in the United States from Pneumonia and Influenza')
deaths = pd.read_csv('./deaths.csv')

decades_natl = deaths[(deaths['geo_level']  == 'National') & (deaths['age'] == 'All')].groupby('year').sum(numeric_only = True).reset_index()

st.markdown("One of the first things we can see is the number of national deaths due to influenza and pneumonia for the United States between the years 2010 and 2018.")
disease = st.selectbox("Select One (this will affect all plots):", ["Pneumonia", "Influenza"])

if disease == "Pneumonia":
    dcd_pneu_plt = sns.barplot(decades_natl, x = 'year', y = 'pneu_deaths', color = 'skyblue')
    dcd_pneu_plt.set(xlabel = "Year", ylabel = "Deaths From Pneumonia", title = "Deaths due to Pneumonia by Year")
    st.pyplot(dcd_pneu_plt.figure, clear_figure=True)
if disease == "Influenza":
    dcd_flu_plt = sns.barplot(decades_natl, x = 'year', y = 'flu_deaths', color = 'firebrick')
    dcd_flu_plt.set(xlabel = "Year", ylabel = "Deaths From Influenza", title = "Deaths due to Influenza by Year")
    st.pyplot(dcd_flu_plt.figure, clear_figure=True)

st.markdown("We can also see trends across a single year for either pneumonia or influenza.")
year = st.selectbox("Select a Year:", [2010,2011,2012,2013,2014,2015,2016,2017,2018])

graph_year = deaths[(deaths['year'] == year) & (deaths['geo_level'] == "National") & (deaths['age'] == "All")]
if disease == "Pneumonia":
    year_plt = sns.lineplot(graph_year, x = 'week', y = 'pneu_deaths', color = 'skyblue')
    year_plt.set(xlabel = "Week", ylabel = "Deaths From Pneumonia", title = f"Death Due to Pneumonia in {year} by Week")
    st.pyplot(year_plt.figure, clear_figure=True)
if disease == "Influenza":
    year_plt = sns.lineplot(graph_year, x = 'week', y = 'flu_deaths', color = 'firebrick')
    year_plt.set(xlabel = "Week", ylabel = "Deaths From Influenza", title = f"Death Due to Influenza in {year} by Week")
    st.pyplot(year_plt.figure, clear_figure=True)

st.markdown("Lastly, we can view deaths by geographic region.")
region = st.selectbox("Select a Region:", ["1 - Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont","2 - New York, New Jersey","3 - Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia","4 - Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee","5 - Illinois, Indiana, Minnesota, Michigan, Ohio, Wisconsin","6 - Arkansas, Louisiana, New Mexico, Oklahoma, Texas","7 - Iowa, Kansas, Missouri, Nebraska","8 - Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming","9 - Arizona, California, Hawaii, Nevada","10 - Alaska, Idaho, Oregon, Washington"])
bck_reg = region[0]
graph_region = deaths[(deaths['region'] == int(bck_reg)) & (deaths['geo_level'] == "Region")].groupby('year').sum(numeric_only=True)
if disease == "Pneumonia":
    region_plt = sns.lineplot(graph_region, x='year', y='pneu_deaths', color = 'skyblue')
    region_plt.set(xlabel = 'Year', ylabel = "Deaths From Pneumonia", title = f"Death Due to Pneumonia in Region {bck_reg}")
    st.pyplot(region_plt.figure, clear_figure=True)
if disease == "Influenza":
    region_plt = sns.lineplot(graph_region, x='year', y='flu_deaths', color='firebrick')
    region_plt.set(xlabel = 'Year', ylabel = "Deaths From Pneumonia", title = f"Death Due to Pneumonia in Region {bck_reg}")
    st.pyplot(region_plt.figure, clear_figure=True)

st.write("For more information, you can find my github repo [here](https://github.com/LotusEat3r/Project). You can also find my own exploratory data analysis on my blog: [Part I](https://lotuseat3r.github.io/introeda/) and [Part II](https://lotuseat3r.github.io/eda/)")