#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# letter = open("./Input/Letters/starting_letter.txt", "r")
# print(letter.readlines())
# letter.close()

# with open("./Input/Letters/starting_letter.txt", "r") as letter:
#     letter_list = letter.readlines()
#     print(letter_list[0])
#     name = letter_list[0].replace('[name]', 'Stefan')
#     print(name)



with open("./Input/Names/invited_names.txt", "r") as names:
    for name in names:
        with open("./Input/Letters/starting_letter.txt", "r") as letter:
            letter_list = letter.readlines()
            with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt",'w') as new_letter:
                new_name = letter_list[0].replace('[name]', name.strip())
                new_letter.write(f"{new_name}{''.join(letter_list[1:])}")
                print(new_letter)
