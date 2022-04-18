# with open ("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)


# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
    # print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# # Converting to a dictionary
# data_dic = data.to_dict()
# print(data_dic)

# Converting to a list
temp_list = data["temp"].to_list()
print(len(temp_list))

# # To get Average
# average = sum(temp_list)/len(temp_list)
# print(average)
# print(data["temp"].mean())

# # To get maximum value
# print(data["temp"].max())

# # Getting Data in columns
# print(data["condition"])
# print(data.condition)

# # Getting Data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# mon_temp = int(monday.temp)
# temp_in_F = (monday.temp*9/5) + 32
# print(temp_in_F)

# Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

# Squirrels
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("squirrel_Data.csv")
grey =len( data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
print(grey)
print(red)
print(black)

data_dict = {
    "Fur Color" : ["Gray", "Cinammon", "Black"],
    "Count" : [grey, red ,black]
}

print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_1.csv")
