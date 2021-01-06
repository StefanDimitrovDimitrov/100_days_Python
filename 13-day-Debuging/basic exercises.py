for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    #   replace or with and
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
# we have to remove []
year = input("Which year do you want to check?")
#  we have to parse the number adding int()
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
#     The final print should be Leap year.

number = input("Which number do you want to check?")
# number % 2 = 0 is wrong
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

