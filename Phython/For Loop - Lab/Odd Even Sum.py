n = int(input())
sum_Odd=0
sum_Even=0
for number in range(n):
 current_number=int(input())
 if number%2==0:
  sum_Even+=current_number
 else:
  sum_Odd+=current_number

if sum_Odd==sum_Even:
  print(f"Yes")
  print(f"Sum = {sum_Even}")
else:
 diff =abs(sum_Even-sum_Odd)
 print("No")
 print(f"Diff = {diff}")

