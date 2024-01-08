budget = float(input())
season = input()
type_house=""
place=""
expenses=0

if budget<=100:
 place="Bulgaria"
 if season=="summer":
  expenses=budget*0.30
  type_house="Camp"
 elif season=="winter":
   expenses=budget*0.70
   type_house="Hotel"
elif budget<=1000:
 place="Balkans"
 if season=="summer":
  expenses=budget*0.40
  type_house="Camp"
 elif season=="winter":
   expenses=budget*0.80
   type_house="Hotel"
elif budget>1000:
 place="Europe"
 expenses=budget*0.90
 type_house="Hotel"


print(f"Somewhere in {place}\n{type_house} - {expenses:.2f}")
