import sys


n =int(input())
min=sys.maxsize
max=-sys.maxsize
for index in range(n):
 number = int(input())
 if(max<number):max=number
 if(min>number):min=number

print(f"Max number: {max}")
print(f"Min number: {min}")