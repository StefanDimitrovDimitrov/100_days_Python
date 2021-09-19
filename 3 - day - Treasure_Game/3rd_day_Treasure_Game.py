print('''
      .-----------.
      |.---------.|                         _      _
      ||         ||          ______      {>|_|<}   )\
      ||_________||         (_____()8oo.          (__)
      ;-----------;      I've tried all sorts of chocolate
    .':O8OoOo8oo.'|      White, and milk and plain -
  .';OoO8oO8oo.' /       From every place and country -
  |"""""""""""| /        Belgian, Swiss and Mayan.
  |__BonBons__|/

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_choice = input(
    "In front of you, the path goes left or right. What do you choose? Please type RIGHT or LEFT:\n").lower()

if first_choice == "left":
    second_choice = input(
        "You've found a river. How would you cross the river? You can try to swim or find a bridge? Please type SWIM or BRIDGE if you go with the second option.\n").lower()
    if second_choice == "swim":
        print("You manage to cross the river.")
        third_choice = input("Around the near bush you find thrее boxes. Which one you will open? The red, the yellow, or the purple?Pleasee type: RED, YELLOW or PURPLE\n").lower()
        if third_choice == "purple":
            print("YOU WON. The chocolate is yours")
        elif third_choice == "yellow":
            print("You miss the treasure. Try one more time.")
            one_more_time = input("RED or PURPLE?\n").lower()
            if one_more_time == "purple":
                print("YOU WON. The chocolate is yours")
            else:
                print("You die bitten by snake\n GAME OVER")
        elif third_choice == "red":
            print("You die bitten by snake\n GAME OVER")
    else:
        print("Wile you looking for a bridge a group of robbers catch you.\n GAME OVER")
else:
    print("Your phone is ringing. Your boss is calling you for something urgent.You have to stop playing.\nGAME OVER")
