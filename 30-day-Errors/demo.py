try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key{error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError("this is an error that i made up ")

height = float(input("Height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

