"""
Squirrel Fur Color Counter

This script analyzes data from the 2018 Central Park Squirrel Census to count the number of squirrels 
with different primary fur colors. It creates a CSV file containing the counts for each fur color category.

Dependencies:
    - pandas: For data manipulation.

Usage:
    Run this script to count the number of squirrels with different fur colors by: $ python3 main.py
    Ensure that the input CSV file ("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") is in the same directory.
    The script will generate an output CSV file ("Fur_Color_Count.csv") containing the fur color counts.

"""

import pandas

# Fur color counter
data_squirrel  = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color_gray = data_squirrel[data_squirrel["Primary Fur Color"] == "Gray"]
fur_color_black = data_squirrel[data_squirrel["Primary Fur Color"] == "Black"]
fur_color_cinnamon = data_squirrel[data_squirrel["Primary Fur Color"] == "Cinnamon"]

data_dict = {
    "Fur Color" : ["Gray", "Black", "Cinnamon"],
    "Count" : [len(fur_color_gray), len(fur_color_black), len(fur_color_cinnamon)]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Fur_Color_Count.csv")