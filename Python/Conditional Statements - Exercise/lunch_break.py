import math
name_series = input()
duration_ep= int(input())
duration_break= int(input())
duration_lunch = duration_break*1/8
duration_relax = duration_break*1/4
left_time = duration_break-(duration_lunch+duration_relax)
if left_time == duration_ep:
    print(f"You have enough time to watch {name_series} and left with 0 minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, you need {math.ceil(duration_ep-left_time)} more minutes.")