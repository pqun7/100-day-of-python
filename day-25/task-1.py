import csv
import pandas as pd
file = pd.read_csv(r'C:\Users\egtea\OneDrive\سطح المكتب\my projects\100 Day\day-25\004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
color = file["Primary Fur Color"]
color_name = ["Cinnamon", "Gray", "Black"]
con = []
for name in color_name:
    gray = file[file["Primary Fur Color"] == name]
    count = con.append(len(gray))
dcit = {
        "Fur Color": color_name,
        "Count": con}
dic = pd.DataFrame(dcit)
dic.to_csv("Color.csv")
print(dic)