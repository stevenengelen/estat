'''
1. Test can not save negative reading
2. Can not save empty reading
3. Can not save wrong date format
4. Can not save empty date
5. Can save correct date and reading
'''
from django.test import TestCase
from electricity.models import MeterReading
from electricity.models import MeterReadings
from datetime import datetime
from datetime import timedelta
from unittest import skip

READING = 15.0
DATE = '2019-03-27'
TOMORROW = str(datetime.today() + timedelta(days = 1))[:10]

class MeterReadingsTest(TestCase) :

    def check_if_db_is_empty(self) :
        '''
        checks if the database is empty, and asserts if not
        '''
        self.assertEqual(len(MeterReading.objects.all()), 0, msg = 'database is not empty')

    def test_can_save_correct_count_reading(self) :
        self.check_if_db_is_empty()

        MeterReading.objects.create(date = DATE, reading = READING)
        self.assertEqual(len(MeterReading.objects.all()), 1, msg = 'meter reading is not saved in database')

    def test_can_save_correct_reading(self) :
        self.check_if_db_is_empty()

        meter_reading = MeterReading.objects.create(date = DATE, reading = READING)
        self.assertEqual(meter_reading, MeterReading.objects.first(), msg = 'reading not saved correct')

    def test_can_save_correct_reading_using_factory(self) :
        self.check_if_db_is_empty()

        meter_reading_pk = MeterReadings().new(DATE, READING)
        meter_reading = MeterReading.objects.filter(pk = meter_reading_pk)
        self.assertEqual(meter_reading.first().pk, meter_reading_pk)
        self.assertEqual(str(meter_reading.first().date), DATE)
        self.assertEqual(meter_reading.first().reading, READING)

    def test_can_get_correct_reading(self) :
        meter_reading_pk = MeterReadings().new(DATE, READING)
        meter_reading = MeterReadings().get(meter_reading_pk)
        self.assertEqual(meter_reading.pk, meter_reading_pk, msg = 'can not get a correct pk from the db')
        self.assertEqual(str(meter_reading.date), DATE, msg = 'can not get a correct date from the db')
        self.assertEqual(meter_reading.reading, READING, msg = 'can not get a correct reading from the db')

    def test_can_not_save_negative_reading(self) :
        self.check_if_db_is_empty()

        meter_reading = MeterReading.objects.create(date = DATE, reading = -READING)
        self.assertEqual(len(MeterReading.objects.all()), 0, msg = 'database contains a negative reading')

    def test_can_not_save_date_in_the_future(self) :
        self.check_if_db_is_empty()

        meter_reading = MeterReading.objects.create(date = TOMORROW, reading = READING)
        self.assertEqual(len(MeterReading.objects.all()), 0, msg = 'database contains a reading of the future')

    def test_can_not_save_empty_reading(self) :
        self.check_if_db_is_empty()

        meter_reading = MeterReading.objects.create(date = DATE, reading = None)
        self.assertEqual(len(MeterReading.objects.all()), 0, msg = 'database contains an empty reading')
