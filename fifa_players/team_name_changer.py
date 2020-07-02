def name_changer(year):
	change = {
		"Bournemouth":"AFC Bournemouth",
		"Brighton & Hove Albion": "Brighton and Hove Albion",
		"Newcastle Utd": "Newcastle United",
		"Spurs": "Tottenham Hotspur",
		"Manchester Utd": "Manchester United",
		"West Brom": "West Bromwich Albion",
		"West Ham":"West Ham United",
		"QPR":"Queens Park Rangers",
		"wigan Athletic":"Wigan Athletic"
	}
	file =  str(year) + "/player_and_ratings.txt"
	fifa_file = open(file,"r",encoding="utf8")
	line = fifa_file.readline()
	lst = eval(line)
	for i in lst:
		if i[0] in change.keys():
			i[0] = change[i[0]]
			print(i)
	f = "../fifa_players/" + str(year) +  "/player_and_ratings.txt"
	file = open(f,"w",encoding="utf8")
	file.write(str(lst))
			


for i in range(10,20):
	name_changer(i)