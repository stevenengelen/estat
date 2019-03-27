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

READING = 15
DATE = '2019-03-27'

class MeterReadingsTest(TestCase) :

    def test_can_save_correct_count_reading(self) :
        reading = MeterReading.objects.create(date = DATE, reading = READING)
        self.assertEqual(len(MeterReading.objects.all()), 1, msg = 'count of meter reading database objects is not correct')

    def test_can_save_correct_reading(self) :
        # first test if the database is empty
        # TODO
        reading = MeterReading.objects.create(date = DATE, reading = READING)
        self.assertQuerysetEqual(MeterReading.objects.all(), [ '<' . DATE . READING . '>' ], msg = 'reading not saved correct')

    def test_can_save_correct_reading_using_factory(self) :
        # meter_reading_pk = MeterReadings().new(READING, DATE)
        # self.assertIn('2019-03-23', meter_reading.date)
        # self.assertEqual(15, meter_reading.reading, msg = 'reading not saved')
        pass

    def test_can_get_correct_reading(self) :
        pass
