import pandas

original_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(original_data[original_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(original_data[original_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(original_data[original_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

new_data = pandas.DataFrame(data_dict)

print(new_data)
