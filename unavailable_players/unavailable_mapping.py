def player_name_translate(name,lst,status="current"):
   name_mapping = {
   "chicharito": "javier hernández",
   "zanka" : "mathias jørgensen",
   "ahmed hegazi":"ahmed hegazy",
   "robert green":"rob green",
   "joe willock":"joseph willock",
   "fabri":"fabricio",
   "andré-frank zambo anguissa":"andré franck zambo an...",
   "bradley smith":"brad smith",
   "ahmed el mohamady":"ahmed elmohamady",
   "dieudonne mbokani bezua": "dieumerci mbokani",
   "ki sung-yeung": "ki sung-yueng"
   }
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
         if n2[-1][-3:] == "...":
            n2 = n2[:-1]
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

filename = "unavailable.txt"
file = open(filename,"r")
file = file.readline()
file = eval(file)
fifa_filename = "../fifa_players/19/player_and_ratings.txt"
fifa_file = open(fifa_filename,"r")
f_file = fifa_file.readline()
fifa_file.close()
f_file = eval(f_file)
team_names = file.keys()
fifa_names = [name[0] for name in f_file]
fifa_dict = {i:[] for i in fifa_names}
copy = {i:[] for i in fifa_names}
for t in f_file:
   l = [i[0].lower() for i in t[1]]
   cpy = [i[0] for i in t[1]]
   fifa_dict[t[0]] = l
   copy[t[0]] = cpy

status = False
team_names = file.keys()
for t_name in team_names:
   team = file[t_name]
   for fifa_team in f_file:
      if fifa_team[0] == t_name:
         for player in team:
            status = False
            for fifa_player in fifa_team[1]:
               if fifa_player[0] == player[0]:
                  status = True
                  break
                  
            if status == False:
            
               word = player_name_translate(player[0].lower(),fifa_dict[t_name])
               if word != "unfound":
                  file[t_name][team.index(player)][0] = copy[t_name][word]
                  print(copy[t_name][word])
               else:
                  print(player[0])
print(str(file))
file_write = open(filename,"w")
file_write.write(str(file))