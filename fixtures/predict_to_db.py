hostname = 'localhost'
username = 'root'
password = ''
database = 'fixtures'


import mysql.connector
from datetime import datetime
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
mycursor = myConnection.cursor()


myConnection.commit()

sql = "INSERT INTO predictions (match_date,home_team,away_team,LinkKey,pred_home_score,pred_away_score) VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE pred_home_score = VALUES(pred_home_score),pred_away_score = VALUES(pred_away_score)"


prediction_file =  "predictions.txt"
predictions = open(prediction_file,"r")
predictions = predictions.readlines()
for prediction in predictions:
	prediction = prediction.split(",")
	m_date = prediction[0]
	m_date = datetime.strptime(m_date,'%A %d %B %Y')
	m_date = str(m_date)
	m_date = m_date[:-9]
	l_key = m_date + prediction[1].strip() + prediction[2].strip()
	l_key = l_key.replace(" ","")
	print(l_key)
	prediction = [m_date,prediction[1].strip(),prediction[2].strip(),l_key,prediction[-2],prediction[-1]]
	val = tuple(prediction)
	mycursor.execute(sql, val)

myConnection.commit()

myConnection.close()
