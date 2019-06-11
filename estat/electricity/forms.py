from django import forms
from .models import MeterReading
from .utilities import Utilities

class RegisterMeterReadingForm(forms.ModelForm) :
    '''
    Form for entering a meter reading
    '''
    class Meta :
        model = MeterReading
        # TODO date and reading should be made required
        # or are they already because in model blank is False?
        fields = '__all__'

    error_css_class = 'error'
    required_css_class = 'required'

    def clean_date(self) :
        date = self.cleaned_data.get('date')
        if Utilities.date_is_in_the_future(date) :
            raise forms.ValidationError('You can not submit a reading made in the future', code = 'future_date_not_allowed')
        return date
