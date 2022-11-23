from generateSetsOfNumbers import generateSetsOfNumbers
from newSetHandler import newSetHandler

# RUNNING BEFORE START OF AN APPLICATION
generateSetsOfNumbers(10, 7)

def runAnswerInput():
    answer = input('Your answer: ')
    print('\n')
    return answer

def runApp():
    showLandingPage()

def showLandingPage():
    print('[1] Sorting\n'
          '[2] Show default sets\n'
          '[3] Enter new set')
    answer = runAnswerInput()
    if answer == '1':
        showSortingPage()

def showSortingPage():
    print('[1] Enter own set of numbers\n'
          '[2] Choose default one')
    answer = runAnswerInput()
    if answer == '1':
        newSetHandler()
    elif answer == '2':
        print(2)


runApp()