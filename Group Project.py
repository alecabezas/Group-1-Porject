# Group Project
"""
Alex Cabezas
Luke Bianchi
Skye Jorgensen

Pledge: "I pledge my honor that I have abided by the Stevens Honor System."

"""
user_prefs = {}
artists_count = {}
F="musicrecplus.txt"

import os.path

def fixSingers(L):
    newSingerList=[]
    for singer in L:
        newName=singer.title()
        newSingerList+=[newName]
    return newSingerList

def loadData(filename):
    """
    Creates dictinoary of all users
    """
    if not os.path.exists(filename):
        f = open(filename, 'x')
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(":")
            singersList = singers.split(",")
            finalSingersList=fixSingers(singersList)
            finalSingersList.sort()
            user_prefs[username]=finalSingersList
            #for user in user_prefs:
            if isPrivate(username)==False: 
                for art in finalSingersList:
                    if art in artists_count:
                        artists_count[art] += 1
                    else:
                        artists_count[art] = 1

def write_file(string, filename):
    myfile = open(filename, "w")
    myfile.write(string)
    myfile.close()
    
def saveAndQuit(user_prefs):
    """Updates the .txt file with new users and liked artists. Quits the program"""
    finalString=""
    for person in user_prefs.keys():
        finalString=finalString+person+":"
        for song in user_prefs[person]:
            finalString=finalString+song+','
        finalString=finalString[0:-1]+"\n"
    write_file(finalString, F)
    
def menu(userName,user_prefs):
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
                L = []
                preference = input('Enter an artist that you like (Enter to finish):\n')
                while preference != '':
                    L+=[preference]
                    preference = input('Enter an artist that you like (Enter to finish):\n')
                finalPreferences=fixSingers(L)
                finalPreferences.sort()
                user_prefs[userName]= finalPreferences
            elif option=='r':
                #print the type of getRec
                answer=getRec(userName,user_prefs)
                if answer=="No recommendations available at this time.":
                    print("No recommendations available at this time.")
                else:
                    for item in answer:
                        print(item)
            elif option=='p':
                pop=showMostPopularArtist(artists_count)
                if pop=="Sorry , no artists found.":
                    print("Sorry , no artists found.")
                else:
                    for item in pop:
                        print(item)
            elif option=='h':
                print(howPopIsMostPopArtist(artists_count))
            elif option=='m':
                print(whichUserLikesTheMostArtists(user_prefs))
            elif option=='q':
                saveAndQuit(user_prefs)
                startMenu=False
                
def isPrivate(userName):
    """"Takes in a string, if last element of string is $
    returns true for private or else false
    """
    if userName[-1]=='$':
        return True
    else:
        return False
def copyList(l):
    """
    Takes a list as input and returns a list that has the same elements
    """
    new=[]
    for item in l:
        new+=[item]
    return new

def numMatches(userPrefs, allUsersPrefs):
    ''' return the number of elements that match between
    the lists userPrefs and storedUserPrefs '''
    count = 0
    for item in userPrefs:
        if item in allUsersPrefs:
            count += 1
    return count

def getRec(userName, users):
    """Provides recomendations of artists from one other
    user that has the most in-common artists with the operating user."""
    max_matches = 0
    numDifferences=0
    nameOfBestMatch=''
    for i in users:
        if i!=userName and isPrivate(i)==False:
            curr_matches = numMatches(users[userName], users[i])
            if curr_matches > max_matches:
                numDifferences=len(users[i])-curr_matches
                nameOfBestMatch=i
                max_matches = curr_matches
    if max_matches==0 or numDifferences==0:
        return "No recommendations available at this time."
    else:
        copyListBestMatch=copyList(users[nameOfBestMatch])
        for item in users[userName]:
            if item in copyListBestMatch:
                copyListBestMatch.remove(item)
        return copyListBestMatch
def howPopIsMostPopArtist(artists_count):
    """Prints the number of likes the most popular artist recieved"""
    maxNum = 0
    maxName = ''
    for key in artists_count:
            if artists_count[key] > maxNum:
                maxNum = artists_count[key]
                maxName = key
    if maxNum==0:
        return "Sorry , no artists found."
    return artists_count[maxName]
def whichUserLikesTheMostArtists(user_prefs):
    """Prints the full name of the user who likes the most artists.
    (Has the most artists in their value list)."""
    maxNum = 0
    maxName = ''
    for key in user_prefs:
        if isPrivate(key)==False:
            if len(user_prefs[key]) > maxNum:
                maxNum = len(user_prefs[key])
                maxName = key
    if maxNum==0:
        return "Sorry, no user found."
    return maxName

def deepCopyDic(artists_count):
    newCopy={}
    for key in artists_count:
        newCopy[key]=artists_count[key]
    return newCopy
def showMostPopularArtist(artists_count):
    """Print the top 3 artists that are liked by the most users."""
    #copyArtists=deepCopyDic(artists_count)
    topArtists = []
    maxName =''
    maxNum=0
    for key in artists_count:
        if isPrivate(key)==False:
            if artists_count[key] > maxNum:
                maxNum = artists_count[key]
                maxName = key
    topArtists.append(maxName)
    if maxNum==0:
        return "Sorry , no artists found."
    maxNum=0
    for key in artists_count:
        if isPrivate(key)==False and key not in topArtists:
            if artists_count[key] > maxNum:
                maxNum = artists_count[key]
                maxName = key
    topArtists.append(maxName)
    maxNum=0
    for key in artists_count:
        if isPrivate(key)==False and key not in topArtists:
            if artists_count[key] > maxNum:
                maxNum = artists_count[key]
                maxName = key
    topArtists.append(maxName)
    return topArtists
    
    
##LOAD data
loadData(F)
userName=input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
if userName in user_prefs.keys():
    menu(userName,user_prefs)
else:
    artists=[]
    item=input("Enter an artist that you like (Enter to finish):\n")
    while item!='':
        artists+=[item]
        item=input("Enter an artist that you like (Enter to finish):\n")
    finalSingersList=fixSingers(artists)
    finalSingersList.sort()
    user_prefs[userName]= finalSingersList
    menu(userName,user_prefs)
     

