def add(*args):
    sum_total = sum(args)
    # sum = 0
    # for n in args:
    #     sum += int(n)
    return sum_total

print(add(5, 6, 7))


def calculate(n, **kwargs):
    # for k, v in kwargs.items():
    #     print(k)
    #     print(v)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add = 3, multiply = 5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make = "Nissan", model = "GT-R")
print(my_car.model)