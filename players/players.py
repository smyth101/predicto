from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_options=options ,firefox_binary=binary)

driver.get("https://www.premierleague.com/players?se=210")
time.sleep(2)
teams_html = driver.page_source
driver.close()
teams_soup = soup(teams_html,"html.parser")

teams_id = {}
teams_lst = teams_soup.find("ul",{"data-dropdown-list":"clubs"})
teams_details = teams_lst.findAll("li")
teams_details  = teams_details[1:]
for team in teams_details:
	name = team.attrs["data-option-name"]
	name_id = team.attrs["data-option-id"]
	teams_id[name] = name_id

teams_and_players = []
for team in teams_id.keys():
	team_url = "https://www.premierleague.com/players?se=210&cl=" + str(teams_id[team])
	driver = webdriver.Firefox(firefox_options=options ,firefox_binary=binary)
	driver.get(team_url)
	time.sleep(4)
	team_html = driver.page_source
	driver.close()
	team_soup = soup(team_html,"html.parser")
	players = []
	player_table = team_soup.find("table")
	player_names = player_table.findAll("a",{"class":"playerName"})
	for name in player_names:
		name = name.text
		players.append(name)
	team_and_players = [team,players]
	print(players)
	teams_and_players.append(team_and_players)

file = open("players.txt","w")
file.write(str(teams_and_players))
file.close()