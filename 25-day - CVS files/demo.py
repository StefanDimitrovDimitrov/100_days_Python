# with(open("weather_data.csv")) as data:
#     data = data.readlines()
#     print(data)

# import csv
#
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     temperatures.pop(0)
#     temperatures = [int(x) for x in temperatures]
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print((sum(temp_list)/len(temp_list)))
#
# # data['temp'].mean()
# print(data['temp'].max())



# _______________________________
# create new cvs

# data_dict = {
#     'student':['Amy', 'James', 'Angela'],
#     'scores':[76, 56, 65]
#
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')