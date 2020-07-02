def team_value(year):
	fifa_file  = "../fifa_players/" + str(year) + "/player_and_ratings.txt"
	f_file = open(fifa_file,"r",encoding = "utf8")
	result_file =  str(year) + "/results_and_pos.txt"
	r_file = open(result_file,"r",encoding = "utf8")
	f_file = f_file.readline()
	f_file = eval(f_file)
	r_file = r_file.readline()
	r_list = eval(r_file)

	for game in r_list:
		home_value = 0
		away_value = 0
		home_team = game[-3]
		home_name = game[0]
		fifa_home_team = []
		for team in f_file:
			if team[0] == home_name:
				fifa_home_team = team[1]
				break
		for player in home_team:
			for (k,v) in fifa_home_team:
				if k == player:
					home_value+=int(v)
					break
		print(home_team,home_value)
		game[-3] = home_value

		away_team = game[-2]
		away_name = game[2]
		fifa_away_team = []
		for team in f_file:
			if team[0] == away_name:
				fifa_away_team = team[1]
				break


		for player in away_team:
			for (k,v) in fifa_away_team:
				if k == player:
					away_value+=int(v)
					break

		print(away_team,away_value)
		game[-2] = away_value
	file_name = str(year) + "/results_with_value.txt"
	file_write = open(file_name,"w")
	file_write.write(str(r_list))
	file_write.close()


for i in range(10,20):
	team_value(i)