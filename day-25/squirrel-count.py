import pandas

df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250610.csv")

fur = df["Primary Fur Color"]
fur_dict = {
    'Fur': ['grey', 'red', 'black'],
    'Count':[(fur == 'Gray').sum(), (fur == 'Cinnamon').sum(), (fur == 'Black').sum()]
}

fur_df = pandas.DataFrame(fur_dict)
print(fur_df)
