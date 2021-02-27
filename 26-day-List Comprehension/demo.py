# list compre...

def list_comprehension():
    new_list = [x + 1 for x in [1, 2, 3]]
    return new_list


# list comre string

def str_comprehension():
    new_list = [x for x in "Stefan"]
    return new_list


def range_comprehension():
    new_list = [x * 2 for x in range(1, 5)]
    return new_list


# conditional list comprehension
def condition():
    names = ['Alex', "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
    # short_names =[new_item for iten in list if test]
    short_names = [name for name in names if len(name) < 5]


def condition_Upper():
    names = ['Alex', "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
    # short_names =[new_item for iten in list if test]
    short_names = [name.upper() for name in names if len(name) > 5]
    return short_names


print(condition_Upper())


def squared_numbers():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [x * x for x in numbers]
    return squared_numbers

def even_nums():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    result = [x for x in numbers if x % 2 == 0]
    return result

def dict_comprehension():
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    result = {word: len(word) for word in sentence.split(' ')}

    print(result)

def dict_comp_temperature():
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }

    weather_f = {day: value * 9 / 5 + 32 for (day, value) in weather_c.items()}

    return weather_f