from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as soup


header = "date,home,home_score,away,away_score\n"
options = Options()
options.add_argument("--headless")

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

driver = webdriver.Firefox(firefox_options=options ,firefox_binary=binary)

driver.get("https://www.premierleague.com/results")
time.sleep(2)
result_years_html = driver.page_source
driver.close()
soup_years = soup(result_years_html,"html.parser")
years_id_html = soup_years.find("ul",{"data-dropdown-list":"compSeasons"})
years_list_html = years_id_html.findAll("li")
year_ids = []
start_year_list_index = 0
end_year_list_index = 1
current_year = 19 #year for current updates of results
file_year = 19 - start_year_list_index
years_list_html = years_list_html[start_year_list_index:end_year_list_index] #gets the last 10 years
for i in years_list_html:
    value = i.attrs["data-option-id"]
    year_ids.append(value)



base_url =  "https://www.premierleague.com/results"
for i in year_ids:
    if current_year == file_year:
        try:
            file_name = str(current_year) + "/results.csv"
            file = open(file_name,"r")
            last_file = file.readline()
            last_file = eval(last_file)
            latest_game = last_file[0]
        except FileNotFoundError:
            latest_game = "new"

    else:
        latest_game = "new"
    

    filename =  str(file_year) + "/results.csv"
    f = open(filename,"w")
    year_games_list = []
    year_url = base_url + "?se=" + i
    driver = webdriver.Firefox(firefox_options=options ,firefox_binary=binary)
    driver.get(year_url)
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    page_html = driver.page_source
    driver.close()
    page_soup = soup(page_html,"html.parser")
    mathes = page_soup.findAll("li",{"class":"matchFixtureContainer"})
    match_urls = []
    for match in mathes:
        match_div = match.find("div")
        match_url = match_div.attrs["data-href"]
        match_url = "https:" + match_url[2:]
        match_urls.append(match_url)


    for game in match_urls:

        driver = webdriver.Firefox(firefox_options = options,firefox_binary=binary)
        driver.get(game)
        if file_year >= 10 and file_year <= 13:
            time.sleep(5)
            line_up = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[1]/div/div/ul/li[2]')
            time.sleep(4)
            line_up.click()
        time.sleep(2)
        lineup_html = driver.page_source
        driver.close()
        soup_lineup = soup(lineup_html,"html.parser")

        
        home_team = soup_lineup.find("div",{"class":"team home"})
        home_team = home_team.find("span",{"class":"long"}).text
        away_team = soup_lineup.find("div",{"class":"team away"})
        away_team = away_team.find("span",{"class":"long"}).text

        date = soup_lineup.find("div",{"class":"matchDate renderMatchDateContainer"}).text

        score=soup_lineup.find("div",{"class":"score fullTime"}).text
        score = score.split("-")
        home_score = score[0]
        away_score = score[1]

        
        teams_html = soup_lineup.findAll("div",{"class":"matchLineupTeamContainer"})
        teams_lineups = []
        for teams in teams_html:
            if file_year >= 10 and file_year <= 13:
                players = teams.findAll("span",{"class":"name"})
                i = 0
                while i < len(players):
                    for div in players[i]("div"):
                      div.decompose()
                    players[i] = players[i].text
                    players[i] = players[i].strip() #strip before finalising
                    i+=1
                teams_lineups.append(players)
            else:
                players = teams.findAll("div",{"class":"name"})
                i = 0
                while i < len(players):
                    for span in players[i]("span"):
                      span.decompose()
                    players[i] = players[i].text
                    players[i] = players[i].strip() #strip before finalising
                    i+=1
                teams_lineups.append(players)


        game_stats = [home_team,away_team,score,teams_lineups[0],teams_lineups[1],date]
        if game_stats == latest_game:
            year_games_list = year_games_list + last_file
            break
        year_games_list.append(game_stats)
        print(game_stats)
        print(len(teams_lineups[0]),len(teams_lineups[1]))
    year_games_list = str(year_games_list)
    f.write(year_games_list)
    f.close()
    file_year = file_year -1

    



