price_excursion= float(input())
count_pizzles= int(input())
count_dolls=int(input())
count_teddyBears= int(input())
count_minions= int(input())
count_truks = int(input())
sum = count_pizzles*2.60+count_dolls*3+count_teddyBears*4.10+count_minions*8.20+count_truks*2
count = count_pizzles+count_dolls+count_teddyBears+count_minions+count_truks
if count>=50:
    sum = sum *0.75
sum = sum*0.90
diff=abs(sum-price_excursion)
if sum>=price_excursion:
  print(f"Yes! {diff:.2f} lv left.")
else:
   print(f"Not enough money! {diff:.2f} lv needed.")