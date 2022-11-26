from run_answer_input import run_answer_input
from choose_algorithm import choose_algorithm
from new_set_handler import new_set_handler

def show_stored_sets():
    sets_data_file_handler = open('./setsData.txt', 'r')

    lines = sets_data_file_handler.readlines()
    set_count = len(lines)
    stored_sets_string = ""
    for i in range(len(lines)):
        set_string = " ".join(lines[i].split(' ')[1:])
        stored_sets_string += str(i + 1) + '. ' + set_string
    print(stored_sets_string)

    sets_data_file_handler.close()

    # print('[1] Choose set to sort\n'
    #       '[2] Enter own set\n'
    #       '[3] Go back')
    # answer = run_answer_input()
    # match answer:
    #     case '1':
    #         # SHOWING SETS AGAIN
    #         print(stored_sets_string)
    #         from choose_set_to_sort import choose_set_to_sort
    #         choose_set_to_sort()
    #     case '2':
    #         new_set_handler()
    #     case '3':
    #         from show_landing_page import show_landing_page
    #         show_landing_page()
    #     case '_':
    #         return