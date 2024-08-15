
# prompt the user for their name
user_name = input("Welcome to GC Mini Golf! What is your name? ")

# create game options in an array with game being played and number of holes as int
#game_options = ["3", "6"]

# prompt user to make a game selection to play 3 or 6 holes of mini golf
game_selection = input(f"Hi {user_name}! Would you like to play 3 or 6 holes? ")

# Finally, prompt the user for each "hole of golf" asking for the number of putts for each specific hole.

if game_selection == "3":
    hole1 = input(f"How many number of putts for hole 1? (par {game_selection}) ")
    hole2 = input(f"How many number of putts for hole 2? (par {game_selection}) ")
    hole3 = input(f"How many number of putts for hole 3? (par {game_selection}) ")
# Keep track of their cumulative score (total number of putts)
    total_putts = int(hole1) + int(hole2) + int(hole3)
    # compare that to the total course par (9 for 3 holes) to calculate the golfer’s total par for the round.
    total_course_par = 9
    golfers_total_par = int(total_putts) - total_course_par
    # After the last hole, 1/3 messages is printed to the console depending on if the user was over, under or on par

    # If over par, message should read "Nice try, (name)... Your total score was: +(par).
    if total_putts > total_course_par:
        print(f"Nice try, {user_name}. Your total score was: + {golfers_total_par}.")
    # If under par, the message should read "Great job, (name)! Your total score was: -(par)."
    elif total_putts < total_course_par:
        print(f"Great Job, {user_name}. Your total score was: - {golfers_total_par}.")
    # If even with par, the message should read "Good game, (name). Your total score was: 0."
    else:
        print(f"Good game, {user_name}. Your total score was: {golfers_total_par}.")


elif game_selection == "6":
    hole1 = input(f"How many number of putts for hole 1? (par {game_selection}) ")
    hole2 = input(f"How many number of putts for hole 2? (par {game_selection}) ")
    hole3 = input(f"How many number of putts for hole 3? (par {game_selection}) ")
    hole4 = input(f"How many number of putts for hole 4? (par {game_selection}) ")
    hole5 = input(f"How many number of putts for hole 5? (par {game_selection}) ")
    hole6 = input(f"How many number of putts for hole 6? (par {game_selection}) ")
    # Keep track of their cumulative score (total number of putts)
    total_putts = int(hole1) + int(hole2) + int(hole3) + int(hole4) + int(hole5) + int(hole6)
    # compare that to the total course par (18 for 6 holes) to calculate the golfer’s total par for the round.
    total_course_par = 18
    golfers_total_par = int(total_putts) - total_course_par

    # After the last hole, 1/3 messages is printed to the console depending on if the user was over, under or on par

    # If over par, message should read "Nice try, (name)... Your total score was: +(par).
    if total_putts > total_course_par:
        print(f"Nice try, {user_name}. Your total score was: + {golfers_total_par}.")
    # If under par, the message should read "Great job, (name)! Your total score was: -(par)."
    elif total_putts < total_course_par:
        print(f"Great job, {user_name}! Your total score was: - {golfers_total_par}.")
    # If even with par, the message should read "Good game, (name). Your total score was: 0."
    else:
        print(f"Good game, {user_name}. Your total score was: {golfers_total_par}.")
else:
    print(f"Sorry. You made an invalid selection.")

