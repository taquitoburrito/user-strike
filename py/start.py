import os
print('Welcome to User Strike \n This is an information intelligence program to track and classify individuals \n You are responsible for any information you discover using this program. \n If you have any questions or suggestions please email me at tburrito@usa.com')
ans = input('What would you like to do? \n 1. Find new user \n 2. Find multiple users \n 3.Look at found profiles \n 4. Quit \n')
anscase(ans)
def anscase(ans):
    if ans == '1':
        singleU()
    elif ans == '2':
        multiU()
    elif ans == '3':
        foundProfiles()
    elif ans == '4':
        quit

def singleU ():
    UserTarget = input("What is the target?(User URL) \n")
    

def multiU():
    createArray = []
    while True:
        toAdd = input('To (To end just hit enter)')
        createArray = createArray.append(toAdd)
        if toAdd == '':
            break
        
    

def foundProfiles():
    open()

def inquireIfKnown():
    knownYN.lower() = input('Do you already know some information about the target? Y/N (Selecting Yes will inquire about their name, alieses, known profiles, etc.)')
    if knownYN == 'y':
        FirstName = input("What is the Targets First Name? (If unknown just hit 'Enter')")
    else:
        break
    if FirstName == '':
        LastName = input('What is the Targets Last Name? (If unknown just hit "enter")')
    else:
        LastName = input("What is " + FirstName + "'s Last name?")
    CorrectName.lower() = input('Is ' + FirstName + ' ' + LastName + ' Correct? Y/N')
    if CorrectName == 'y':
        continue
    else:
        inquireIfKnown()
        
            
            
    

