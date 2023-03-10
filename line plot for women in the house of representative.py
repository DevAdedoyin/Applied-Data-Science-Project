# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 16:22:33 2023

@author: Adedoyin Idris
"""

# import modules
import pandas as pd
import matplotlib.pyplot as plt

# Global variables
start_index = 29
marker = "o"

# A function to read the dataset from the excel source file
def dataframe():
    # Read the dataset into a variable called data_frame
    data_frame = pd.read_excel("Women in the House of Representatives.xlsx",)
    
    # Retrieve the years from 1975 to 2019
    years = data_frame["Years"][start_index:]  
    return data_frame, years

# Call the dataframe function and store the return values of the function 
# into the variables dataframe and years
dataframe, years = dataframe()

# Create a new figure for the plot 
plt.figure(figsize=(14, 10))

# Retrieve data for total number of women, 
# number of women in the republican party,
# number of women in the democratic party 
total_women = dataframe["Women total"][start_index:]
republican_women = dataframe["Republican"][start_index:]
democratic_women = dataframe["Democratic"][start_index:]

# A list of the total number of women and number of women by party
number_of_women = [total_women, republican_women, democratic_women,]

# A list of labels for each line plot
labels = ["Total Number of Women", "Number of Republican", 
          "Number of Democratic",]

# This for-loop, loops through both the number_of_women and labels list and
# plots out each line in the plot
for number_of_women_, labels_ in zip(number_of_women, labels):
    plt.plot(years, number_of_women_, label=labels_, marker=marker)

# Labels for the x and y axis
plt.xlabel("Years", fontsize=16)
plt.ylabel("Number of Women", fontsize=16)

# Rotate the x-axis ticks for legibility
plt.xticks(rotation=50)

# Title for the plot
plt.title("Women in the USA House of Representatives (1975 - 2019)", 
          fontsize=20,
          color="white", backgroundcolor='black', pad='15.0',)

# Describes the elements of the plot
plt.legend()

# Saves the plot in jpg format
plt.savefig("women in the house of rep.jpg", dpi=300)

# Displays the plot
plt.show()
