from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

file = "fixtures.csv"
f = open(file,"w")
header = "date,home,away\n"
f.write(header)

options = Options()
options.add_argument("--headless")
# binary = FirefoxBinary('D:\\browsers\\firefox\\firefox.exe')
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_options=options ,firefox_binary=binary)
driver.get("https://www.premierleague.com/fixtures")
time.sleep(4)
page_html = driver.page_source
page_soup = soup(page_html,"html.parser")
driver.close()
dates = page_soup.findAll("div",{"data-competition"})
date= page_soup.findAll("time",{"class":"date long"})
for i in date:   
   date = i.text
   day = page_soup.findAll("div",{"data-competition-matches-list":date})
   day = day[0]
   for j in day.findAll("li",{"class":"matchFixtureContainer"}):
      teams = j.findAll("span",{"class":"team"})
      t1  =teams[0].text
      t2 = teams[1].text
      #time = j.findAll("time",{"datetime":"score"})
      tmp = [date,t1,t2]
      print(tmp)
      if date != "Date To Be Confirmed":
         f.write(date + "," + t1 + ","  + t2 + "\n")
