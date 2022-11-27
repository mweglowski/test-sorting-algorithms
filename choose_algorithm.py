import time
from run_answer_input import run_answer_input
from show_algorithms import show_algorithms

def choose_algorithm():
    algorithm_paths = {
        '0': 'bubble_sort',
        '1': 'quick_sort'
    }
    answer = run_answer_input()
    file_path = algorithm_paths[str(int(answer) - 1)]
    algorithm_name = file_path.replace('_', ' ').title()
    module = __import__(file_path)

    # GET THE SELECTED SET
    selected_set_file_handler = open('./selected_set.txt', 'r')
    # list of strings
    selected_set = selected_set_file_handler.read().split()[1:]
    # formatting to list of integers
    selected_set = [int(string_num) for string_num in selected_set]
    print(selected_set)

    # Sorting operation
    start_time = time.time()
    module.sort_set(selected_set)
    duration = time.time() - start_time

    print('Sorted: ', end='')
    print(module.sort_set(selected_set))
    print('Duration: {}'.format(duration))

    print('[1] Try another algorithm\n'
          '[2] Choose different set\n'
          '[3] Go to home page')
    answer = run_answer_input()
    match answer:
        case '1':
            show_algorithms()
            choose_algorithm()
        case '2':
            from show_stored_sets import show_stored_sets
            show_stored_sets()
            from choose_set_to_sort import choose_set_to_sort
            choose_set_to_sort()
        case '3':
            from show_landing_page import show_landing_page
            show_landing_page()
        case '_':
            return



