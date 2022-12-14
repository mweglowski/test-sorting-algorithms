import timeit
import sys
import importlib
from run_answer_input import run_answer_input
from show_algorithms import show_algorithms

sys.path.append('c:\\Learning\\clean\\projects\\python-sorting-app\\algorithms')

def choose_algorithm():
    algorithm_paths = {
        '0': 'bubble_sort',
        '1': 'quick_sort',
        '2': 'insertion_sort',
        '3': 'bucket_sort',
        '4': 'selection_sort',
        '5': 'merge_sort',
    }
    answer = run_answer_input()
    file_name = algorithm_paths[str(int(answer) - 1)]
    module = importlib.import_module(file_name)

    # GET THE SELECTED SET
    selected_set_file_handler = open('./store/selected_set.txt', 'r')
    # list of strings
    selected_set_string = selected_set_file_handler.read()
    selected_set = selected_set_string.split()[1:]
    # formatting to list of integers
    selected_set = [int(string_num) for string_num in selected_set]

    # Sorting operation
    start_time = timeit.default_timer()
    module.sort_set(selected_set)
    duration = timeit.default_timer() - start_time
    # 1ms = 0.001s
    # 1µs = 0.000001s
    duration_result_string = ''
    if duration < 0.000001:
        duration_result_string = f'{round(duration * 1000000)}µs'
    elif duration >= 0.000001 and duration < 0.001:
        duration_result_string = f'{round(duration * 1000000)}µs'
    elif duration >= 0.001 and duration < 1:
        duration_result_string = f'{round(duration * 1000)}ms'
    else:
        duration_result_string = f'{round(duration, 3)}s'

    print('Sorted Set: ', end='')
    print(module.sort_set(selected_set))
    print('Duration Time: {}'.format(duration_result_string))

    # SAVING OPERATION TO algorithm_results.txt
    alg_results_file_handler = open("./store./algorithm_results.txt", 'a+') 
    set_id = selected_set_string.split(' ')[0]
    chosen_set = " ".join(selected_set_string.split(' ')[1:])
    algorithm_name = file_name.replace('_', ' ').title()
    duration_in_ms = f'{round(duration * 1000, 6)}' + 'ms'
    next_sorting_result = f'[{set_id}] [{chosen_set}] [{algorithm_name}] [{duration_in_ms}]\n'
    alg_results_file_handler.write(next_sorting_result)
    alg_results_file_handler.close()

    # ADDING RESULT TO ranking.txt
    ranking_file_handler = open("./store/ranking.txt", "r")
    set_length = len(selected_set_string.split(' ')[1:])
    execution_time_in_ms = round(duration * 1000, 6)
    points = round(set_length / execution_time_in_ms)
    ranking_item = f'[{points}] [{algorithm_name}] [{duration_in_ms}] [{set_id}] [{chosen_set}]\n'
    ranking_file_handler_lines = ranking_file_handler.readlines()
    ranking_file_handler_lines_length = len(ranking_file_handler_lines)
    ranking_file_handler.close()
    

    if ranking_file_handler_lines_length < 1:
        ranking_file_handler = open('./store/ranking.txt', 'w')
        ranking_file_handler.write(ranking_item)
        ranking_file_handler.close()
    else:
        ranking_file_handler = open('./store/ranking.txt', 'w')
        for i in range(ranking_file_handler_lines_length):
            current_item = ranking_file_handler_lines[i]
            current_item_points = int(current_item.split(' ')[0][1:-1])
            if current_item_points < points:
                ranking_file_handler_lines.insert(i, ranking_item)
                break
        ranking_file_handler.writelines(ranking_file_handler_lines)

    ranking_file_handler.close()



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



