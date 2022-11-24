def show_stored_sets():
    sets_data_file_handler = open('./setsData.txt', 'r')

    lines = sets_data_file_handler.readlines()
    set_count = len(lines)
    print(" ".join(lines))

    sets_data_file_handler.close()
