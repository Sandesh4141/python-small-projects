#! python3
# practise.py - insecure password locker
import sys
import pyperclip as pc


PASSWORDS = {'email': 'sandesh@41',
             'spotify': 'hackersp41'}
if len(sys.argv) < 2:
    print('usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]

if account not in PASSWORDS:
    print(f"Do You want to add {account} to Database")
    print("Account not in password enter password to add in Database!\n")
    inp = input("Enter pass or enter 'q' to quit:")
    if inp != 'q':
        PASSWORDS[account] = inp
        
        print("account added with password to database!\n")

elif account in PASSWORDS:
    pc.copy(PASSWORDS[account])
    print(f"Password copied for {account}")
else:
    print(f"{account} not found")

with open('pass_file.txt', 'w') as pw:
    pw.write(PASSWORDS)