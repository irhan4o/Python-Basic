first_number = int(input())
second_number=int(input())
operator = input()
result=0
zero_flag=False
odd_or_even=""
if operator=="+":
 result= first_number+second_number
elif operator=="-":
 result= first_number-second_number
elif operator=="*":
 result= first_number*second_number
elif operator=="/":
 if second_number==0:
  zero_flag=True
 else:
  result=first_number/second_number
elif operator=="%":
 if second_number==0:
  zero_flag=True
 else:
  result=first_number%second_number

if zero_flag:
 print(f"Cannot divide {first_number} by zero")
elif operator=="+"or operator=="-"or operator=="*":
  if result%2==0:
   odd_or_even="even"
  else:
   odd_or_even="odd"
  print(f"{first_number} {operator} {second_number} = {result} - {odd_or_even}")
elif operator=="%":
 print(f"{first_number} {operator} {second_number} = {result} ")
elif operator=="/":
  print(f"{first_number} {operator} {second_number} = {result:.2f}")