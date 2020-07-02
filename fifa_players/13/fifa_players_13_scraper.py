from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import io

url_start = "https://www.futhead.com/"

filename = "player_and_ratings.txt"
team_names = ["Arsenal","Aston Villa","Chelsea","Everton","Fulham","Liverpool","Manchester City","Manchester United","Newcastle United","Norwich City","Southampton","Stoke City","Sunderland","Swansea City","Tottenham Hotspur","West Bromwich Albion","West Ham United","wigan Athletic","Queens Park Rangers","Reading"]
year_url = url_start + "13" + "/players/?league=13"
teams_id = [1,2,5,7,144,9,10,11,13,1792,17,1806,106,1960,18,109,19,1917,15,1793]
teams = []
team_name_index = 0
for team in teams_id:
    all_players = []
    team_url = year_url + "&club=" + str(team)
    pos = ["gk","def","mid","att"]
    for i in pos:
         levels = ["all_nif","transfer"]
         for level in levels:
            pos_url = team_url + "&group=" + i + "&level=" + level
            pos_url = team_url + "&group=" + i + "&level=all_nif"
            req = Request(pos_url, headers={'User-Agent': 'Mozilla/5.0'})
            uClient = urlopen(req)
            pos_html_page = uClient.read()
            uClient.close()
            soup_team = soup(pos_html_page,"html.parser")


            player_details = soup_team.findAll("span",{"class":"player-info"})
            players = []
            for details in player_details:
                player_name = details.find("span",{"class":"player-name"}).text
                score = details.find("img",{"class":"player-image"})
                score = score.attrs["alt"]
                score = score[-2:]
                
                #change
                j = 0
                while j < len(all_players):
                    if player_name == all_players[j][0]:
                        if int(all_players[j][1]) > int(score):
                            score = all_players[j][1]
                        all_players.remove(all_players[j])
                    j+=1
                j = 0
                while j < len(players):
                    if player_name == players[j][0]:
                        if int(players[j][1]) > int(score):
                            score = players[j][1] 
                        players.remove(players[j])
                    j+=1
                #change end
                name_score = (player_name,score)
                players.append(name_score) 
            
            all_players = all_players + players
            team_and_players = [team_names[team_name_index],all_players]
    teams.append(team_and_players)
    team_name_index += 1
teams = str(teams)
with io.open(filename,"w",encoding="utf-8") as f:
    f.write(teams)
# print(teams)

