from pandas import DataFrame, read_csv
import pandas as pd
import xlrd
import datetime
#Reading spreadsheet data and creating file object 
file = r'C:\Users\Aman Riat\Documents\FantasyWebApp\FantasyApp\Games\static\Games\NBA_18_19.xls'
data = pd.read_excel(file)

def game_position(game):
    '''
    (str) -> int
    Returns the list position of the date entered 

    >>> Game_Position("12/25")
    70
    '''
    
    for date_index in range (0,(len(data['Date']))):
        if game in data['Date'][date_index]:
            return date_index
        else:
            pass
 
def games_played(start, end):
    '''
    (int,int) -> None
    Iterates over the teams in game range to see how many times each team plays
    Game is played if a string is in cell position otherwise it's null
    Prints lists that shows the amount of games teams play
    
    >>> Games_Played(0,7)
    Teams with 4 games: ['Bos', 'Cha', 'Den', 'Gsw', 'Ind',
    'LAC', 'Min', 'NY', 'Orl', 'Phi', 'Sac', 'Tor']

    Teams with 3 games: ['Atl', 'Bkn', 'Chi', 'Cle', 'Dal',
    'Det', 'Hou', 'LAL', 'Mem', 'Mia', 'Mil', 'NO', 'OKC',
    'Pho', 'Por', 'SA', 'Uth', 'Was']

    '''

    #New list with all NBA Teams
    nba_t = (list(data)[1:31])
    totalTeams = []

    #Variable used as counter to retrieve position of team in nba_t list
    team = 0
    #testLength is used to determine the number of teams each game play and sort those teams together 
    testLength = []

    #Loop iterates over 30 teams
    while team <= 29:
        gamesPlayed = 0
        team_sch = (list(data[nba_t[team]]))
        
        #For loop iterates over game range user enters 
        for game in range (start,end+1):
            if type(team_sch[game]) == str:
                gamesPlayed += 1
            else:
                pass

        currentTeam = Teams(nba_t[team],start,end,gamesPlayed)
        totalTeams.append(currentTeam)

        #Each unique number is added to know what dimension list to make to organize teams together 
        if currentTeam.total_games() not in testLength:
            testLength.append(currentTeam.total_games())
        team += 1

    #multi dimension list where each cell holds teams that play the same games together 
    gamesPlayedByTeam = [[] for i in range (len(testLength))]

    #sorting through teams and their games played from highest to lowest 
    #makes it easier to group together in the list later 
    totalTeamsLength = len(totalTeams)
    for i in range(totalTeamsLength):
        for j in range (0,totalTeamsLength-i-1):
            if (totalTeams[j]).total_games() < (totalTeams[j+1]).total_games():
                (totalTeams[j]), (totalTeams[j+1]) = (totalTeams[j+1]),(totalTeams[j])  

    #By the nature of how teams are added to the list the first and last teams must be added beforehand
    #This is so the teams can be compared to detremine if they should be held in the first cell or second 
    gamesPlayedByTeam[0].append(totalTeams[0])
    gamesPlayedByTeam[len(testLength)-1].append(totalTeams[totalTeamsLength-1])

    #Teams are added by comparing their number of games to the team behind them 
    #If the number is the same as the team behind them then the team is added to the same cell 
    #If the number is different then the position increments and the team go into the next cell 
    currentPosition = 0
    for x in range(1,totalTeamsLength-1):
        if totalTeams[x].total_games() == totalTeams[x-1].total_games():
            gamesPlayedByTeam[currentPosition].append(totalTeams[x])
        else:
            currentPosition += 1
            gamesPlayedByTeam[currentPosition].append(totalTeams[x])

    return (gamesPlayedByTeam)

def week_games(start,end):
    '''
    (int, int) -> None
    Prints out games days that are light

    >>> Week_Games(76,82)
    Light Game Days:
    Tu-01/01 :  5  games
    Th-01/03 :  3  games
    '''
    #TODO: Add additional output to show which teams play on that day 
    print ("Light Game Days:")
    nba_teams = (list(data)[1:31])

    totalLightGameDays = []
    for date in range (start,end+1):
        teamsInAWeek =[]
        games = 0
        for team in range (0,30):
            current_team = (list(data[nba_teams[team]]))
            if type(current_team[date]) == str:
                    games += 1
                    teamsInAWeek.append(Teams(nba_teams[team]))
               
        if games == 0:
            return []
        elif games < 14:
            totalLightGameDays.append(teamsInAWeek)

    return totalLightGameDays


class Teams:
    '''
    Object stores team name, start date of back to back, and end date of back to back
    '''
    
    def __init__(self,team,date_start = None,date_end = None, totalGames = None):
        self.team = team
        self.start = date_start
        self.end = date_end
        self.totalGames = totalGames

    def total_games(self):
        return self.totalGames
    
    def __str__(self):
        if (self.start ==0 and self.end ==0):
            return str(self.team)
        return str(self.team) + ': '+ (data['Date'][self.start]) + ' - ' + (data['Date'][self.end])

    def __repr__(self):
        return str(self.team)

    def __eq__(self,other):

        if self.start == other.start and self.end == other.end:
            return True
        else:
            return False 

class BackToBack:
    '''
    Displays teams with backs to backs on the same day 
    '''
    def __init__(self,start,end):
        self.start = start
        self.end = end


    def teams_with_back(self):
        #New list with all NBA Teams
        nba_t = (list(data)[1:31])

        #Counter to retrieve position of team in nba_t list and list of teams with a back to back
        team = 0
        b2b = []

        while team <= 29:
            team_sch = (list(data[nba_t[team]]))
  
            for game in range (self.start,self.end+1):
                if type(team_sch[game]) == str and type(team_sch[game+1]) == str:
                    new_team = Teams((nba_t[team]),game,game+1)
                    b2b.append(new_team)
                else:
                    pass

            team += 1
        #modified bubble sort to sort teams by date the back to back is played 
        total_teams = len(b2b)
        for i in range(total_teams):
            for j in range (0,total_teams-i-1):
                if (b2b[j]).start > (b2b[j+1]).start:
                    (b2b[j]), (b2b[j+1])= (b2b[j+1]),(b2b[j])       
        print (b2b)
        total_teams_with_b2b = []
        if len(b2b) > 0:
            #Loops over teams with back to backs to sort and output teams with back to backs on the same days 
            while (len(b2b)) > 0:
                teams_back = []

                #sentinel used to find every team with back to backs on the same day
                b2b_start = b2b[0]
                
                for nba_team in range (len(b2b)):
                    print (b2b_start)
                    # == works here as it compares the start dates to each other 
                    if b2b_start == b2b[nba_team]:
                        teams_back.append(b2b[nba_team])

                #removing teams that have been sorted for a back to back from original list   
                for sorted_team in teams_back:
                    if sorted_team in b2b:
                        b2b.remove(sorted_team)

                total_teams_with_b2b.append(teams_back)

            return total_teams_with_b2b

        else:
            return []


def convert_time(date):
    #Convert time object to string to better use pre-existing code
    cleaned_date = date.strftime('%m/%d')

    return cleaned_date
