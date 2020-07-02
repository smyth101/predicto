def create_training_file():
	file_data = "home_pos,home_value,home_score_form,home_concede_form,away_pos,away_value,away_score_form,away_concede_form,home_result_score,away_result_score\n"
	for i in range(10,20):
		year = i
		filename = str(year) + "/results_with_form.txt"
		file = open(filename,"r")
		file = file.readline()
		file = eval(file)
		for line in file:
			row = str(line[1]) +"," + str(line[5]) +"," + str(line[7][0]/3) + "," + str(line[7][1]) + "," + str(line[3]) +"," + str(line[6]) +"," + str(line[8][0]) + "," + str(line[8][1]) + "," + line[4][0] + "," + line[4][1] + "\n" 
			file_data += row
	file_name = "training_results.csv"
	f = open(file_name,"w")
	f.write(file_data)


create_training_file()