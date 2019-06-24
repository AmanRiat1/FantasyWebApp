from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

from .forms import StartForm,EndForm

from .static.Games import main_schedule as schedule


def index(request):
    latest_question_list = 'hey'
    template = loader.get_template('Games/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def process(request):
    if request.method == 'POST':
        formStart = StartForm(request.POST)
        formEnd = EndForm(request.POST)

        if formStart.is_valid() and formEnd.is_valid():
            rawStartDate = formStart.cleaned_data['start_date']
            rawEndDate = formEnd.cleaned_data['end_date']

            start_date = schedule.convert_time(rawStartDate)
            end_date = schedule.convert_time(rawEndDate)

            #Where the date is in the spreadsheet
            startPos = schedule.game_position(start_date)
            endPos = schedule.game_position(end_date)

            #Processing of total games
            totalNumberOfGames = schedule.games_played(startPos, endPos)
            #PICKUP FROM HERE 




