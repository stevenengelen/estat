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
from electricity.models import MeterReading
from electricity.tests.test_models import DATE, READING
from datetime import datetime, timedelta
from unittest import skip

class RegisterMeterReadingFormTest(TestCase) :

    def test_form_has_reading_input_field(self) :
        reading_form = RegisterMeterReadingForm()
        self.assertIn(escape('reading'), reading_form.as_p())

    def test_form_has_date_input_field(self) :
        reading_form = RegisterMeterReadingForm()
        self.assertIn(escape('date'), reading_form.as_p())

    def test_form_saves_reading(self) :
        form = RegisterMeterReadingForm(data = { 'date' : DATE, 'reading' : READING })
        assert(form.is_valid())
        meter_reading = form.save()
        stored_meter_reading = MeterReading.objects.first()
        self.assertEqual(str(stored_meter_reading.date), DATE, msg = 'form does not save date correctly')
        self.assertEqual(stored_meter_reading.reading, READING, msg = 'form does not save reading correctly')

    def test_form_validation_rejects_date_in_the_future(self) :
        # create a date tomorrow
        # this formats the today variable to  YYYY-MM-DD
        tomorrow = datetime.today() + timedelta(days = 1)
        date_tomorrow = str(tomorrow)[:10]
        reading_form = RegisterMeterReadingForm(data = { 'date' : date_tomorrow, 'reading' : READING })
        self.assertFalse(reading_form.is_valid())
        self.assertIn('You can not submit a reading made in the future', reading_form.errors['date'], msg = 'form does not contain date field error message: You can not submit a reading made in the future')

    def test_form_validation_rejects_negative_readings(self) :
        reading_form = RegisterMeterReadingForm(data = { 'date' : DATE, 'reading' : -READING })
        self.assertFalse(reading_form.is_valid())
        self.assertIn('The meter is not capable to display a negative electricity consumation, so a negative reading is not possible', reading_form.errors['reading'], msg = 'form does not contain reading field error message: The meter is not capable to display a negative electricity consumation, so a negative reading is not possible.')

    def test_form_validation_requires_a_reading(self) :
        reading_form = RegisterMeterReadingForm(data = { 'date' : DATE, 'reading' : '' })
        self.assertFalse(reading_form.is_valid())
        self.assertIn('Please enter a reading', reading_form.errors['reading'], msg = 'form does not contain reading field error message: Please enter a reading')
