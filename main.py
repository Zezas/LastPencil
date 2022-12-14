import random

Name_1 = "John"
Name_2 = "Jack"  # the bot


# game prep loop
print("How many pencils would you like to use:")
while True:
    try:
        pencils = int(input())

        # could change the conditions orders, so it goes faster when is correct
        if pencils < 0:
            raise ValueError
        elif pencils == 0:
            print("The number of pencils should be positive")
        else:
            break

    except ValueError:
        print("The number of pencils should be numeric")

# game starter loop
print(f"Who will be the first ({Name_1}, {Name_2}):")
while True:
    First_Player = input()

    # add second player
    if First_Player == Name_1:
        Second_Player = Name_2
        break
    elif First_Player == Name_2:
        Second_Player = Name_1
        break
    else:
        print(f"Choose between '{Name_1}' and '{Name_2}'")

# show pencils
print("|" * pencils)
# first interaction
player = First_Player
print(f"{player}'s turn:")

# game loop
while pencils > 0:
    # value check for non-bot player
    if player == Name_1:
        try:
            pencils_to_remove = int(input())
            if pencils_to_remove < 1 or pencils_to_remove > 3:
                raise ValueError
            elif pencils_to_remove > pencils:
                print("Too many pencils were taken")
                continue
        except ValueError:
            print("Possible values: '1', '2', or '3'")
            continue
    # bot playing
    else:
        # only on pencil left, bot loses
        if pencils == 1:
            pencils_to_remove = 1
        # losing position
        elif (pencils - 1) % 4 == 0:
            pencils_to_remove = random.randint(1, 3)
        # last winning positions
        else:
            pencils_to_remove = (pencils - 1) % 4
        print(pencils_to_remove)

    print("|" * (pencils - pencils_to_remove))
    pencils -= pencils_to_remove

    # player change
    if player == First_Player:
        player = Second_Player
    else:
        player = First_Player

    # end game validation
    if pencils == 0:
        print(f"{player} won!")
        break
    else:
        print(f"{player}'s turn:")
