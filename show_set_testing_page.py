from run_answer_input import run_answer_input
from show_stored_sets import show_stored_sets
from new_set_handler import new_set_handler
from choose_set_to_sort import choose_set_to_sort
from choose_algorithm import choose_algorithm

def show_set_testing_page():
    print('[1] Enter own set of numbers\n'
          '[2] Choose default one')
    answer = run_answer_input()
    if answer == '1':
        new_set_handler()
    elif answer == '2':
        show_stored_sets()
        choose_set_to_sort()
        choose_algorithm()