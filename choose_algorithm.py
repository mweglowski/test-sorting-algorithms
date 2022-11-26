import time
from run_answer_input import run_answer_input

def choose_algorithm():
    algorithm_paths = {
        '0': 'bubble_sort',
        '1': 'quick_sort'
    }
    answer = run_answer_input()
    file_path = algorithm_paths[str(int(answer) - 1)]
    algorithm_name = file_path.replace('_', ' ').title()
    module = __import__(file_path)

    start_time = time.time()
    module.sort_set([3, 1, 5, 1, 2, 5, 8, 321, 12, 3254, 23, 123, 123, 123, 123, 123, 123, 3425, 345, 213, 123,3, 1, 5, 1, 2, 5, 8, 321, 12, 3254, 23, 123, 123, 123, 123, 123, 123, 3425, 345, 213, 123,3, 1, 5, 1, 2, 5, 8, 321, 12, 3254, 23, 123, 123, 123, 123, 123, 123, 3425, 345, 213, 123,3, 1, 5, 1, 2, 5, 8, 321, 12, 3254, 23, 123, 123, 123, 123, 123, 123, 3425, 345, 213, 123,3, 1, 5, 1, 2, 5, 8, 321, 12, 3254, 23, 123, 123, 123, 123, 123, 123, 3425, 345, 213, 123,3, 1, 5, 1, 2, 5, 8, 321, 12, 3254, 23, 123, 123, 123, 123, 123, 123, 3425, 345, 213, 123,3, 1, 5, 1, 2, 5, 8, 321, 12, 3254, 23, 123, 123, 123, 123, 123, 123, 3425, 345, 213, 123])
    duration = time.time() - start_time
    print('Duration: {}'.format(duration))

    # get id of set
    # get set
    # get algorithm name +
    # get time of execution +


