from japan_holiday import JapanHoliday

holiday = JapanHoliday()
print(holiday.is_holiday('2018-01-04'))  # 平日木曜日なのでTrue
print(holiday.is_holiday('2018-01-06'))  # 土曜日なのでTrue
print(holiday.is_holiday('2018-01-07'))  # 日曜日なのでTrue
print(holiday.is_holiday('2018-01-07'))  # 祝日成人の日なのでTrue

holiday_dict = holiday.get_holiday_dict()  # 祝日一覧を取得
print(holiday_dict['2017-01-01']['day'])  # 2017-01-01
print(holiday_dict['2017-01-01']['name'])  # 元日
