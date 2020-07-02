from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import sys


unavailable_url = "https://www.premierinjuries.com/injury-table.php"
unavailable_html = uReq(unavailable_url)
unavalable_soup = soup(unavailable_html,"html.parser")
table = unavalable_soup.find("table",{"class":"injury-table"})
teams_details = table.findAll("a",{"data-type":"team"})
teams_ids = []

for i in teams_details:
	name = i.attrs["data-name"]
	team_id = i.attrs["data-id"] 
	teams_ids.append((name,team_id))
teams_and_players = {team[0]:[] for team in teams_ids}


for team in teams_ids:
	tag_data = "player-row team_" + str(team[1])
	players = table.findAll("tr",{"class":tag_data})
	teams_and_players[team[0]] = players

for team in teams_and_players.keys():
	players_list = []
	for player in teams_and_players[team]:
		player_details = player.findAll("td")
		player_details = [str(player_details[0]),str(player_details[3]),str(player_details[5])]
		details = []

		for detail in player_details:
			detail = detail.split("</div>")
			detail = detail[1][:-5]
			details.append(detail)
		players_list.append(details)
	teams_and_players[team] = players_list

filename = "unavailable.txt"
f = open(filename,"w")
f.write(str(teams_and_players))

print(teams_and_players)


