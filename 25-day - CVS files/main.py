import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# grey_squirrels_count = len(data[data["Primary Fur Color"]=="Grey])
color_list = data["Primary Fur Color"].to_list()

grey = int(color_list.count('Gray'))
red = int(color_list.count('Cinnamon'))
black = int(color_list.count('Black'))

data_color = {
    'Fur Color': ['Grey', 'Red', 'Black'],
    'Count': [grey, red, black]
}
data = pandas.DataFrame(data_color)
data.to_csv('squirrel_count.csv')
