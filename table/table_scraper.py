from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

name_mapping = {
	"Bournemouth" : "AFC Bournemouth"
}

table_url = "https://www.premierleague.com/tables"
uClient = uReq(table_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

filename = "PLtable.txt"
f = open(filename,"w")

teams = page_soup.findAll("tr",{"data-compseason":"210"})
pos = 1
for team in teams:
	name = team.find("span",{"class":"long"}).text
	points = team.find("td",{"class":"points"}).text
	stats = team.findAll("td",{"class":False})
	stats = stats + team.findAll("td",{"class":"hideSmall"})
	i = 0
	while i < len(stats):
		stats[i] = stats[i].text
		i+=1
	tmp = stats[-3]
	stats[-3] = stats[-1]
	stats[-1] = tmp
	tmp = stats[-2]
	stats[-2] = stats[-3]
	stats[-3] = tmp
	rest_stats = ""
	for stat in stats:
		rest_stats += stat + ","
	rest_stats = rest_stats[:-1]

	if name in name_mapping.keys():
		name = name_mapping[name]
	f.write(name + ", " + str(pos) + "," + rest_stats + "," + points + "\n" )
	pos+=1
f.close()