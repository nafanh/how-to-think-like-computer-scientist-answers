# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result

wins_human = 0
wins_computer = 0
draws = 0
total = 0
while True:
    result = play_once('joe mama')
    if result == 1:
        wins_computer += 1
    elif result == 0:
        draws += 1
    else:
        wins_human +=1
    total += 1
    print("Percent wins Human: {0} Percent wins computer: {1} Percent Draws: {2}".format(
        (wins_human/total) * 100 , (wins_computer/total) * 100, (draws/total) * 100
    ))
    play_again = input("Do you want to play again? ")
    if play_again == 'yes' or play_again == 'Yes':
        continue
    print("Goodbye")
    break
