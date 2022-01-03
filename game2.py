import random   
randomNumber=random.randint(1,100)
userguess=None
guesses=0

while(userguess!=randomNumber):
    userguess=int(input("Enter your Guess:"))
    guesses+=1

    if(userguess==randomNumber):
        print("You guessed it corectly")
    else:
        if(userguess<randomNumber):
            print("You guessed it wrong please enter a larger number")
        else:
          
            print("You guessed it wrong please enter a smaller number")

print(f"You guessed the number in {guesses} guesses")
with open("myscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print(" Congratulations !!! :)You have just broken the high score!")
    with open("myscore.txt", "w") as f:
        f.write(str(guesses))
