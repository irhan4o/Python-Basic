import math
count_t=int(input())
points=int(input())
copy_points=0
br=0
for i in range(1,count_t+1):
    tour=input()
    if tour=="W":
        copy_points+=2000
        br+=1
    elif tour=="F":
        copy_points+=1200
    elif tour=="SF":
     copy_points+=720


total_points=copy_points+points
average_points=copy_points/count_t
win_tour_per=br/count_t*100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{win_tour_per:.2f}%")