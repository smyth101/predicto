def results_with_form(year):
	filename = str(year) + "/results_with_value.txt"
	results_file = open(filename,"r")
	results_file = results_file.readline()
	results_file = eval(results_file)

	fifa_file = "../fifa_players/"+ str(year) + "/player_and_ratings.txt"
	f_file = open(fifa_file,"r")
	f_file = f_file.readline()
	f_file = eval(f_file)
	form = {team[0]:[] for team in f_file}
	form_value = {team[0]:[] for team in f_file}

	game_index = len(results_file) - 1
	while game_index >= 0:

		game = results_file[game_index]
		form_results = []
		for team_index in range(0,2):
			form_score_value = 0
			form_conceded_value = 0
			if team_index == 1:
				team_index = 2
			t_name = game[team_index]
			score = game[4]
			if team_index == 2:
				score = [score[1],score[0]]
			if len(form[t_name]) == 8:
				form[t_name] = form[t_name][:-2]
			form[t_name] = score + form[t_name]
			
			goal_index = 2
			conceded_index = 3
			while goal_index < len(form[t_name]):
				form_score_value += int(form[t_name][goal_index])
				form_conceded_value += int(form[t_name][conceded_index])
				goal_index += 2
				conceded_index += 2
			form_value[t_name] = [form_score_value,form_conceded_value]
			form_results.append(form_value[t_name])
		date = results_file[game_index][-1]
		results_file[game_index] = results_file[game_index][:-1] + form_results
		results_file[game_index].append(date)

		game_index -= 1
	print(form)
	print(form_value)
	file_name = str(year) + "/results_with_form.txt"
	file_write = open(file_name,"w")
	print(results_file)
	file_write.write(str(results_file))
	file_write.close()





for i in range(10,20):
	results_with_form(i)