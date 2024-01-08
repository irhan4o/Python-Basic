import sys
min=sys.maxsize
command=input()
while command!="Stop":
    current_number=int(command)
    if current_number<min:
        min=current_number   
    command=input()    
print(min)
