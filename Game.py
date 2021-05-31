import random
# --> snake, water and gun == scissor rock and paper


def gameWin(comp,  you):
    if comp == you:
        return None
    if comp == "s":
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == "g":
        if you == 's':
            return False
        elif you == 'w':
            return True


randNo = random.randint(1, 3)
print("Computer turn: Snake(s), Water(w) and Gun(g)...")
print("Done, Computer choosed something, Now it's Your turn")
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
# print(randNo)
print("Your turn: Snake(s), Water(w) and Gun(g)")
you = input('Choose between s, w and g: ')
print(f"Computer choose: {comp}")
print(f"You choose: {you}")
a = gameWin(comp,  you)
if a == None:
    print("OOps! game is tie")
elif a:
    print("Hurray!! You won the game")
else:
    print("So Sad, You loose the game Try Next Time!!")
