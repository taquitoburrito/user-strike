#ask for social media account to follow
import os
print('Welcome to User Strike \n This is an information intelligence program to track and classify individuals \n You are responsible for any information you discover using this program. \n If you have any questions or suggestions please email me at tburrito@usa.com')
ans = input('What would you like to do? \n 1. Find new user \n 2. Find multiple users \n 3.Look at found profiles \n 4. Quit \n')

if ans == '1':
    UserTarget = input("What is the target?(User URL) \n")
    yn = input('Is this correct(y/n)? \n' + UserTarget + '\n')
elif ans == '2':
    createArray = input('How many users are you going to search for?')
elif ans == '3':
    open()
elif ans == '4':
    print('Goodbye')
    
