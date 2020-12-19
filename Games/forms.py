from django import forms
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    start_date = forms.DateField(widget=DateInput,label='Start Date', input_formats= ['%Y-%m-%d'])
    end_date = forms.DateField(widget=DateInput,label='End Date', input_formats=['%Y-%m-%d'])
    nba_start_date = datetime.date(2020,12,22)
    nba_end_date = datetime.date(2021,3,4)

    def clean_start_date(self, *args, **kwargs):
        start_date = self.cleaned_data.get('start_date')
        if ((start_date < self.nba_start_date) or (start_date > (self.nba_end_date - datetime.timedelta(days=1)))):
            raise forms.ValidationError('The start date is not within the NBA season')
        else:
            return start_date

    def clean_end_date(self, *args, **kwargs):
        end_date = self.cleaned_data.get('end_date')
        if ((end_date < (self.nba_start_date + datetime.timedelta(days=1))) or (end_date > self.nba_end_date)):
            raise forms.ValidationError('The end date is not within the NBA season')
        else:
            return end_date



