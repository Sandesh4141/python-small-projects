no = 18
chances = 1

print("welcome to number guess challange\n")
while(chances <= 5):
    choice = int(input("enter your choice no:"))
    if choice > no:
        print("number is too strong")
    elif (choice) < no:
        print("number too weak")
    else:
        print("you are winer")
        break
    print(5 - chances,"chances you have left")
    chances = chances +1

if chances >=5:
    print(""
          ""
          "GAME OVER\n"
          "\n"
          "\n"
          "\n"
          "THIS GAME IS DEVELOPED BY SANDESH PAWAR")
