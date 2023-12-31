def createFile(fileName, fileHeading):
    file = open(fileName + '.txt', 'w')
    file.write(fileHeading + '\n')
    file.close()

def addEntry(fileName, company, username, email, password):
    file = open(fileName + '.txt', 'a')
    file.write('\n')
    file.write(company + '\n')
    file.write("Username: " + username + '\n')
    file.write("Email: " + email + '\n')
    file.write("Password: " + password + '\n')
    file.close()

def sortFunction(nestedList):
    return sorted(nestedList, key = lambda sublist: sublist[0])

def sortEntry(fileName):
    file = open(fileName + '.txt', 'r')

    entries = file.read()
    entries = entries.split('\n')
    entryHeading = entries[0]

    sortedEntries = []
    for i in entries:
        if i == '':
            entries.remove(i)
    for i in range(1, len(entries), 4):
        if entries[ i : i + 4 : ] != ['']:
            sortedEntries += [entries[ i : i + 4 : ]]

    x = (sortFunction(sortedEntries))
    return entryHeading, x

def listEntry(fileName):
    file = open(fileName + '.txt', 'r')

    entries = file.read()
    entries = entries.split('\n')
    for i in entries:
        if i == '':
            entries.remove(i)
    for i in range(1, len(entries), 4):
        if entries[ i : i + 4 : ] != ['']:
            print(entries[ i : i + 4 : ])

def main():

    import os

    os.chdir('/Users/larryyang/Desktop')
    
    choiceOne = ''
    while choiceOne != "q":

        choiceOne = input('(c)reate a file, (s)elect a file to modify, or (q)uit: ')

        if choiceOne == 'c':
            fileName = input("Please enter the name of the file you wish to create: ")
            heading = input("Please enter the desired document heading: ")
            createFile(fileName, heading)
            print("File created!")

        elif choiceOne == 's':
            fileModify = input("Please enter the name of the file you wish to modify: ")
            
            if os.path.isfile(fileModify + '.txt'):

                choiceTwo = ''
                while choiceTwo != "r":

                    choiceTwo = input('(a)dd an entry, (l)ist existing entries, (s)ort existing entries, or (r)eturn to main menu: ')

                    if choiceTwo == 'a':
                        fileName = fileModify
                        company = input("Website/Company: ")
                        username = input("Username: ")
                        email = input("Email: ")
                        password = input("Password: ")
                        addEntry(fileName, company, username, email, password)
                        print("Entry added!")
                        print()

                    elif choiceTwo == 'l':
                        fileName = fileModify
                        listEntry(fileName)
                        print()

                    elif choiceTwo == 's':
                        fileName = fileModify
                        heading, sortedList = sortEntry(fileName)

                        choiceThree = input("Would you like to overwrite the current file with sorted entries (y/n)? ")

                        if choiceThree == 'y':
                            file = open(fileName + '.txt', 'w')
                            file.write(heading + '\n')
                            file.write('\n')

                            for sublist in sortedList:
                                for l in sublist:
                                    
                                    file.write(l + '\n')
                                file.write('\n')
                                
                            
                            file.close()
                            print("Document sorted!")
                        else:
                            break
                        print()
            else:
                print("Specified file not found.")
                break

        print()
main()
    
