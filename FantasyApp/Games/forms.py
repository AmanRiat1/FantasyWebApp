from django import forms

class DateForm(forms.Form):
    start_date = forms.DateField(label='Start Date', input_formats= ['%m/%d/%Y'])
    end_date = forms.DateField(label='End Date', input_formats=['%m/%d/%Y'])

    # #Override
    # def clean_start_date(self):
    #     data = self.cleaned_data['start_date']
    #
    #     # if data > data + datetime.timedelta(days=365):
    #     #     raise ValidationError(_('Invalid date - too old'))
    #     return data


