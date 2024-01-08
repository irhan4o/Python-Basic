budget= float(input())
count_statists=int(input())
price_clothing= float(input())
decor= budget*0.1
sum_clothing = count_statists*price_clothing
if count_statists>150:
   sum_clothing=sum_clothing*0.90 

expenses = decor+sum_clothing
diff=abs(expenses-budget)
if expenses<=budget:
   print("Action!")
   print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")