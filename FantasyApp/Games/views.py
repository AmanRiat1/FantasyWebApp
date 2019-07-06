from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import DateForm
from django.template import loader

from .static.Games import main_schedule as schedule


def index(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        #formEnd = EndForm(request.POST)

        if form.is_valid():
            rawStartDate = form.cleaned_data['start_date']
            rawEndDate = form.cleaned_data['end_date']

            start_date = schedule.convert_time(rawStartDate)
            end_date = schedule.convert_time(rawEndDate)

            #Where the date is in the spreadsheet
            startPos = schedule.game_position(start_date)
            endPos = schedule.game_position(end_date)

            #Processing of total games
            form.start = start_date
            form.end = end_date
            form.totalNumberOfGames = schedule.games_played(startPos, endPos)

            teamsWithBackToBack = schedule.BackToBack(startPos, endPos)
            form.totalTeamsWithBack = teamsWithBackToBack.teams_with_back()

            form.lightGameDays =  schedule.week_games(startPos, endPos)

    else:
        form = DateForm()


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
