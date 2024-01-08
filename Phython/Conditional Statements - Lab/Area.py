from math import pi
figuri = input()
result =0
if figuri=="square":
 side_a = float(input())
 result = side_a*side_a
elif figuri=="rectangle":
 first_side= float(input())
 secound_side = float(input())
 result=first_side*secound_side
elif figuri=="circle":
 side = float(input())
 result= pi*(side**2)
else:
 starna1= float(input())
 h = float(input())
 result= (starna1*h)/2

print(f"{result:.3f}")