import datetime

from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import FormView



class DateForm(forms.Form):
    start_date = forms.DateField(label='Start Date', input_formats= ['%m/%d/%Y'])
    end_date = forms.DateField(help_text="Enter a date 7 days away", label='End Date', input_formats=['%m/%d/%Y'])

    # #Override
    # def clean_start_date(self):
    #     data = self.cleaned_data['start_date']
    #
    #     # if data > data + datetime.timedelta(days=365):
    #     #     raise ValidationError(_('Invalid date - too old'))
    #     return data

#
# class EndForm(forms.Form):
#     end_date = forms.DateField(help_text="Enter a date 7 days away", label='End Date', input_formats= ['%m/%d/%Y'])
#
#     def clean_end_date(self,startDate):
#     #TODO add docstrings + start-date type
#         data = self.cleaned_data['end_date']
#
#         # if data > startDate.start_date + datetime.timedelta(days=7):
#         #     raise ValidationError(_('Game range should be within a week'))
#         return data

