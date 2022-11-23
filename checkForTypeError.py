def checkForTypeError(answer):
    try:
        answer = int(answer)
        answer = str(answer)
    except:
        print('Error', answer, 'is not a number.')
        return True
    return False