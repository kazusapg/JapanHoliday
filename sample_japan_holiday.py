from japan_holiday import JapanHoliday

holiday = JapanHoliday()

print(holiday.is_holiday('2018-01-04'))  # 平日木曜日なのでFalse
print(holiday.is_holiday('2018-01-06'))  # 土曜日なのでTrue
print(holiday.is_holiday('2018-01-07'))  # 日曜日なのでTrue
print(holiday.is_holiday('2018-01-07'))  # 祝日成人の日なのでTrue

holiday_dict = holiday.get_holiday_dict()  # 祝日一覧を取得
print(holiday_dict['2017-01-01']['day'])  # 2017-01-01
print(holiday_dict['2017-01-01']['name'])  # 元日

# デフォルトではpythonファイルと同じ場所のsyukujitsu_kyujitsu.csvを読み込みます
# パスが違う場合はpathにcsvのファイルパスを入力します。
# holiday_another = JapanHoliday(path='C:\\holiday.csv')

# デフォルトのエンコーディングはcp932です。
# cp932以外の文字コードを使用するときは、encodingに使用する文字コードを指定します。
# holiday_another = JapanHoliday(encoding='utf-8')

# ファイルパスと文字コードの指定例
# # holiday_another = JapanHoliday('C:\\holiday.csv', 'utf-8')
