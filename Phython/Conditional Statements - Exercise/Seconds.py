import math
time_first= float(input())
time_second= float(input())
time_third =float(input())
time_sum= time_first+time_second+time_third
minutes = time_sum//60
seconds = time_sum%60
minutes = math.floor(minutes)
seconds= math.floor(seconds)
if seconds<10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")  
