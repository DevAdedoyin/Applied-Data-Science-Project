# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 16:58:15 2023

@author: Adedoyin Idris
"""

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import color_module

# Global variable
percentage = []
colors = color_module.colors()
bar_plot = object
index = 0

# A function to calculate the percentage occurence each category 
def calculate_percentage(dataframe):
    # Calculate the sum of frequency
    total_frequency = dataframe.Frequency.sum()
    
    for count in range(len(dataframe.Category)):
        pct = (dataframe.Frequency[count] / total_frequency) * 100
        percentage.append(round(pct, 2))
        
    return percentage

# Read the dataset from the csv source file
dataframe = pd.read_csv("googleplaystore.csv")

# Count the number of category
category_count = dataframe["Category"].value_counts()

# Convert category_count to a new dataframe
new_data_frame = category_count.rename_axis('Category') \
                .reset_index(name='Frequency')

# Extract the 1st 33 rows of the new dataframe
new_data_frame = new_data_frame[:20]

# Add the percentage frequency of each category to the new_data_frame
# as a table
new_data_frame['Percentage'] = calculate_percentage(new_data_frame)

# Create a list of the category and frequencies 
list_of_categories = list(new_data_frame.Category)
list_of_frequency = list(new_data_frame.Frequency)

# Create a new figure for the plot 
plt.figure(figsize=(50, 48))

# Create the plot for each category in the new_data_frame
for category, frequency, color, count in zip(list_of_categories, 
                                             list_of_frequency, colors, 
                                             category_count):
    label = f"{count} {category} Apps " 
    bar_plot = plt.bar(category, frequency, color=color, label=label)
    for plot in bar_plot:
        width = plot.get_width()
        height = plot.get_height()
        x, y = plot.get_xy()
        plt.text(x+width/2,
                 y+height*1.01,
                 str(new_data_frame.Percentage[index])+'%',
                 ha='center',
                 size=35,
                 rotation=45,
                 )
        index+=1

# Title of the plot
plt.title(
    "The Frequency of Apps in 20 of the top Categories" 
    " in the Google Playstore (2018)",
    fontsize=40, color="white", backgroundcolor='black', pad='15.0',)

# x and y ticks of the plot.
plt.xticks(fontsize=33, rotation=69)
plt.yticks(fontsize=33)

# Describes the elements of the plot
plt.legend(fontsize=30)

# Saves the bar plot in jpg format
plt.savefig("frequency of the categories of app.jpg", dpi=300)

# Displays the plot   
plt.show()

