from run_answer_input import run_answer_input

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