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