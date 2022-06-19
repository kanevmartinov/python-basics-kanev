group_budget = int(input())
season = input()
fisherman = int(input())
boat_rent_price = 0

if season == 'Spring':
    boat_rent_price = 3000
    if fisherman <= 6:
        boat_rent_price *= 0.90
    elif 11 >= fisherman > 7:
        boat_rent_price *= 0.85
    elif fisherman >= 12:
        boat_rent_price *= 0.75
    if fisherman % 2 == 0:
        boat_rent_price *= 0.95
elif season == 'Summer':
    boat_rent_price = 4200
    if fisherman <= 6:
        boat_rent_price *= 0.90
    elif 11 >= fisherman > 7:
        boat_rent_price *= 0.85
    elif fisherman >= 12:
        boat_rent_price *= 0.75
    if fisherman % 2 == 0:
        boat_rent_price *= 0.95
elif season == 'Autumn':
    boat_rent_price = 4200
    if fisherman <= 6:
        boat_rent_price *= 0.90
    elif 11 >= fisherman > 7:
        boat_rent_price *= 0.85
    elif fisherman >= 12:
        boat_rent_price *= 0.75
elif season == 'Winter':
    boat_rent_price = 2600
    if fisherman <= 6:
        boat_rent_price *= 0.90
    elif 11 >= fisherman > 7:
        boat_rent_price *= 0.85
    elif fisherman >= 12:
        boat_rent_price *= 0.75
    if fisherman % 2 == 0:
        boat_rent_price *= 0.95

left_sum = abs(group_budget - boat_rent_price)

if group_budget >= boat_rent_price:
    print(f"Yes! You have {left_sum:.2f} leva left.")
else:
    print(f"Not enough money! You need {left_sum:.2f} leva.")