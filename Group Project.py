# Group Project
"""
Alex Cabezas
Luke Bianchi
Skye Jorgensen

Pledge: "I pledge my honor that I have abided by the Stevens Honor System."

"musicrecplus.txt"
"""
import os.path
F="musicrecplus.txt"
def fixSingers(L):
    newSingerList=[]
    for singer in L:
        newName=singer.title()
        newSingerList+=[newName]
    return newSingerList

def getUsers(filename):
    """
    Creates dictinoary of all users
    """
    memo={}
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(":")
            singersList = singers.split(",")
            finalSingersList=fixSingers(singersList)
            finalSingersList.sort()
            memo[username]=finalSingersList
    return memo
def write_file(string, filename):
    myfile = open(filename, "w")
    myfile.write(string)
    myfile.close()
def saveAndQuit(users):
    finalString=""
    for person in users.keys():
        finalString=finalString+person+":"
        for song in users[person]:
            finalString=finalString+song+','
        finalString=finalString[0:-1]+"\n"
    write_file(finalString, F)
    
def menu(users):
    startMenu=True
    values=['e','r','p','h','m','q']
    while startMenu==True:
        option=input("Enter a letter to choose an option:\n"+
            "e - Enter preferences\n"+
            "r - Get recommendations\n"+
            "p - Show most popular artists\n"+
            "h - How popular is the most popular\n"+
            "m - Which user has the most likes\n"+
            "q - Save and quit\n")
        if option in values:
            if option=='e':
                enterPref()
            elif option=='r':
                getRec()
            elif option=='p':
                showMostPop()
            elif option=='h':
                howPop()
            elif option=='m':
                whichUser()
            elif option=='q':
                saveAndQuit(users)
                startMenu=False
                
def isPrivate(user):
    if user[-1]=='$'
        return True
    else:
        return False
def numMatches(userPrefs, allUsersPrefs):
    ''' return the number of elements that match between
    the lists userPrefs and storedUserPrefs '''
    count = 0
    for item in userPrefs:
        if item in allUsersPrefs:
            count += 1
    return count

def getRec(userPrefs, allUsersPrefs):
    max_matches = 0
    best_index = 0
    for i in range(len(allUsersPrefs)):
        curr_matches = numMatches(userPrefs, allUsersPrefs[i])
        if curr_matches > max_matches:
            best_index = i
            max_matches = curr_matches
    a = allUsersPrefs[best_index]
    for item in userPrefs:
        if item in a:
            a.remove(item)
    return a

def enter():
    L = []
    preference = 'null'
    while preference != '':
        preference = input('Enter an artist that you like (Enter to finish): ')
        L.append(preference.title())
    del L[-1]
    return L


if os.path.exists(F):
    users=getUsers(F)
else:
    write_file('',F)
    users={}
userName=input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
if userName in users.keys():
    menu(users)
else:
    artists=[]
    item=input("Enter an artist that you like (Enter to finish):\n")
    while item!='':
        artists+=[item]
        item=input("Enter an artist that you like (Enter to finish):\n")
    finalSingersList=fixSingers(artists)
    finalSingersList.sort()
    users[userName]= finalSingersList
    menu(users)
        
