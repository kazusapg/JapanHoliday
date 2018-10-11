import unittest
from japan_holiday import JapanHoliday

CSV_FILE_NAME = 'syukujitsu_kyujitsu.csv'


class TestReadHoliday(unittest.TestCase):

    def test__read_holiday(self):
        jpholiday = JapanHoliday(CSV_FILE_NAME)
        self.assertEqual(len(jpholiday._holidays), 55)
        self.assertEqual(jpholiday._holidays['2017-01-01']['day'], '2017-01-01')
        self.assertEqual(jpholiday._holidays['2017-01-01']['name'], '元日')

    def test__read_holiday_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            jpholiday = JapanHoliday('filenotfound.csv')

    def test__read_holiday_wrong_encode(self):
        with self.assertRaises(UnicodeDecodeError):
            jpholiday = JapanHoliday(CSV_FILE_NAME, encoding='utf-8')


class TestIsHoliday(unittest.TestCase):
    def setUp(self):
        self.jpholiday = JapanHoliday(CSV_FILE_NAME)

    def test_is_holiday(self):
        self.assertTrue(self.jpholiday.is_holiday('2018-01-01'))  # 元日（祝）
        self.assertTrue(self.jpholiday.is_holiday('2018-01-06'))  # 土曜日
        self.assertTrue(self.jpholiday.is_holiday('2018-01-07'))  # 日曜日
        self.assertFalse(self.jpholiday.is_holiday('2018-01-09'))  # 火曜日

    def test_is_holiday_wrong_day_format(self):
        with self.assertRaises(ValueError):
            self.jpholiday.is_holiday('2018/01/01')


class TestGetHolidayList(unittest.TestCase):
    def test_get_holiday_dict(self):
        jpholiday = JapanHoliday(CSV_FILE_NAME)
        self.assertEqual(len(jpholiday.get_holiday_dict()), 55)
        self.assertEqual(jpholiday._holidays['2017-01-01']['day'], '2017-01-01')
        self.assertEqual(jpholiday._holidays['2017-01-01']['name'], '元日')


if __name__ == '__main__':
    unittest.main()
