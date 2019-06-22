from django.shortcuts import render

from django.http import HttpResponse

from Games.forms import StartForm,EndForm

from Games.static.Games import main_schedule as schedule

from

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def process(request):
    if request.method == 'POST':
        formStart = StartForm(request.POST)
        formEnd = EndForm(request.POST)

        if formStart.is_valid() and formEnd.is_valid():
            raw_start_date = formStart.cleaned_data['start_date']
            raw_end_date = formEnd.cleaned_data['end_date']

            start_date = schedule.convertTime(raw_start_date)
            end_date = schedule.convertTime(raw_end_date)

            #Where the date is in the spreadsheet
            start_pos = schedule.game_position(start_date)
            end_pos = schedule.game_position(end_date)

            #Processing of total games
            #PICKUP FROM HERE 




