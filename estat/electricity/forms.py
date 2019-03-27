from django import forms
from .models import MeterReading

class RegisterMeterReadingForm(forms.ModelForm) :
    '''
    Form for entering a meter reading
    '''
    class Meta :
        model = MeterReading
        fields = [ 'date', 'reading' ]
    # input_reading = forms.FloatField(label = 'Meter reading: ', required = True, help_text = 'Enter the meter reading')
    # input_date = forms.DateField(label = 'Date reading: ', required = True, help_text = 'Enter the date on which teh meter reading was taken')
