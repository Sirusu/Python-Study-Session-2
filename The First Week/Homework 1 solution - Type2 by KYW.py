# Type 2의 2번째 문제를 모듈을 사용한 풀이 입니다.

# input Month Day
a=4; b=12

# find week
import calendar
weeks=["MON","TUE","WED","THU","FRI","SAT","SUN"]
weeks[calendar.weekday(2016, a, b)]

# 월과 일이 초과될 경우 error ValueError: day is out of range for month가 표시 됩니다.
