import random 

number = random.randint(1,100)

while True:
    user = input("ENTER YOUR NUMBER('q' for quit) : ")

    if user == "q":
        print("try again")
        break
    user = int(user)

    if user == number:
        print("YOU FOUND SUCCESFULLY")
        break
    elif user >= number:
        print("YOUR NUMBER IS BIGGER")
    else:
        print("YOUR NUMBER IS SMALLER")
print("====================[{(GAME OVER)}]====================")