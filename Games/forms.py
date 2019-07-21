from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    start_date = forms.DateField(widget=DateInput,label='Start Date', input_formats= ['%Y-%m-%d'])
    end_date = forms.DateField(widget=DateInput,label='End Date', input_formats=['%Y-%m-%d'])



