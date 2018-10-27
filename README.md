# JapanHoliday
内閣府が公表している祝日のCSVを使用して
入力された日付が休日または祝日か判定します

# 使用方法
japan_holiday.pyと祝日のcsvを同じフォルダに置いて使用します。 
```
from japan_holiday import JapanHoliday

holiday = JapanHoliday()
```

デフォルトでpythonファイルと同じ場所のsyukujitsu_kyujitsu.csvを読み込みます。  
パスが違う場合は引数のpathにcsvのファイルパスを入力します。  
```
holiday = JapanHoliday(path='C:\\holiday.csv')
```

デフォルトのエンコーディングはcp932です。  
cp932以外の文字コードを使用するときは、encodingに使用する文字コードを指定します。
```
holiday = JapanHoliday(encoding='utf-8')
```

ファイルパスと文字コードを同時に指定したいときは以下のように入力します
```
holiday = JapanHoliday('C:\\holiday.csv', 'utf-8')
```

is_holidayメソッドで平日か休日・祝日を判定します。
```
print(holiday.is_holiday('2018-01-04'))  # 平日木曜日なのでFalse
print(holiday.is_holiday('2018-01-06'))  # 土曜日なのでTrue
print(holiday.is_holiday('2018-01-07'))  # 日曜日なのでTrue
print(holiday.is_holiday('2018-01-07'))  # 祝日成人の日なのでTrue
```

get_holiday_dictメソッドで祝日の一覧をdict形式で取得します。
```
holiday_dict = holiday.get_holiday_dict()  # 祝日一覧を取得
print(holiday_dict['2017-01-01']['day'])  # 2017-01-01
print(holiday_dict['2017-01-01']['name'])  # 元日
```