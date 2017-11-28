import os
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
    #finds the target
    UserTarget = input("What is the target?(User URL) \n")
    inquireIfKnown()
    

def multiU():
    #creates an array to search through
    createArray = []
    while True:
        toAdd = input('To (To end just hit enter)')
        createArray = createArray.append(toAdd)
        if toAdd == '':
            break
        
    

def foundProfiles():
    #opens a txt file and presents profiles, these profiles can be selected to be updated, deleted or for further digging
    open()

def inquireIfKnown():
    #find out any additional information about targets
    knownYN = input('Do you already know some information about the target? Y/N (Selecting Yes will inquire about their name, alieses, known profiles, etc.)')
    knownYN = knownYN.lower()
    if knownYN == 'y':
        FirstName = input("What is the Targets First Name? (If unknown just hit 'Enter')")
    if FirstName == '':
        LastName = input('What is the Targets Last Name? (If unknown just hit "enter")')
    else:
        LastName = input("What is " + FirstName + "'s Last name?")
    CorrectName = input('Is ' + FirstName + ' ' + LastName + ' Correct? Y/N')
    CorrectName = CorrectName.lower()
    if CorrectName == 'y':
        print('')

    else:
        inquireIfKnown()
        
def FaceLift(CorrectName, UserTarget):
    #Facebook search
            
    print('Starting User Search /n')
    if CorrectName == '':
        
        

def TwitTwat():
    #Twitter search



def Instafind():
    #Instagram Search



def Redrum():
    #Reddit search

print('Welcome to User Strike \n This is an information intelligence program to track and classify individuals \n You are responsible for any information you discover using this program. \n If you have any questions or suggestions please email me at tburrito@usa.com')
ans = input('What would you like to do? \n 1. Find new user \n 2. Find multiple users \n 3.Look at found profiles \n 4. Quit \n')
anscase(ans)
