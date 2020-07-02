from table_maker import Team
from table_maker import make_table

for i in range(10,20):
	make_table(i)

team_objs = make_table(16)
for x in team_objs:
		print(x.name,x.pts)