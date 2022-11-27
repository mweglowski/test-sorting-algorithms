import time
from check_for_type_error import check_for_type_error
from run_answer_input import run_answer_input
from show_algorithms import show_algorithms
from choose_algorithm import choose_algorithm

def new_set_handler():
    set_length = int(input('Enter set length: '))

    new_set = []
    while len(new_set) != set_length:
        entered_num = input('Enter number: ')
        entered_num = entered_num.strip()

        error_occured = check_for_type_error(entered_num)

        if not error_occured:
            new_set.append(entered_num)
            print('Number added!')

    new_set_string = ' '.join(new_set)
    print('Your set:\n' + new_set_string)

    # ADDING SET TO DATABASE
    print('Adding set to our database', end='')
    time.sleep(.8)
    print('.', end='')
    time.sleep(.8)
    print('.', end='')
    time.sleep(.8)
    print('.')
    time.sleep(.8)

    with open('./setsData.txt', 'r+') as sets_data_file_handler:
        lines = sets_data_file_handler.readlines()
        next_set_id = len(lines)
        new_set_string = f'{next_set_id}m ' + new_set_string + '\n'
        sets_data_file_handler.write(new_set_string)

    print('Set successfully added!\n'
          '[1] Go to home page\n'
          '[2] Choose algorithm to sort this set')
    answer = run_answer_input()
    if answer == '1':
        from show_landing_page import show_landing_page
        show_landing_page()
    elif answer == '2':
        show_algorithms()
        choose_algorithm()
    else:
        return

