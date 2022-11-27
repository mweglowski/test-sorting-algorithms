import random

def generate_sets_of_numbers(numOfSets, setLength):
    file = open('./store/stored_sets.txt', 'w')

    sets = []
    for i in range(numOfSets):
        num_set = [f'{i}d']
        for j in range(setLength):
            num_set.append(str(random.randint(0, 1000)))
        sets.append(num_set)

    sets_string = ""
    for item in sets:
        item = " ".join(item)
        sets_string += item + '\n'

    file.write(sets_string)
    file.close()


