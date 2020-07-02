from datetime import datetime


filename = "fixtures.csv"
fixt_file = open(filename,"r")
player_file = open("../players/players.txt","r",encoding="windows-1252")
player_file = player_file.readline()
player_file = eval(player_file)
unavail_file = open("../unavailable_players/unavailable.txt")
unavail_file = unavail_file.readline()
unavail_file = eval(unavail_file)
table_file = open("../table/PLtable.txt")
table_file = table_file.readlines()


fifa_file = open("../fifa_players/19/player_and_ratings.txt")
fifa_file = fifa_file.readline()
fifa_file = eval(fifa_file)

fixt_file  = fixt_file.readlines()
fixt_file = fixt_file[1:]

form_file = open("../results_and_players/19/results_with_form.txt")
form_file = form_file.readline()
form_file = eval(form_file)

overall_stats = "home_pos,home_value,home_score_form,home_concede_form,away_pos,away_value,away_score_form,away_concede_form\n"

for game in fixt_file:
	game = game.strip()
	game = game.split(",")
	match_date = game[0].strip()
	match_date = match_date.split()
	match_date = "{} {:0>2} {} {}".format(match_date[0],match_date[1],match_date[2],match_date[3])
	date = datetime.strptime(match_date, '%A %d %B %Y')
	home_team = game[1].strip()
	away_team = game[2].strip()
	teams = [home_team,away_team]
	stats = []
	for team in teams:
		for team_squad in player_file:
			if team_squad[0] == team:
				available_squad = team_squad[1]
				if(team in unavail_file.keys()):
					for injured_player in unavail_file[team]:
						return_date = injured_player[1]
						return_chance = injured_player[-1]
						if(return_date == "No Return Date" or return_date > match_date or injured_player[-1] != "100%"):
							if injured_player[0] in available_squad:
								available_squad.remove(injured_player[0])
				for fifa_team in fifa_file:
					if fifa_team[0] == team:
						overall_value = []
						for fifa_player in fifa_team[1]:
							if fifa_player[0] in available_squad:
								overall_value.append(int(fifa_player[1]))
						overall_value = sorted(overall_value,reverse=True)
						overall_value = sum(overall_value[:18])
				pos = 0
				while pos < len(table_file):
					table_row = table_file[pos].split(",")
					if table_row[0] == team:
						break
					pos+=1
				pos = pos + 1
				
				gs = 0
				gc = 0
				num_games = 0
				for result in form_file:
					if num_games == 3:
						break
					if result[0] == team:
						gs += int(result[4][0])
						gc += int(result[4][1])
						num_games += 1

					elif result[2] == team:
						gs += int(result[4][1])
						gc += int(result[4][0])
						num_games += 1  
				stats += [str(pos),str(overall_value),str(gs),str(gc)]
	stats = ",".join(stats)
	overall_stats += stats + "\n"
file_write = open("test_games.csv","w")
file_write.write(overall_stats)
# print(overall_stats)
