import math

# prompt the user for their name
user_name = input("Welcome to GC Mini Golf! What is your name? ")

# create game options in an array with game being played and number of holes as int
game_options = ["3", "6"]

# prompt user to make a game selection to play 3 or 6 holes of mini golf
game_selection = input(f"Hi {user_name}! Would you like to play 3 or 6 holes? ")

# Finally, proszaz#Z#ser44trdnmpt the user for each "hole of golf" asking for the number of putts for each specific hole.
hole_number = 1
number_of_putts = input(f"How many number of putts for hole {hole_number}? (par {game_selection})")
hole_number += 1 <= int(game_selection)

while hole_number <= int(game_selection):  # for each hole in the selected game
    number_of_putts = input(f"How many number of putts for hole {hole_number}? (par {game_selection})")

    hole_number += 1
    # write if-else statements for game selection. Write rules to  game for inputs 3 or 6 and not a valid input
    # if user puts any other response
    if game_selection == "3":
        game_outcome = []
        print(number_of_putts)
        game_outcome.append(number_of_putts)
        total_par = sum(game_outcome)
# for i in range(1, 3):
 #    print("How many number of putts for hole {}?".format(hole_number))
  #  hole_number += 1
    elif game_selection == "6":
        game_outcome = []
        print(number_of_putts)
        game_outcome.append(number_of_putts)
        total_par = sum(game_outcome)

    else:
        print(f"Sorry. {game_selection} is an invalid option.")


#Keep track of their cumulative score (total number of putts) and, at the end,
# compare that to the total course par (9 if they chose 3 holes,
# 18 if they chose 6 — par is 3 for every hole) to calculate the golfer’s total par for the round.