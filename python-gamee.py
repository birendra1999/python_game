import random
lst=["s","p","r"]
no_of_chance=0
chance=3
computer_point= 0
timro_point= 0
print("\t \t \t this is scissor paper rock game")
print("press s for scissor \n p for paper \n r for rock")

while(no_of_chance<chance):
    _input= input("scissor, paper, rock:")
    _random= random.choice(lst)

    if(_input== _random):
        print("its a tie no one wins")

    elif(_input=="p" and _random=="s"):
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer guess is{_random}")
        print("computer wins 1 point")
        print(f"computer point is{computer_point}and your point is {timro_point}\n")

    elif(_input=="p" and _random=="r"):
        timro_point=timro_point+1
        print(f"your guess is{_input} and computer guess is{_random}")
        print("you win 1 point")
        print(f"computer print is {computer_point}and your point is{timro_point}\n")

    elif(_input=="s"and _random=="r"):
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer guess uis{_random}")
        print("computer win 1 point")
        print(f"computer point is{computer_point} and your point is{timro_point}\n")

    elif(_input=="s" and _random=="p"):
        timro_point=timro_point+1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("you win 1 point")
        print(f"computer point is {computer_point} and your point is{timro_point}\n")

    elif(_input=="r" and _random=="p"):
        computer_point=computer_point+1
        print(f"your guess is {_input}and computer guess is {_random}")
        print("computer wins 1 point")
        print(f"computer point is{computer_point} and your point is {timro_point}\n")

    elif(_input=="r" and _random=="s"):
        timro_point=timro_point+1
        print(f"your guess is {_input}and computer guess is{_random}")
        print("you win 1 point")
        print(f"computer point is{computer_point} and your point is{timro_point}\n")


    else:
        print("it is a wrong input\n")
    no_of_chance=no_of_chance+1
    print(f"{no_of_chance}chance is already played out of {chance}for you now\n")

print("game over")

if(computer_point==timro_point):
    print("its a tie")

elif(computer_point>timro_point):
    print("computer wins you lose")

elif(computer_point<timro_point):
    print("you win computer lose")

print(f"your point is {timro_point} and computer point is {computer_point}")



