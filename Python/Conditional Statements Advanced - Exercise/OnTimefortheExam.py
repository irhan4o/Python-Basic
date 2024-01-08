exam_hour=int(input())
exam_min = int(input())
arrival_hour=int(input())
arrival_min=int(input())

exam_all_min=(exam_hour*60)+exam_min
arrival_all_min=(arrival_hour*60)+arrival_min

diff =abs(exam_all_min-arrival_all_min)
if arrival_all_min>exam_all_min:
    print("Late")
    if diff<60:
        print(f"{diff} minutes after the start")
    else:
        hour=diff//60
        minutes=diff%60
        if minutes<10:
         print(f"{hour}:0{minutes} hours after the start")
        else:
            print(f"{hour}:{minutes} hours after the start")
elif arrival_all_min==exam_all_min or diff<=30:
    print("On Time")
    if diff>=1 and diff<=30:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff<60:
       print(f"{diff} minutes before the start")
    else:
        hour = diff//60
        minutess=diff%60
        if minutess<10:
            print(f"{hour}:0{minutess} hours before the start")
        else:
            print(f"{hour}:{minutess} hours before the start")



