hostname = 'localhost'
username = 'root'
password = ''
database = 'fixtures'


import mysql.connector
from datetime import datetime
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
mycursor = myConnection.cursor()


myConnection.commit()

sql = "INSERT IGNORE INTO fixtures (match_date,home_team,away_team,LinkKey) VALUES (%s,%s,%s,%s)"


fixture_file =  "fixtures.csv"
fixtures = open(fixture_file,"r")
fixtures = fixtures.readlines()
fixtures = fixtures[1:]
for fixture in fixtures:
	fixture = fixture.split(",")
	m_date = fixture[0]
	m_date = datetime.strptime(m_date,'%A %d %B %Y')
	m_date = str(m_date)
	m_date = m_date[:-9]
	l_key = m_date + fixture[1].strip() + fixture[2].strip()
	l_key = l_key.replace(" ","")
	fixture = [m_date,fixture[1].strip(),fixture[2].strip(),l_key]
	val = tuple(fixture)
	mycursor.execute(sql, val)


myConnection.commit()

sql2 = "DELETE FROM fixtures WHERE LinkKey in (SELECT LinkKey FROM results.results)"
mycursor.execute(sql2)

myConnection.commit()


sql3 = "DELETE FROM fixtures WHERE Date(match_date) < CURDATE()"
mycursor.execute(sql3)

myConnection.commit()

myConnection.close()
