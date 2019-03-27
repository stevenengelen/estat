'''
2. Form has a validation for negative readings
3. Form has a validation for non numerical readings
3. Form has a validation for empty readings
4. Form has a validation for wrong format dates
4. Form has a validation for dates in the future
5. Form saves meter reading and date
'''

from electricity.forms import RegisterMeterReadingForm
from django.test import TestCase
from django.utils.html import escape

class RegisterMeterReadingFormTest(TestCase) :

    def test_form_has_reading_input_field(self) :
        reading_form = RegisterMeterReadingForm()
        self.assertIn(escape('reading'), reading_form.as_p())

    def test_form_has_date_input_field(self) :
        reading_form = RegisterMeterReadingForm()
        self.assertIn(escape('date'), reading_form.as_p())

    def test_form_validation_for_negative_readings(self) :
        pass
