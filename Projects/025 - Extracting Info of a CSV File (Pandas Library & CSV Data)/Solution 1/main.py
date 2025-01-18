import pandas

original_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = 0
cinnamon_squirrels_count = 0
black_squirrels_count = 0

for color in original_data["Primary Fur Color"]:
    if color == "Gray":
        gray_squirrels_count += 1
    if color == "Cinnamon":
        cinnamon_squirrels_count += 1
    if color == "Black":
        black_squirrels_count += 1

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
