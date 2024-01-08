import sys
max=-sys.maxsize
command=input()
while command!="Stop":
    current_number =int(command)
    if current_number>max:
        max=current_number
    command=input()
print(max)