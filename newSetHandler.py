import time
from checkForTypeError import checkForTypeError

def newSetHandler():
    setLength = int(input('Enter set length: '))

    newSet = []
    while len(newSet) != setLength:
        enteredNum = input('Enter number: ')
        enteredNum = enteredNum.strip()

        errorOccured = checkForTypeError(enteredNum)

        if errorOccured == False:
            newSet.append(enteredNum)
            print('Number added!')

    stringOfNewSet = ' '.join(newSet)
    print('Your set:\n' + stringOfNewSet)

    # ADDING SET TO DATABASE
    print('Adding set to our database.')
    time.sleep(1)
    print('Adding set to our database..')
    time.sleep(1)
    print('Adding set to our database...')
    time.sleep(1)

    setsDataFileHandler = open('./setsData.txt', 'a')
    setsDataFileHandler.write(stringOfNewSet)
    setsDataFileHandler.close()
    print('Set successfully added!')
