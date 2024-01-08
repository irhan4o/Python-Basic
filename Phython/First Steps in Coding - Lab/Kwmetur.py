kw = float(input())
total_sum = kw*7.61
total_sum_otstupka= total_sum*0.82
discount = total_sum-total_sum_otstupka
print(f"The final price is: {round(total_sum_otstupka,2)} lv.")
print(f"The discount is: {round(discount,2)} lv.")