needed_money=float(input())
intit_money=float(input())

count_spend=0
all_days_count=0
while intit_money<needed_money:
    if count_spend==5:
        break
    action=input()
    amount=float(input())
    all_days_count+=1
    if action=="spend":
        count_spend+=1
        intit_money-=amount
        if intit_money<0:
            intit_money=0
    elif action=="save":
        count_spend=0
        intit_money+=amount

if count_spend==5:
    print("You can't save the money.")
    print(all_days_count)
else:
    print(f"You saved the money for {all_days_count} days.")