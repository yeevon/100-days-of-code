# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# data.pop(0)

# import csv
#
# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for index, row in enumerate(data):
#         if index == 0:
#             continue
#
#         temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].tolist()
# print(sum(temp_list) / len(temp_list))
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
# print(data.condition)

# get data in the rows of the dataframe

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp * 1.8 + 32)

# Create a df from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")