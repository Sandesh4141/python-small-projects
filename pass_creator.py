
import random

print("length/strength should be in numbers".title())

strength = int(input("Enter length of password:".title()))

if strength <= 5:
    print("you can choose more strong password. ".title())

characters = ["!", "@", "#", "%", "&", "*", "_", "-"]
low_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
upp_letters = ['A','B','C','D','E','F','J','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']


all = characters + low_letters + upp_letters

password = "".join(random.sample(all, strength))

print(f"Here is your Password --->\n {password}")
