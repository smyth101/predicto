
def player_name_translate(name,lst,status="current",club=""):
   name_ignore = [['Tottenham Hotspur', 'jimmy walker'],['Manchester City', 'adam johnson'],['Newcastle United', 'sammy ameobi'],['Tottenham Hotspur', 'kyle walker-peters'],['Manchester City', 'aleix garcía'],['Norwich City', 'ryan bennett'], ['Blackburn Rovers', 'marcus olsson'],['Manchester United', 'michael keane'],['West Ham United', 'carlton cole'],['West Bromwich Albion', 'kane wilson'],['Everton', 'joe williams'],['Crystal Palace', 'jonathan benteke'],['West Bromwich Albion', 'luke daniels'],['Liverpool', 'lloyd jones']]
   if [club,name] in name_ignore:
      return "unfound"

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
   }
   #translating name
   translationTable = str.maketrans("éàèùâêîôûççøäöüëčšíïğğōúóáćěðñłńýęžăřşůåãż","eaeuaeiouccoaouecsiiggouoacednlnyezarsuaaz")
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

all_years_unmatched = {}
max_year = 19
min_year = 10
total_overall = 0
year = 13
while year >= 13:
   fifa_file =  str(year) + "/player_and_ratings.txt"
   f = open(fifa_file,"r",encoding="utf8")
   fifa_list = f.readlines()
   f.close()


   result_file = "../results_and_players/" + str(year) + "/results.csv"
   f = open(result_file,"r",encoding="windows-1252")
   result_list = f.readlines()
   f.close()

   invalid_names = []

   result_list = result_list[0]
   result_list = eval(result_list)
   approved = []
   non_approved = []
   fifa_list = eval(fifa_list[0])
   fifa_names = [team[0] for team in fifa_list]


   result_dict = {i:[] for i in fifa_names}

   f_dict = {i:[] for i in fifa_names}
   for t in fifa_list:
      l = [i[0].lower() for i in t[1]]
      f_dict[t[0]] = l
   
   #player value dictionary without player names lowercased
   f_dict_original = {i:[] for i in fifa_names}
   for t in fifa_list:
      l = [i[0].lower() for i in t[1]]
      f_dict_original[t[0]] = l


   found_dict = {i:[] for i in fifa_names}
   for i in result_list:
      
      for k in range(0,2):
         fifa_dict = f_dict
         fifa_dict_original = f_dict_original
         for j in fifa_list:

            if j[0] == i[k]:
               if j[0] not in approved:
                  approved.append(j[0])
               if j[0] in fifa_names:
                  fifa_names.remove(j[0])  
               if i[k] in non_approved:
                  non_approved.remove(i[k]) 


               for r_player in i[k+3]:
                  if r_player.lower not in fifa_dict_original[j[0]]:
                     name_index = player_name_translate(r_player.lower(),fifa_dict[j[0]],club = i[k])
                     if name_index == "unfound":
                        #if player unfound check to see were they in next year
                        if (year+1) <= max_year:
                              fifa_next = "../fifa_players/" + str(year+1) + "/player_and_ratings.txt"
                              f_next = open(fifa_next,"r",encoding="utf8")
                              fifa_next_list = f_next.readlines()
                              f_next.close()
                              fifa_next_list = eval(fifa_next_list[0])
                              fifa_next_names = [team[0] for team in fifa_next_list]
                              f_next_dict = {i:[] for i in fifa_next_names}
                              for t in fifa_next_list:
                                 l = [i[0].lower() for i in t[1]]
                                 f_next_dict[t[0]] = l
                              if j[0] in f_next_dict.keys():
                                 name_index = player_name_translate(r_player.lower(),f_next_dict[j[0]],"next",club = i[k])
                                 if name_index == "unfound":
                                    if r_player not in result_dict[j[0]]:
                                       result_dict[j[0]].append(r_player)
                                 else:
                                    for team_next in fifa_next_list:
                                       if team_next[0] == j[0]:
                                          if r_player not in found_dict[j[0]]:
                                             found_dict[j[0]].append(r_player)
                                             player_value = team_next[1][name_index][1] 
                                             j[1].append((r_player,player_value))

                                             break             
                        #if player unfound check to see were they in previous year
                        if name_index == "unfound" and (year-1) >= min_year:
                           fifa_prev = "../fifa_players/" + str(year-1) + "/player_and_ratings.txt"
                           f_prev = open(fifa_prev,"r",encoding="utf8")
                           fifa_prev_list = f_prev.readlines()
                           f_prev.close()
                           fifa_prev_list = eval(fifa_prev_list[0])
                           fifa_prev_names = [team[0] for team in fifa_prev_list]
                           f_prev_dict = {i:[] for i in fifa_prev_names}
                           for t in fifa_prev_list:
                              l = [i[0].lower() for i in t[1]]
                              f_prev_dict[t[0]] = l
                           if j[0] in f_prev_dict.keys():
                              name_index = player_name_translate(r_player.lower(),f_prev_dict[j[0]],"next",club=i[k])
                              if name_index == "unfound":
                                 if r_player not in result_dict[j[0]]:
                                    result_dict[j[0]].append(r_player)
                              else:
                                 if r_player in result_dict[j[0]]:
                                    result_dict[j[0]].remove(r_player)

                                 for team_prev in fifa_prev_list:
                                    if team_prev[0] == j[0]:
                                       if r_player not in found_dict[j[0]]:
                                          found_dict[j[0]].append(r_player)
                                          player_value = team_prev[1][name_index][1] 
                                          j[1].append((r_player,player_value))
                                          break             


                        #adding to unfound players
                        if name_index == "unfound":
                           if r_player not in result_dict[j[0]]:
                              result_dict[j[0]].append(r_player)


                     else:
                        player_value = j[1][name_index][1] 
                        j[1][name_index] = (r_player,player_value)


               break
            else:
               if i[k] not in non_approved:
                  non_approved.append(i[k])
   #mapping players that were not found to a value
   for team in result_dict.keys():
      players_50 = []
      i = 0
      while i < len(result_dict[team]):
         print(len(result_dict[team]))
         print(result_dict[team][i])
         print(result_dict[team])
         players_50.append((result_dict[team][i],50))
         print(players_50)
         result_dict[team].remove(result_dict[team][i])
         
      for i in fifa_list:
         if i[0] == team:
            i[1] = i[1]+ players_50
            break


   total_year = 0
   for i in result_dict.keys():
      total_year+= len(result_dict[i])
      if i in all_years_unmatched.keys():
         for j in result_dict[i]:
            if j not in all_years_unmatched[i]:
               all_years_unmatched[i].append(j)
      else:
         all_years_unmatched[i] = result_dict[i]



   f = open(fifa_file,"w",encoding="utf8")
   f.write(str(fifa_list))
   f.close()

   total_overall += total_year
   year-=1
print(all_years_unmatched)
every_player_unmatched_count = 0
for i in all_years_unmatched.keys():
   every_player_unmatched_count += len(all_years_unmatched[i])
print(every_player_unmatched_count)