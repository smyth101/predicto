import unittest
import test

#testing the length of table is 20
class tests(unittest.TestCase):
    def test1(self):
    	table_len = test.table_length()
    	self.assertEqual(table_len, 20, 'incorrect table size')

    
    #testing that all the seasons collected that have finished have 380 games in them
    def test2(self):
        results_len = test.results_length(10)
        self.assertEqual(results_len, 380, 'incorrect table size')
        results_len = test.results_length(11)
        self.assertEqual(results_len, 380, 'incorrect results size')
        results_len = test.results_length(12)
        self.assertEqual(results_len, 380, 'incorrect results size')
        results_len = test.results_length(13)
        self.assertEqual(results_len, 380, 'incorrect results size')
        results_len = test.results_length(14)
        self.assertEqual(results_len, 380, 'incorrect results size')
        results_len = test.results_length(15)
        self.assertEqual(results_len, 380, 'incorrect results size')
        results_len = test.results_length(16)
        self.assertEqual(results_len, 380, 'incorrect results size')
        results_len = test.results_length(17)
        self.assertEqual(results_len, 380, 'incorrect results size')
        results_len = test.results_length(18)
        self.assertEqual(results_len, 380, 'incorrect results size')

    #testing that all players in results have a mapping to a player rating
    def test3(self):
        player_match = test.results_player_match(10)
        self.assertFalse(player_match, 'missing player mapping')
        player_match = test.results_player_match(11)
        self.assertFalse(player_match, 'missing player mapping')
        player_match = test.results_player_match(12)
        self.assertFalse(player_match, 'missing player mapping')
        player_match = test.results_player_match(13)
        self.assertFalse(player_match, 'missing player mapping')
        player_match = test.results_player_match(14)
        self.assertFalse(player_match, 'missing player mapping')
        player_match = test.results_player_match(15)
        self.assertFalse(player_match, 'missing player mapping')
        player_match = test.results_player_match(16)
        self.assertFalse(player_match, 'missing player mapping')
        player_match = test.results_player_match(17)
        self.assertFalse(player_match, 'missing player mapping')
        player_match = test.results_player_match(18)
        self.assertFalse(player_match, 'missing player mapping')
        player_match = test.results_player_match(19)
        self.assertFalse(player_match, 'missing player mapping')

    #testing that the squad value generated is correct for 20 random games
    def test4(self):
        squad_value = test.team_values(19,0)
        self.assertEqual(squad_value,[1360,1385])
        squad_value = test.team_values(19,125)
        self.assertEqual(squad_value,[1405,1377])
        squad_value = test.team_values(18,40)
        self.assertEqual(squad_value,[1355,1417])
        squad_value = test.team_values(18,250)
        self.assertEqual(squad_value,[1387,1351])
        squad_value = test.team_values(17,30)
        self.assertEqual(squad_value,[1384,1328])
        squad_value = test.team_values(17,310)
        self.assertEqual(squad_value,[1482,1389])
        squad_value = test.team_values(16,5)
        self.assertEqual(squad_value,[1363, 1317])
        squad_value = test.team_values(16,275)
        self.assertEqual(squad_value,[1318, 1358])
        squad_value = test.team_values(15,15)
        self.assertEqual(squad_value,[1270, 1360])
        squad_value = test.team_values(15,360)
        self.assertEqual(squad_value,[1479, 1408])
        squad_value = test.team_values(14,2)
        self.assertEqual(squad_value,[1281, 1276])
        squad_value = test.team_values(14,365)
        self.assertEqual(squad_value,[1318, 1329])
        squad_value = test.team_values(13,60)
        self.assertEqual(squad_value,[1209, 1414])
        squad_value = test.team_values(13,220)
        self.assertEqual(squad_value,[1341, 1201])
        squad_value = test.team_values(12,8)
        self.assertEqual(squad_value,[1342, 1347])
        squad_value = test.team_values(12,379)
        self.assertEqual(squad_value,[1306, 1414])
        squad_value = test.team_values(11,75)
        self.assertEqual(squad_value,[1299, 1485])
        squad_value = test.team_values(11,305)
        self.assertEqual(squad_value,[1451, 1300])
        squad_value = test.team_values(10,25)
        self.assertEqual(squad_value,[1460, 1319])
        squad_value = test.team_values(10,240)
        self.assertEqual(squad_value,[1293, 1260])

    #testing that the function for finding a teams position is correct by comparing with end of season tables
    def test5(self):
        end_year_table = test.table_maker(18)
        final_table = [["Manchester City",100],["Manchester United",81],["Tottenham Hotspur",77],["Liverpool",75],["Chelsea",70],["Arsenal",63],["Burnley",54],["Everton",49],["Leicester City",47],["Newcastle United",44],["Crystal Palace",44],["AFC Bournemouth",44],["West Ham United",42],["Watford",41],["Brighton and Hove Albion",40],["Huddersfield Town",37],["Southampton",36],["Swansea City",33],["Stoke City",33],["West Bromwich Albion",31]]
        self.assertEqual(end_year_table,final_table)
        end_year_table = test.table_maker(17)
        final_table = [["Chelsea",93],["Tottenham Hotspur",86],["Manchester City",78],["Liverpool",76],["Arsenal",75],["Manchester United",69],["Everton",61],["Southampton",46],["AFC Bournemouth",46],["West Bromwich Albion",45],["West Ham United",45],["Leicester City",44],["Stoke City",44],["Crystal Palace",41],["Swansea City",41],["Burnley",40],["Watford",40],["Hull City",34],["Middlesbrough",28],["Sunderland",24]]
        self.assertEqual(end_year_table,final_table)
        end_year_table = test.table_maker(16)
        final_table = [["Leicester City",81],["Arsenal",71],["Tottenham Hotspur",70],["Manchester City",66],["Manchester United",66],["Southampton",63],["West Ham United",62],["Liverpool",60],["Stoke City",51],["Chelsea",50],["Everton",47],["Swansea City",47],["Watford",45],["West Bromwich Albion",43],["Crystal Palace",42],["AFC Bournemouth",42],["Sunderland",39],["Newcastle United",37],["Norwich City",34],["Aston Villa",17]]
        self.assertEqual(end_year_table,final_table)
        end_year_table = test.table_maker(15)
        final_table = [["Chelsea",87],["Manchester City",79],["Arsenal",75],["Manchester United",70],["Tottenham Hotspur",64],["Liverpool",62],["Southampton",60],["Swansea City",56],["Stoke City",54],["Crystal Palace",48],["Everton",47],["West Ham United",47],["West Bromwich Albion",44],["Leicester City",41],["Newcastle United",39],["Sunderland",38],["Aston Villa",38],["Hull City",35],["Burnley",33],["Queens Park Rangers",30]]
        self.assertEqual(end_year_table,final_table)
        end_year_table = test.table_maker(14)
        final_table = [["Manchester City",86],["Liverpool",84],["Chelsea",82],["Arsenal",79],["Everton",72],["Tottenham Hotspur",69],["Manchester United",64],["Southampton",56],["Stoke City",50],["Newcastle United",49],["Crystal Palace",45],["Swansea City",42],["West Ham United",40],["Sunderland",38],["Aston Villa",38],["Hull City",37],["West Bromwich Albion",36],["Norwich City",33],["Fulham",32],["Cardiff City",30]]
        self.assertEqual(end_year_table,final_table)
        end_year_table = test.table_maker(13)
        final_table = [["Manchester United",89],["Manchester City",78],["Chelsea",75],["Arsenal",73],["Tottenham Hotspur",72],["Everton",63],["Liverpool",61],["West Bromwich Albion",49],["Swansea City",46],["West Ham United",46],["Norwich City",44],["Fulham",43],["Stoke City",42],["Southampton",41],["Aston Villa",41],["Newcastle United",41],["Sunderland",39],["Wigan Athletic",36],["Reading",28],["Queens Park Rangers",25]]
        self.assertEqual(end_year_table,final_table)
        end_year_table = test.table_maker(12)
        final_table = [["Manchester City",89],["Manchester United",89],["Arsenal",70],["Tottenham Hotspur",69],["Newcastle United",65],["Chelsea",64],["Everton",56],["Liverpool",52],["Fulham",52],["West Bromwich Albion",47],["Swansea City",47],["Norwich City",47],["Sunderland",45],["Stoke City",45],["Wigan Athletic",43],["Aston Villa",38],["Queens Park Rangers",37],["Bolton Wanderers",36],["Blackburn Rovers",31],["Wolverhampton Wanderers",25]]
        self.assertEqual(end_year_table,final_table)
        end_year_table = test.table_maker(11)
        final_table = [["Manchester United",80],["Chelsea",71],["Manchester City",71],["Arsenal",68],["Tottenham Hotspur",62],["Liverpool",58],["Everton",54],["Fulham",49],["Aston Villa",48],["Sunderland",47],["West Bromwich Albion",47],["Newcastle United",46],["Stoke City",46],["Bolton Wanderers",46],["Blackburn Rovers",43],["Wigan Athletic",42],["Wolverhampton Wanderers",40],["Birmingham City",39],["Blackpool",39],["West Ham United",33]]
        self.assertEqual(end_year_table,final_table)
        end_year_table = test.table_maker(10)
        final_table = [["Chelsea",86],["Manchester United",85],["Arsenal",75],["Tottenham Hotspur",70],["Manchester City",67],["Aston Villa",64],["Liverpool",63],["Everton",61],["Birmingham City",50],["Blackburn Rovers",50],["Stoke City",47],["Fulham",46],["Sunderland",44],["Bolton Wanderers",39],["Wolverhampton Wanderers",38],["Wigan Athletic",36],["West Ham United",35],["Burnley",30],["Hull City",30],["Portsmouth",28]]
        self.assertEqual(end_year_table,final_table)

    # def test6(self):
    #     squad_map = test.squad_player_match(current_year = 19)
    #     self.assertFalse(squad_map)

    #testing that all unavailable players have a rating
    def test7(self):
        unavailable_map = test.unavailable_player_match()
        self.assertFalse(unavailable_map)

if __name__ == "__main__":
	unittest.main()