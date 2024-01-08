fruit= input()
days= input()
quantity=float(input())
day_is_valid=True
fruit_is_valid=True
price = 0
if days=="Monday" or\
      days=="Tuesday" \
        or days=="Wednesday" \
            or days=="Thursday" \
                or days=="Friday":
    if fruit=="banana":
        price=2.50
    elif fruit=="apple":
        price= 1.20
    elif fruit=="orange":
        price=0.85
    elif fruit=="grapefruit":
        price= 1.45
    elif fruit=="kiwi":
        price= 2.70
    elif fruit=="pineapple":
        price=5.50
    elif fruit=="grapes":
        price= 3.85
    else:
        fruit_is_valid=False
elif days=="Saturday" or days=="Sunday":
    if fruit=="banana":
        price=2.70
    elif fruit=="apple":
        price= 1.25
    elif fruit=="orange":
        price=0.90
    elif fruit=="grapefruit":
        price=1.60
    elif fruit=="kiwi":
        price= 3.00
    elif fruit=="pineapple":
        price=5.60
    elif fruit=="grapes":
        price= 4.20 
    else:
        fruit_is_valid=False
else:
    day_is_valid=False
if day_is_valid==True and fruit_is_valid==True:
 final_price= quantity*price
 print(f"{final_price:.2f}")
else:
    print("error")