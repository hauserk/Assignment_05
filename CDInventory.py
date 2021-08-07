#----------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# KHauser, 2021-Aug-03, Modified File
# KHauser, 2021-Aug-07, Cleanup for submission
#----------------------------------------------#

# Declare variables
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = []  # specific list row
dictRow = {} # dict for row data
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 2. Exit the program if the user chooses 'x'
        break
    
    
    if strChoice == 'l':
        # 3. Read file from .txt file if the user chooses 'l'
        objFile = open(strFileName, 'r')
        
        # Loop through data rows in .txt file and parse data into list of dicts
        for row in objFile:
            lstRow = row.strip().split(',')  # comma seperated sections into list elements
            dictRow = {'id':lstRow[0],'album':lstRow[1],'artist':lstRow[2]}
            lstTbl.append(dictRow) # append dict to list
        
        # Print user message and close file
        print('Data loaded from file\n')
        objFile.close()
    
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 4. Add data to the table (2d-list) each time the user selects 'a'
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)

        # Store input in dict and append to list of dicts
        dictRow = {'id':intID,'album':strTitle,'artist':strArtist}
        lstTbl.append(dictRow)
        
        
    elif strChoice == 'i':
        # 5. Display the current data to the user each time the user wants to display the data 'i'
        print('ID, CD Title, Artist')
        
        # Loop through dicts in list and display value associated with key
        for row in lstTbl:
            print(str(row['id']) + ', ' + str(row['album']) + ', ' + str(row['artist']))
        print()
            
            
    elif strChoice == 'd':
        # 6. Delete album and artist data from inventory on matched ID
        intDelID = input('Enter an ID to delete: ')
                    
        # Loop through list until ID matches on ID to delete entered
        for i in range(len(lstTbl)):
            if int(lstTbl[i]['id']) == int(intDelID):
                del lstTbl[i]
                break
        pass
    
    
    elif strChoice == 's':
        # 7. Save the data to a text file CDInventory.txt if the user chooses 's'
        # Open file to write over existing file data
        objFile = open(strFileName, 'w')
        
        # Loop through list of dicts and write dict elements as comma seperated
        for i in range(len(lstTbl)):
            objFile.write(str(lstTbl[i]['id']) + ',' + lstTbl[i]['album'] + ',' + lstTbl[i]['artist'] + '\n')
            
        # Exit program setting control variable to zero to stop loop
        print('Your data has been saved.\n')
        objFile.close()
        
        
    else:
        # 8. Error message if user chooses a letter other than listed
        print('Please choose either l, a, i, d, s or x!')

