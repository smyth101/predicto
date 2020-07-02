from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url_start = "https://www.futhead.com/"
year = 19
while year >= 19:
    filename = str(year) + "/player_and_ratings.txt"
    f = open(filename,"w")
    teams = []
    team_names = []
    year_url = url_start + str(year) + "/players/?league=13"
    req = Request(year_url, headers={'User-Agent': 'Mozilla/5.0'})
    uClient = urlopen(req)
    html_page = uClient.read()
    uClient.close()
    #scrape pages data
    soup_page = soup(html_page,"html.parser")
    drops = soup_page.findAll("li",{"class":"dropdown dropdown-hover hidden-xs"})
    team_drop = drops[2]
    teams_data = team_drop.findAll("a",{"data-preserve-attr":"club"})
    teams_id = []
    for i in teams_data:
        team_name = i.text
        team_name = team_name.strip()
        #remove eror in sites team listing
        if team_name != "The Journey":
            teams_id.append(i.attrs["data-preserve-value"])
            team_names.append(team_name)
    team_name_index = 0
    #go through the 20 teams
    for team in teams_id:
        all_players = []
        team_url = year_url + "&club=" + team
        #go through each position
        pos = ["gk","def","mid","att"]
        for i in pos:
            levels = ["all_nif","transfer"]
            for level in levels:
                pos_url = team_url + "&group=" + i + "&level=" + level
                req = Request(pos_url, headers={'User-Agent': 'Mozilla/5.0'})
                uClient = urlopen(req)
                pos_html_page = uClient.read()
                uClient.close()
                #scrape page for team with position filter
                soup_team = soup(pos_html_page,"html.parser")


                player_details = soup_team.findAll("span",{"class":"player-info"})
                players = []
                for details in player_details:
                    player_name = details.find("span",{"class":"player-name"}).text
                    score = details.find("img",{"class":"player-image"})
                    score = score.attrs["alt"]
                    score = score[-2:]
                    
                    j = 0
                    while j < len(all_players):
                        #if player has a second higher rated card update player value
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

                    name_score = (player_name,score)
                    players.append(name_score) 
                
                all_players = all_players + players
                team_and_players = [team_names[team_name_index],all_players]
        teams.append(team_and_players)
        team_name_index += 1

    f.write(str(teams))

    year = year -1
    if year == 13:
        year = year -1
