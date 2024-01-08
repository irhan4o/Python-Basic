same_txt=input()
sum_of_point=0
for letter in same_txt:
    if letter=="a":
        sum_of_point+=1
    elif letter=="e":
        sum_of_point+=2
    elif letter=="i":
        sum_of_point+=3
    elif letter=="o":
        sum_of_point+=4
    elif letter=="u":
        sum_of_point+=5

print(sum_of_point)
