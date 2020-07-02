def table_maker(year):
	import sys
	sys.path.insert(0, '../results_and_players/')
	import table_maker
	team_list = []
	team_objs = table_maker.make_table(year,"../results_and_players/")
	for x in team_objs:
			team_list.append([x.name,x.pts])
	return team_list


def team_values(year,game_list_index):
	filename = "../results_and_players/" + str(year) + "/results_with_value.txt"
	f = open(filename,"r")
	f_list = f.readline()
	f.close()
	f_list = eval(f_list)
	game = f_list[game_list_index]
	team_values = [game[5],game[6]]
	return team_values	



def results_length(year):
	filename = "../results_and_players/" + str(year) + "/results_with_form.txt"
	file = open(filename,"r")
	file_list = file.readline()
	file.close()
	file_list = eval(file_list)
	len_file = len(file_list)
	return len_file

def table_length():
	filename = "../table/PLtable.txt"
	file = open(filename,"r")
	file_lines = file.readlines()
	file.close()
	return len(file_lines)

def results_player_match(year):
	unfound_list = []
	filename = "../results_and_players/" + str(year) + "/results_and_pos.txt"
	result_file = open(filename,"r",encoding="utf8")
	file = result_file.readline()
	result_file.close()
	file = eval(file)
	fifa_filename = "../fifa_players/" + str(year) + "/player_and_ratings.txt"
	fifa_file = open(fifa_filename,"r",encoding="utf8")
	f_file = fifa_file.readline()
	fifa_file.close()
	f_file = eval(f_file)
	status = False
	for i in file:
		team1 =i[-3]
		t1_name = i[0]
		team2 = i[-2]
		t2_name = i[2]
		date = i[-1]
		teams = [t1_name,t2_name]
		teams_players = [team1,team2]
		index = 0
		for team in teams:
			for fifa_team in f_file:
				if fifa_team[0] == team:
					for player in teams_players[index]:
						status = False
						for fifa_player in fifa_team[1]:
							if fifa_player[0] == player:
								status = True
								break
						if status == False:
							if [team,player] not in unfound_list:
								unfound_list.append([team,player])
			index+=1

	return unfound_list



def squad_player_match(current_year = 19):
	unfound_list = []
	filename = "../players/players.txt"
	result_file = open(filename,"r",encoding="windows-1252")
	file = result_file.readline()
	result_file.close()
	file = eval(file)
	fifa_filename = "../fifa_players/" + str(current_year) + "/player_and_ratings.txt"
	fifa_file = open(fifa_filename,"r")
	f_file = fifa_file.readline()
	fifa_file.close()
	f_file = eval(f_file)
	status = False
	for i in file:
		t_name = i[0]
		team = i[1]
		for fifa_team in f_file:
			if fifa_team[0] == t_name:
				for player in team:
					status = False
					for fifa_player in fifa_team[1]:
						if fifa_player[0] == player:
							status = True
							break
					if status == False:
						if [t_name,player] not in unfound_list:
							unfound_list.append([t_name,player])
						print(t_name,player)
	return unfound_list



def unavailable_player_match(current_year = 19):
	unfound_list = []
	filename = "../unavailable_players/unavailable.txt"
	result_file = open(filename,"r")
	file = result_file.readline()
	result_file.close()
	file = eval(file)
	fifa_filename = "../fifa_players/" + str(current_year) + "/player_and_ratings.txt"
	fifa_file = open(fifa_filename,"r")
	f_file = fifa_file.readline()
	fifa_file.close()
	f_file = eval(f_file)
	status = False
	team_names = file.keys()
	for t_name in team_names:
		team = file[t_name]
	
		for fifa_team in f_file:
			if fifa_team[0] == t_name:
				for player in team:
					status = False
					for fifa_player in fifa_team[1]:
						if fifa_player[0] == player[0]:
							status = True
							break
							
					if status == False:
						unfound_list.append(player[0])

	return unfound_list





