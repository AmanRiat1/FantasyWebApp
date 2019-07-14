import pandas as pd
import os
import datetime

#Reading spreadsheet data and creating file object, when running file indepdently remove Games\static\Games\ part
file = os.path.realpath(r'Games/static/Games/NBA_18_19.xls')
data = pd.read_excel(file)

def convert_time(date):
    #Convert time object to string to better use pre-existing code
    cleaned_date = date.strftime('%m/%d')

    return cleaned_date

def game_position(game):
    '''
    Function to find position of entered date in excel sheet

    Parameters:
        game (str): Date of a NBA game

    Returns:
        int: Position of game in excel sheet
    '''
    
    for date_index in range (0,(len(data['Date']))):
        if game in data['Date'][date_index]:
            return date_index

 
def games_played(start, end):
    '''
    Function to find how many games each NBA team plays in specified date range

    Parameters:
        start (int): Start date of date range
        end (int): End date of date range

    Returns:
        list: multi-dimensional list where each cell holds teams that play the same amount of games
    '''
    if (start == None) or (end == None):
        return None

    nbaTeams = (list(data)[1:31])
    totalTeams = []

    #Variable used as counter to retrieve position of team in nba_t list
    team = 0
    #testLength is used to determine the number of games each teams plays and sort those teams together
    testLength = []

    while team <= 29:
        gamesPlayed = 0
        teamSchedule = (list(data[nbaTeams[team]]))
        for game in range (start,end+1):
            if type(teamSchedule[game]) == str:
                gamesPlayed += 1
            else:
                pass

        currentTeam = Teams(nbaTeams[team],start,end,gamesPlayed)
        totalTeams.append(currentTeam)

        #Each unique number is added to know what dimension list to make to organize teams together 
        if currentTeam.totalGames not in testLength:
            testLength.append(currentTeam.totalGames)
        team += 1

    #multi dimension list where each cell holds teams that play the same games together 
    gamesPlayedByTeam = [[] for i in range (len(testLength))]

    #sorting through teams and their games played from highest to lowest 
    #makes it easier to group together in the list later 
    totalTeamsLength = len(totalTeams)
    for i in range(totalTeamsLength):
        for j in range (0,totalTeamsLength-i-1):
            if (totalTeams[j]).totalGames < (totalTeams[j+1]).totalGames:
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
        if totalTeams[x].totalGames == totalTeams[x-1].totalGames:
            gamesPlayedByTeam[currentPosition].append(totalTeams[x])
        else:
            currentPosition += 1
            gamesPlayedByTeam[currentPosition].append(totalTeams[x])

    return (gamesPlayedByTeam)

def light_game_days(start,end):
    '''
    Function to calculate days with a lesser amount of games in specified date range

     Parameters:
        start (int): Start date of date range
        end (int): End date of date range

    Returns:
        list: multi-dimensional list where each cell holds teams that play on the light game day
    '''

    if (start == None) or (end == None):
        return None

    nba_teams = (list(data)[1:31])

    totalLightGameDays = []
    for date in range (start,end+1):
        lightGameDay =[]
        games = 0
        for team in range (0,30):
            current_team = (list(data[nba_teams[team]]))
            if type(current_team[date]) == str:
                    games += 1
                    lightGameDay.append(Teams(nba_teams[team], None, None, None, data['Date'][date]))
               
        if games == 0:
            return None
        elif games < 14:
            totalLightGameDays.append(lightGameDay)

    return totalLightGameDays


class Teams:
    '''
    Object stores team name, start date of back to back, and end date of back to back

    Attributes:
        team (str): Team name
        start (int): Position of start date in excel sheet
        end (int): Position of end date in excel sheet
        totalGames (int): Total number of games team plays in date range
        lightDay (str): If a team plays on a date where there is a lighter amount of games it has this attribute
        stringStart (str): Position of start date in day-mm/dd format
        stringEnd (str): Position of end date in day-mm/dd format

    '''
    
    def __init__(self,team,date_start = None,date_end = None, totalGames = None, lightDay = None):
        self.team = team
        self.start = date_start
        self.end = date_end
        self.totalGames = totalGames
        self.lightDay = lightDay

        #Needed for django template as processing can't be done there
        if (date_start != None):
            self.stringStart = data['Date'][date_start]
            self.stringEnd = data['Date'][date_end]
    
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

    Attributes:
        start (int): Position of start date in excel sheet
        end (int): Position of end date in excel sheet
    '''
    def __init__(self,start,end):
        self.start = start
        self.end = end



    def teams_with_back(self):
        '''
        Method to calculate teams with back to backs in a week

        Returns:
            list: multi-dimensional list with each cell holding teams that play back to backs on the same date

        '''
        #New list with all NBA Teams
        if (self.start == None) or (self.end == None):
            return None

        nbaTeams = (list(data)[1:31])

        #Counter to retrieve position of team in nba_t list and list of teams with a back to back
        team = 0
        b2b = []

        while team <= 29:
            teamSchedule = (list(data[nbaTeams[team]]))
  
            for game in range (self.start,self.end+1):
                if type(teamSchedule[game]) == str and type(teamSchedule[game+1]) == str:
                    newTeam = Teams((nbaTeams[team]),game,game+1)
                    b2b.append(newTeam)
                else:
                    pass

            team += 1
        #modified bubble sort to sort teams by date the back to back is played
        totalTeams = len(b2b)
        for i in range(totalTeams):
            for j in range (0,totalTeams-i-1):
                if (b2b[j]).start > (b2b[j+1]).start:
                    (b2b[j]), (b2b[j+1])= (b2b[j+1]),(b2b[j])

        totalTeamsWithB2B = []
        if len(b2b) > 0:
            #Loops over teams with back to backs to sort and output teams with back to backs on the same days 
            while (len(b2b)) > 0:
                teamsWithB2B = []

                #sentinel used to find every team with back to backs on the same day
                b2b_start = b2b[0]
                
                for nba_team in range (len(b2b)):
                    # == works here as it compares the start dates to each other 
                    if b2b_start == b2b[nba_team]:
                        teamsWithB2B.append(b2b[nba_team])

                #removing teams that have been sorted for a back to back from original list   
                for sortedTeam in teamsWithB2B:
                    if sortedTeam in b2b:
                        b2b.remove(sortedTeam)

                totalTeamsWithB2B.append(teamsWithB2B)

            return totalTeamsWithB2B

        else:
            return []