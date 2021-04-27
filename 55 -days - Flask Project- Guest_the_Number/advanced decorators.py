# You called a_function(1,2,3)
#it returned: 6

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}\nIt returned: {function(args[0], args[1], args[2])}")
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a + b + c

a_function(1, 2, 3)