# Game: Snake Water Gun
import random
options = ["Snake", "Water", "Gun"]
c_points = 0
u_points = 0
print("Welcome to the game: Snake Water Gun")
print("Let's Play:\n")
print("Press key s for the snake")
print("Press key w for the water")
print("Press key g for the gun")
i=0
while(i<10):
    comp = random.choice(options)
    u = input("Choose one option: ")
    if u=="s" and comp=="Water":
        print("Yeah!!! Your snake drink the Opponent's Water\n")
        u_points+=1
    elif u=="s" and comp=="Gun":
        print("Ohh!!! Your snake has been killed by the Opponent's Gun\n")
        c_points+=1
    elif u=="g" and comp=="Snake":
        print("Yeah!!! You killed the Opponent's Snake\n")
        u_points+=1
    elif u=="g" and comp=="Water":
        print("Ohh!!! Your gun has been spoiled by the Opponent's Water\n")
        c_points+=1
    elif u=="w" and comp=="Snake":
        print("Ohh!!! You have been beaten by the opponent\n")
        c_points+=1
    elif u=="w" and comp=="Gun":
        print("Yeah!!! You spoiled the opponent's Gun\n")
        u_points+=1
    elif u=="w" and comp=="Water":
        print("Same Option choosen\n")
    elif u=="g" and comp=="Gun":
        print("Same Option choosen\n")
    elif u=="s" and comp=="Snake":
        print("Same Option choosen\n")
    else:
        print("You choosen input is wrong.... Plz check the input & Try Again\n")
        continue
    i+=1

print(f"You scored {int(u_points)} points in the game")
print(f"Your opponent scored {int(c_points)} points in the game")
if(u_points>c_points):
    print("Yeah!!! You win the game")
elif(c_points>u_points):
    print("So Sorry!!! You lost")
else:
    print("Opponent & You both scored same points.....Tie up!!!")