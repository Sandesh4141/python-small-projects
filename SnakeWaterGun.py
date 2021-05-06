import random

choices = ['s', 'w', 'g']



rules = ("s: Snake\t w: Water \t g:Gun")
n = 0
gamerScore = 0
CpuScore = 0


print("\t \t \t \t \t \t YOU HAVE TO TRY YOUR LUCK 10 TIMES.\n"
              "\t \t \t  \t \t \t \t \t \t BEST OF LUCK")
try:
    while n < 10:
        print("CHOOSE YOUR CHOICE ---------->  " +  rules, "<<<-----------------------")
        user = input("Enter your choice:-")
        CpuChoice = random.choice(choices)
        if user == 's':
            if CpuChoice == 'w':
                gamerScore = gamerScore + 1
                print("Your snake drink cpu's water!!! You got 1 point.")

            elif CpuChoice == 's':
                gamerScore = gamerScore + 0
                CpuScore =CpuScore +0
                print("\t \t TIE!! Both Are Same.")
            else:
                CpuScore = CpuScore + 1
                print("Cpu has Gun, He kill Your snake!! cpu got 1 point!!")




        elif user == 'w':
            if CpuChoice == 'g':
                gamerScore = gamerScore + 1
                print("\t \t Cpu Choose Gun, You got 1 point!!")

            elif CpuChoice == 's':
                CpuScore = CpuScore + 1
                print("\t \t Snake drank your water, cpu got 1 point!!!")
            elif CpuChoice == 'w':
                CpuScore = CpuScore +0
                gamerScore = gamerScore +0
                print("\t \t \t TIE!")
            else:
                CpuScore = CpuScore +1
                print(" \t \t Cpu got gun!. You get killed!!")


        elif user == 'g':
            if CpuChoice == 's':
                gamerScore = gamerScore + 1
                print("\t \tYou killed snake!!. You got 1 point!!")
            elif CpuChoice == 'w':
                CpuScore + 1
                print("\t \t Gun get drown in water!!! Cpu got 1 point!")
            else:
                print("\t \t \t \t TIE!!!")




        else:
            print("\t \t TRY VALID INPUT FROM", rules)
            continue

        n = n + 1
        if n == 10:
            break

    if CpuScore > gamerScore:
        print("------------->>> CPU WINS <<<------------"," Total Points you Scored -->", CpuScore, "out of 10")
    else:
        print("------------>>> YOU WIN <<<-------------","Total Points you Scored --->",  gamerScore, "out of 10")
except TypeError:
    print( "this is error 404")
