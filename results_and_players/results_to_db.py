hostname = 'localhost'
username = 'root'
password = ''
database = 'results'



import mysql.connector
from datetime import datetime
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
mycursor = myConnection.cursor()


myConnection.commit()

year = 19

sql = "INSERT IGNORE INTO results (LinkKey,match_date,home_team,away_team,home_score,away_score) VALUES (%s,%s,%s,%s,%s,%s) "
result_file =  str(year) + "/results_with_value.txt"
results = open(result_file,"r")
results = results.readline()
results = eval(results)
for result in results[::-1]:
	m_date = result[-1]
	m_date = datetime.strptime(m_date,'%a %d %b %Y')
	m_date = str(m_date)
	m_date = m_date[:-9]
	l_key = m_date + result[0] + result[2]
	l_key = l_key.replace(" ","")
	result = [l_key,m_date,result[0],result[2],result[4][0],result[4][1]]
	val = tuple(result)
	mycursor.execute(sql, val)

myConnection.commit()

myConnection.close()
