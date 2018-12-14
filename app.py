import random
input_number = 0
quit = ""

while quit != "n":
    print(str(random.randrange(int(input("How many sides does your die have? ")))+1))
    quit = input("do you wish to roll again? y/n: ").lower()
    if quit == "n":
        break
    else:
        ""
input()