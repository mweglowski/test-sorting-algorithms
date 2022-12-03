from run_answer_input import run_answer_input

def show_ranking():
	ranking_file_handler = open("./store/ranking.txt", 'r')
	ranking_file_handler_lines = ranking_file_handler.readlines()
	ranking_file_handler_lines_length = len(ranking_file_handler_lines)
	output = ""
	if ranking_file_handler_lines_length > 0:
		for i in range(ranking_file_handler_lines_length):
			output += f'{i + 1}. {ranking_file_handler_lines[i]}\n'
	else:
		output = "[Ranking is empty]"
	
	print(output)
	print("[1] Go back")
	answer = run_answer_input()
	if answer == '1':
		from show_landing_page import show_landing_page
		show_landing_page()
	else: 
		return
