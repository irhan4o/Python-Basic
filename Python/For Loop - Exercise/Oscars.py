name_actor = input()
point=float(input())
count_evaluative=int(input())
result=0
total_points=point
for i in range(1,count_evaluative+1):
    evaluative =input()
    points_evaluative=float(input())

    points =(len(evaluative)*points_evaluative)/2
    total_points =total_points+points
    if total_points>=1250.5:
        break
 
if total_points>=1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff=1250.5-total_points
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")