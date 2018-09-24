print("           Welcome to the Magic Maze           ")
print("***********************************************")

print("                    The Rules                  ")
print("-----------------------------------------------")
print(" - There is a secret combination of directions")
print(" - Guess that combination using N,S,W or E")
print(" - If you guess wrong, you must start over")
print(" - Guess those directions with your 3 lives")
print(" - If you guess wrong, you lose a life")
print('\n')

guessTaken = 0
lives = 3
key = ["S", "S", "W", "N", "E", "S"]
guess = ''
index = 0

start = print(input("Type Start to Play:"))
if start == 'start' or "Start" or "START":
    while index<6:
        guess = input("Enter a Cardinal Direction: ")
        if key[index] == guess:
            print("Correct")
            index = index + 1
            guessTaken = guessTaken + 1
        else:
            print("Wrong.")
            lives = lives - 1
            guessTaken = guessTaken + 1
            index = 0
            if lives == 0:
                break
            continue

    if lives == 0:
        print(" \n      GAME OVER        ")
        print("You lost all your lives :(")
    else:
        print("Congratulations! Felicidades! おめでとうございます! Gratulation! Felicitări!")
        print("You Win! \n You Guessed the Code in ", guessTaken, " guesses!")



