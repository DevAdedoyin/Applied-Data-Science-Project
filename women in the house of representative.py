# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:12:04 2023

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_excel("Women in the House of Representatives.xlsx",)
print(data_frame)

plt.figure(figsize=(14,8))

plt.xticks(rotation=90)

plt.plot(data_frame["Congress"], data_frame["Women total"], marker="o")
plt.plot(data_frame["Congress"], data_frame["Republican"], marker="o")
plt.plot(data_frame["Congress"], data_frame["Democratic"], marker="o")

# Labels for the x and y axis
plt.xlabel("Congress")
plt.ylabel("Number of Women")

plt.title("Women in the House of Representatives (65th to 115th Congress)")

plt.show()