#Luke Bianchi
#Project Workstation


L = []
def enter():
    preference = 'null'
    while preference != '':
        preference = input('Enter an artist that you like (Enter to finish): ')
        L.append(preference.title())
    del L[-1]
    return L

'''After the user finishes entering preferences, the database should be updated
immediately so that the other functions proceed using the new preferences.
(In memory, not saved to a file.)'''

'''After the user finishes entering preferences, they should be returned to the
menu, which should be awaiting their next choice. It should be the same after
each of the operations (except Quit), so we won’t repeat this point below.'''


#Users in private mode are exluded from getRec()
def getRec(userPrefs, allUsersPrefs):

    def numMatches(userPrefs, allUsersPrefs):
        ''' return the number of elements that match between
        the lists userPrefs and storedUserPrefs '''
        count = 0
        for item in userPrefs:
            if item in allUsersPrefs:
                count += 1
        return count


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

    



    

    
