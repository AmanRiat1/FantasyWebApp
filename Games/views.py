from django.shortcuts import render
from .forms import DateForm
from .app_code import main_schedule as schedule
import datetime

#TODO: further encapsulate code

def index(request):
    if request.method == 'POST':
        form = DateForm(request.POST)

        if form.is_valid():
            rawStartDate = form.cleaned_data['start_date']
            rawEndDate = form.cleaned_data['end_date']

            start_date = schedule.convert_time(rawStartDate)
            end_date = schedule.convert_time(rawEndDate)

            #Where the date is in the spreadsheet
            startPos = schedule.game_position(start_date)
            endPos = schedule.game_position(end_date)

            #Processing of total games and related information
            form.start = start_date
            form.end = end_date
            form.totalNumberOfGames = schedule.games_played(startPos, endPos)

            teamsWithBackToBack = schedule.BackToBack(startPos, endPos)
            form.totalTeamsWithBack = teamsWithBackToBack.teams_with_back()

            form.lightGameDays =  schedule.light_game_days(startPos, endPos)

    else:
        form = DateForm()

        # Starting at the beginning of the week, code below finds monday and then sunday of the week
        today = datetime.date.today()
        nearestMonday = today - datetime.timedelta(days=today.weekday())
        sunday = nearestMonday + datetime.timedelta(days=6)

        form.start = schedule.convert_time(nearestMonday)
        form.end = schedule.convert_time(sunday)

        startPos = schedule.game_position(form.start)
        endPos = schedule.game_position(form.end)

        form.totalNumberOfGames = schedule.games_played(startPos, endPos)

        teamsWithBackToBack = schedule.BackToBack(startPos, endPos)
        form.totalTeamsWithBack = teamsWithBackToBack.teams_with_back()

        form.lightGameDays = schedule.light_game_days(startPos, endPos)


    context = {
        'form': form
    }

    return render(request,'Games/all_info.html', context)

#
#
#
#
#
#
#
