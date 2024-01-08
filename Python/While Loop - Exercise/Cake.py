width = int(input())
lenght=int(input())
total_pieces=width*lenght
input_line =input()
while input_line!="STOP":
    pieces=int(input_line)
    total_pieces=total_pieces-pieces
    if total_pieces<0:
        break
    input_line=input()

if total_pieces<0:
   print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
   print(f"{total_pieces} pieces are left.")