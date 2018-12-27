from Rosters import Team_Lists


class Team:
    def __init__(self,Team_Name,lineups = None, lineup_stats = None):
        self.Team_Name = Team_Name
        self.lineups = []
        self.lineup_stats = []


class Player:
    """" A player's performance in a game"""
  
    def __init__(self,Team_Name,Player_Name,assist_data = None,player_stats=None):
        """Initialize attributes to describe a player"""
        
        self.player_stats = {'Team_Name' : Team_Name,
        'Game_ID':0,
        'Player_Name' : Player_Name,
        'Pts' : 0,
        'FGA' : 0,
        'FGM' : 0,
        'FGm' : 0,
        'Two_FGA' : 0,
        'Two_FGM' : 0,
        'Two_FGm' : 0,
        'Three_FGA' : 0,
        'Three_FGM' : 0,
        'Three_FGm' : 0,
        'DefReb' : 0,
        'OffReb' : 0,
        'TtlReb' : 0,
        'FTA' : 0,
        'FTm' : 0,
        'FTM' : 0,
        'Ast' : 0,
        'Stl' : 0,
        'Turnover':0,
        'Block': 0,
        'Foul':0,
        'Lineup_ID':None}  

        for team in Team_Lists:
            if(team[0]==self.player_stats['Team_Name']):
                # print("found the team!")
                self.assist_data = dict((el,0) for el in team[1:])
                # print(self.assist_data)

    def pass_to(self,teammate):


        # initiate players dictionary storing the assist information
        # print(self.Name +'\'s Passing history:\n')
        for key in self.assist_data: 
            if(teammate == key):
                self.assist_data[key]+=1
        # for k,v in self.assist_data.items():
        #     print( str(k) +' : '+str(v))
        # print('\n')


class Lineup:
    def __init__(self,number,players = None):
        self.number = number   # recording the session of this lineup
        self.players = []

class Lineup_Stats:

    def __init__(self,stats = None):

        self.stats = {'Team_Name':None,
                            'Game_ID':0,
                            'session_number' : 0,
                            'Lineup_Players': None,
                            'From' : 0 ,
                            'To' : 0 ,
                            'Min' : None,
                            'Lineup_Score' : 0 ,
                            'Oppo_Score' : 0 ,
                            'FGA' : 0 ,  
                            'FGM' : 0 ,  
                            'FGm' : 0 ,  
                            'Two_FGA' : 0 ,  
                            'Two_FGM' : 0 ,  
                            'Two_FGm' : 0 ,  
                            'Three_FGA' : 0 ,  
                            'Three_FGM' : 0 ,
                            'Three_FGm' : 0 ,
                            'DefReb' : 0 ,  
                            'OffReb' : 0 ,  
                            'TtlReb' : 0 ,  
                            'FTA' : 0 ,
                            'FTm' : 0 ,
                            'FTM' : 0 ,
                            'Ast' : 0 ,
                            'Stl' : 0 ,
                            'Block':0 ,
                            'Foul':0 ,
                            'Turnover':0,
                            'Oppo_FGA' : 0 ,  
                            'Oppo_FGM' : 0 ,  
                            'Oppo_FGm' : 0 ,  
                            'Oppo_Two_FGA' : 0 ,  
                            'Oppo_Two_FGM' : 0 ,  
                            'Oppo_Two_FGm' : 0 ,  
                            'Oppo_Three_FGA' : 0 ,  
                            'Oppo_Three_FGM' : 0 ,
                            'Oppo_Three_FGm' : 0 ,
                            'Oppo_DefReb' : 0 ,  
                            'Oppo_OffReb' : 0 ,  
                            'Oppo_TtlReb' : 0 ,  
                            'Oppo_FTA' : 0 ,
                            'Oppo_FTm' : 0 ,
                            'Oppo_FTM' : 0 ,
                            'Oppo_Ast' : 0 ,
                            'Oppo_Stl' : 0 ,
                            'Oppo_Turnover':0,
                            'Oppo_Block':0,
                            'Oppo_Foul':0,
                            'PlusMinus' : 0,
                            'Lineup_ID':None}


class Score_Tracker:

    def __init__(self,tracker=None):

        self.tracker = {
        'Game_ID':None, 
        'Session_num':[],
        'Time' : [],
        'Score_Dif':[]
        }



# score_track = Score_Tracker()
# score_track.tracker['Home'].extend([1,3,4])


# print(score_track.tracker)