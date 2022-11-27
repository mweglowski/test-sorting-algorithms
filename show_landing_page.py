from show_set_testing_page import show_set_testing_page
from run_answer_input import run_answer_input
from show_stored_sets import show_stored_sets

def show_landing_page():
    print('[1] Test some numbers\n'
          '[2] Show stored sets\n'
          '[3] Enter own set')
    answer = run_answer_input()
    match answer:
        case '1':
            show_set_testing_page()
        case '2':
            show_stored_sets()
            print('[1] Go back')
            answer = run_answer_input()
            if answer == '1': 
                show_landing_page()
            else: 
                return
        case '3':
            from new_set_handler import new_set_handler
            new_set_handler()
        case '_':
            return