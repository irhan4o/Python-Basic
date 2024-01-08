# Четене на входните данни
days = int(input())
room_type = input()
feedback = input()

# Инициализация на променливи за цената на нощувка и броя на нощувките
price_per_night = 0
nights = days - 1

# Определяне на цената на нощувката в зависимост от видът на помещението
if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

# Изчисляване на общата цена преди намаления
total_before_discount = nights * price_per_night

# Прилагане на намаления в зависимост от броя на нощувките
if nights < 10:
    # Няма намаление за всички видове помещения
    pass
elif 10 <= nights <= 15:
    # Намаление за apartment
    if room_type == "apartment":
        total_before_discount *= 0.65  # 35% отстъпка
    # Намаление за president apartment
    elif room_type == "president apartment":
        total_before_discount *= 0.85  # 15% отстъпка
else:
    # Намаление за apartment
    if room_type == "apartment":
        total_before_discount *= 0.50  # 50% отстъпка
    # Намаление за president apartment
    elif room_type == "president apartment":
        total_before_discount *= 0.80  # 20% отстъпка

# Прилагане на оценката за услугите на хотела
final_price = 0

if feedback == "positive":
    final_price = total_before_discount * 1.25  # 25% надценка
elif feedback == "negative":
    final_price = total_before_discount * 0.90  # 10% отстъпка

# Извеждане на резултата
print(f"{final_price:.2f}")