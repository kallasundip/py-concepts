'''
number = 9
count=0

while (count < 3):
    guess = int(input("Guess: "))   #user input comes String converted into int
    count +=1
    if guess == number:
        print("you win")
        break;
else:
    print("Sorry You Failed!")

'''


value = input(">")
if value == "help":
    print(help)
    print("Start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")
    car = input(">")
    if car == "start":
        print("Car started...Ready to go!")
        cstop = input(">")
        if cstop == "stop":
            print("Car stopped...")
            cquit = input(">")
            if cquit == "quit":
                print("Car stop")
else:
    print("It didn't Under Stant")


