
def player_name_translate(name,lst,status="current"):
   name_mapping = {}
   #translating name
   translationTable = str.maketrans("éàèùâêîôûçøäöüëčšíïğōúóáćěðñłńýęžăřşůåãż","eaeuaeioucoaouecsiigouoacednlnyezarsuaaz")
   original_name = name
   name = name.translate(translationTable)
   name_apperances = 0
   name_spotted = 0

   i = 0
   while i < len(lst):
      n = lst[i]
      original_n = n
      n = n.translate(translationTable)
      if name == n:
         return i
      #removing hyphens
      n1 = n
      name1 = name
      name1 = name1.replace("-"," ")
      n1 = n1.replace("-"," ")
      if name1 == n1:
         return i
      #comparing same name in differant order
      n2 = n1.split()
      name2 = name1.split()
      if n2[-1] == name2[-1]:
         name_apperances += 1
         name_spotted = i

      if len(n2) == len(name2):
         c = 0
  
         while c < len(n2):
            if n2[c] in name2:
               c+=1
            else:
               break
         if c == len(n2):
            return i
      #comparing entire shorter name contained in longer name
      if len(n2) != len(name2):
         if len(n2) < len(name2):
            c = 0
            while c < len(n2):
               if n2[c] in name2:
                  c+=1
               else:
                  break
            if c == len(n2):
               return i
         else:
            c = 0
            while c < len(name2):
               if name2[c] in n2:
                  c+=1
               else:
                  break
            if c == len(name2):
               return i
      #mapping players who have nicknames or miss spellings
      if original_name in name_mapping.keys():
         if name_mapping[original_name] == original_n:
            return i

      name3 = name.replace("'","")
      n3 = n.replace("'","")
      if name3 == n3:
         return i
         
      i+=1
   if name_apperances == 1:
      if status == "current":
         return name_spotted

   
   return "unfound"

filename = "players.txt"
result_file = open(filename,"r",encoding="windows-1252")
file = result_file.readline()
result_file.close()
file = eval(file)
fifa_filename = "../fifa_players/19/player_and_ratings.txt"
fifa_file = open(fifa_filename,"r",encoding="utf8")
f_file = fifa_file.readline()
fifa_file.close()
f_file = eval(f_file)

fifa_names = [team[0] for team in f_file]


f_dict = {i:[] for i in fifa_names}
for t in f_file:
  l = [i[0].lower() for i in t[1]]
  f_dict[t[0]] = l

status = False

for i in file:
	t_name = i[0]
	team = i[1]

	for player in team:
		status = False
		if player.lower() in f_dict[t_name]:
			do = "Nothing"


		else:
			name = player.lower()
			index = player_name_translate(name,f_dict[t_name])
			if index != "unfound":
				for tn in f_file:
					if tn[0] == t_name:
						value = f_file[f_file.index(tn)][1][index][1]
						player_stat = (player,value)
						f_file[f_file.index(tn)][1][index] = player_stat

f = open("../fifa_players/19/player_and_ratings.txt","w")
f.write(str(f_file))
			
		