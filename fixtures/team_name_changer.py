def name_changer():
	change = {
		"Bournemouth":"AFC Bournemouth",
		"Brighton": "Brighton and Hove Albion",
		"Newcastle": "Newcastle United",
		"Spurs": "Tottenham Hotspur",
		"Man Utd": "Manchester United",
		"Man City": "Manchester City",
		"Wolves":"Wolverhampton Wanderers",
		"Huddersfield": "Huddersfield Town",
		"West Brom": "West Bromwich Albion",
		"West Ham":"West Ham United",
		"Leicester" : "Leicester City",
		"Cardiff" : "Cardiff City"
	}
	file =  "fixtures.csv"
	fixtures = open(file,"r")
	fixtures = fixtures.readlines()
	index = 0
	while index <  len(fixtures):
		fixtures[index] = fixtures[index].split(",")
		if fixtures[index][-2].strip() in change.keys():
			fixtures[index][-2] = change[fixtures[index][-2].strip()]
			

		if fixtures[index][-1].strip() in change.keys():
			fixtures[index][-1] = change[fixtures[index][-1].strip()]
			fixtures[index][-1] += "\n"



		fixtures[index] = ",".join(fixtures[index])
		
		index += 1
	full_fixtures = "".join(fixtures)
	print(full_fixtures)
	f = "fixtures.csv"
	file = open(f,"w")
	file.write(str(full_fixtures))
			


name_changer()