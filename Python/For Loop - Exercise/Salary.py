open_webtab = int(input())
salary=int(input())
copy_salary=salary
for i in range(1,open_webtab+1):
    web_tab = input()
    if web_tab=="Facebook":
        copy_salary=copy_salary-150
    elif web_tab=="Instagram":
        copy_salary =copy_salary-100
    elif web_tab=="Reddit":
        copy_salary=copy_salary-50
    
    if copy_salary<=0:
        break

if copy_salary<=0:
    print("You have lost your salary.")
else:
    print(copy_salary)
    

