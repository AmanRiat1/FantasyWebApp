from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    start_date = forms.DateField(widget=DateInput,label='Start Date', input_formats= ['%Y-%m-%d'])
    end_date = forms.DateField(widget=DateInput,label='End Date', input_formats=['%Y-%m-%d'])

    # #Override
    # def clean_start_date(self):
    #     data = self.cleaned_data['start_date']
    #
    #     # if data > data + datetime.timedelta(days=365):
    #     #     raise ValidationError(_('Invalid date - too old'))
    #     return data


