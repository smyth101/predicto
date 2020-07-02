hostname = 'localhost'
username = 'root'
password = ''
database = 'results'

# Simple routine to run a query on a database and print the results:

import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
mycursor = myConnection.cursor()

sql = "DELETE FROM pl_table WHERE position >= 1"
mycursor.execute(sql)
myConnection.commit()

sql = "INSERT INTO pl_table (team_name,position,played,won,drawn,lost,gf,ga,gd,points) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE team_name=values(team_name),played=values(played),won=values(won),drawn=values(drawn),lost=values(lost),gf = values(gf),ga=values(ga),gd = values(gd),points = values(points)"


table_file = "PLtable.txt"
table = open(table_file,"r")
table = table.readlines()
for line in table:
	line = line.strip()
	line = line.split(",")
	val = tuple(line)
	mycursor.execute(sql, val)

myConnection.commit()

myConnection.close()
