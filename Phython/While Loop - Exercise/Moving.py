width=int(input())
lenght=int(input())
height=int(input())

volume=width*lenght*height

sum_boxes=0
input_line=input()
while input_line!="Done":
    boxes=int(input_line)

    sum_boxes+=boxes

    if sum_boxes>=volume:
        break

    input_line=input()
diff=abs(sum_boxes-volume)
if sum_boxes>=volume:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")