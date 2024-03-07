# with open(r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\100 Day\day-25\002 weather-data.csv", "r") as data:
#     reader = data.readlines()
#     print(reader)
#
# import csv
#
# with open(r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\100 Day\day-25\002 weather-data.csv") as data:
#     data = csv.reader(data)
#     temperatures = []
#     for raw in data:
#         if raw[1] != "temp":
#             temperatures.append(int(raw[1]))
# #     print(temperatures)
#
import pandas
data = pandas.read_csv(r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\100 Day\day-25\002 weather-data.csv")
#data_max = data["temp"].max()
#print(data_max)

#Get data in Colums
# print(data["day"])
# print(data.day)

#Get data in raw
raw1 = data[data.day == "Monday"]
#print(raw1)

#Get the max raw in data
data_max = data["temp"].max()
raw_max = data[data.temp == data_max]
#print(raw_max)

#Get the temp of the day
monday = data[data.day == "Monday"]
print(monday.temp)

# trmp = data.temp
# fahrenheit_temperatures = (trmp * 9/5) + 32
# print(fahrenheit_temperatures)

#Create a dataframe from scratch
data_stodant = {"staondt": ["Ahmed", "Ali", "Nazer"],
                "score": [95, 85, 94]
                }
data = pandas.DataFrame(data_stodant)
data.to_csv("New_file.csv")
#print(data)


