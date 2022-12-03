# import os
from show_set_testing_page import show_set_testing_page
from run_answer_input import run_answer_input
from show_stored_sets import show_stored_sets
from show_algorithms import show_algorithms
from show_ranking import show_ranking

def show_landing_page():
    print('[1] Test some numbers\n'
          '[2] Algorithms\n'
          '[3] Stored sets\n'
          '[4] Ranking\n'
          '[4] Enter own set\n'
          '[5] Exit')
    answer = run_answer_input()
    match answer:
        case '1':
            show_set_testing_page()
        case '2':
            show_algorithms()
            # algorithm_count = len(os.listdir('./algorithms')) - 1
            # print('-' * 15)
            # print(f'[{algorithm_count + 1}] Go back')
            print('[1] Go back')
            answer = run_answer_input()
            if answer == '1': 
                show_landing_page()
            else: 
                return
            # if answer == f'{algorithm_count + 1}': 
            #     show_landing_page()
            # else: 
            #     return
                
        case '3':
            show_stored_sets()
            print('[1] Go back')
            answer = run_answer_input()
            if answer == '1': 
                show_landing_page()
            else: 
                return
        case '4':
            show_ranking()
        case '5':
            from new_set_handler import new_set_handler
            new_set_handler()
        case '6':
            print('See you again!')
            exit()
        case '_':
            return