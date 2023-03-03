# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 16:22:33 2023

@author: Adedoyin Idris
"""

# Import modules
import pandas as pd
import matplotlib.pyplot as plt

# A function to calculate the percentage of each ethnicity
def calculate_percentage(percentage, ethnic_count):
    return "{:.1f}%".format(percentage)

# Read the dataset from the csv source file
congress_women_data_frame = pd.read_csv("women_of_color_congress.csv", 
                                        encoding='ISO-8859-1')

# A list of ethnicity in the dataset
ethnicity = ["African American", "Hispanic American", 
             "Asian-Pacific American", 
             "African American, Asian-Pacific American"]

# The number of each ethnic group in the dataset
ethnicity_count = congress_women_data_frame["Ethnicity"].value_counts()

# Wedge properties for the pie plot
wedge_property = {'linewidth':2, 'edgecolor':"black"}
 
# Create a new figure for the pie plot 
fig, ax = plt.subplots(figsize=(16, 13))

# Plot the pie plot
wedges, texts, autotexts = ax.pie(ethnicity_count,
                                  autopct=lambda percentage: 
                                  calculate_percentage(percentage, 
                                                       ethnicity_count), 
                                  labels=ethnicity, 
                                  startangle=65, 
                                  wedgeprops=wedge_property,
                                  textprops=dict(color ="black"))
 
# Describes the elements of the pie plot
ax.legend(wedges, ethnicity)

# Set properties for the percentages in each wedge of the pie plot
plt.setp(autotexts, size=15, weight="bold", color="white")

# Title of the pie plot
ax.set_title("Women of Color in the USA Congress (1965 - 2017)", fontsize=20,
          color="white", backgroundcolor='black', pad='15.0',)

# Saves the pie plot in jpg format
plt.savefig("women of color in the congress.jpg")
 
# show plot
plt.show()