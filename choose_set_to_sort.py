from run_answer_input import run_answer_input
from show_algorithms import show_algorithms
from show_stored_sets import show_stored_sets

def choose_set_to_sort():
    sets_data_file_handler = open('./setsData.txt', 'r')
    lines = sets_data_file_handler.readlines()

    answer = run_answer_input()

    set_to_show = " ".join(lines[int(answer) - 1].split()[1:])
    print('Selected Set: ' + set_to_show)

    sets_data_file_handler.close()
    # SETTING SELECTED SET STATE
    with open('./selected_set.txt', 'w') as selected_set_file_handler:
        set_id = lines[int(answer) - 1].split()[0]
        set_id_and_contents = set_id + ' ' + set_to_show
        selected_set_file_handler.write(set_id_and_contents)

    print('[1] Choose algorithm\n'
          '[2] Select other set\n'
          '[3] Go back to home page')
    answer = run_answer_input()
    if answer == '1':
        show_algorithms()
    elif answer == '2':
        show_stored_sets()
        choose_set_to_sort()
    elif answer == '3':
        from show_landing_page import show_landing_page
        show_landing_page()
    else:
        return