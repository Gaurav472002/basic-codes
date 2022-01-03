import random


def gamewinner(comp, you):
    if(comp == you):
        return None

    elif(comp == "rock"):
        if you == "scissor":
            return False
        elif you == "paper":
            return True

    elif comp == "paper":
        if you == "rock":
            return False
        elif you == "scissor":
            return True

    elif comp == "scissor":
        if you == "paper":
            return False
        elif you == "rock":
            return True


print("Computer Turn: 1-> Rock : 2-> Paper : 3-> scissor")

randomout = random.randint(1, 3)
if randomout == 1:
    comp = 'rock'
elif randomout == 2:
    comp = 'paper'
elif randomout == 3:
    comp = 'scissor'


you = input('''Your Turn: Please Select  
1-> rock  
2-> paper 
3-> scissor:\t''')
a = gamewinner(comp, you)
print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
