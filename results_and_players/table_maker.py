class Team(object):
	def __init__(self,name,gf=0,ga=0,gd=0,pts=0):
		self.name = name
		self.gf = gf
		self.ga = ga
		self.gd = gd
		self.pts = pts

	def add_result(self,lst):
		if self.name == lst[0]:
			self.gf = self.gf + int(lst[2][0])
			self.ga = self.ga + int(lst[2][1])
			goal_diff = int(lst[2][0]) - int(lst[2][1])
			self.gd = self.gd + goal_diff
			if goal_diff > 0:
				self.pts += 3
			elif goal_diff == 0:
				self.pts += 1


		elif self.name == lst[1]:
			self.gf = self.gf + int(lst[2][1])
			self.ga = self.ga + int(lst[2][0])
			goal_diff = int(lst[2][1]) - int(lst[2][0])
			self.gd = self.gd + goal_diff
			if goal_diff > 0:
				self.pts += 3
			elif goal_diff == 0:
				self.pts += 1

def make_table(year,file_destination = ""):
	fifa_file =file_destination + "../fifa_players/" + str(year) + "/player_and_ratings.txt"
	file = open(fifa_file,"r",encoding="utf8")
	lines = file.readline()
	file.close()
	line = eval(lines)
	result_file = file_destination + str(year) + "/results.csv"
	r_file = open(result_file,"r",encoding="windows-1252")
	results = r_file.readline()
	r_file.close()
	results = eval(results)
	teams = []
	for team in line:
		teams.append(team[0])

	team_objs = [Team(teams[i]) for i in range(0,20)]
	teams_pos = {t.name:0 for t in team_objs}
	previous_week = teams_pos
	game_index = len(results) - 1
	all_games_len = game_index

	while game_index >= 0:
		previous_week = teams_pos
		game = results[game_index]
		for team in team_objs:
			team.add_result(game)
		

		team_objs.sort(key=lambda x: (-x.pts,-x.gd,-x.gf,x.name), reverse=False)
		if game_index <= (all_games_len - 30):
			pos = 1
			for teams in team_objs:
				teams_pos[teams.name] = pos
				pos += 1 

		results[game_index] = [results[game_index][0],previous_week[results[game_index][0]],results[game_index][1],previous_week[results[game_index][1]]] + results[game_index][2:]

		game_index -= 1

		
	file_name = file_destination + str(year) + "/results_and_pos.txt"
	f_write = open(file_name,"w")
	f_write.write(str(results))
	f_write.close() 

	return team_objs




