# this is no guessing game

no = 18
no_of_guesses = 1
print("welcome to game bro \n")
print("you have 9 chances to guess the no \n")

while(no_of_guesses <= 9):
    guess_no = int(input("guess the no:\n"))
    if guess_no > no:
        print("aage ja raha hai , TRY AGAIN")
    elif guess_no < no:
        print("you went to BACK, TRY AGAIN")
    else:
        print("you won bro")
        print("you guess ", no_of_guesses, "times")
        break
    print(9 - no_of_guesses,"no of guesses left")
    no_of_guesses = no_of_guesses +1


if no_of_guesses >= 9:
    print("game over")