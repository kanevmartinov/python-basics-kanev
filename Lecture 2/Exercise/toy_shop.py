# prices
vacation_price = float(input())
puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

# quantities
puzzle_quantity = int(input())
doll_quantity = int(input())
bears_quantity = int(input())
minions_quantity = int(input())
trucks_quantity = int(input())

# calculations
revenue = puzzle_quantity * puzzle_price + doll_quantity * doll_price + bears_quantity * bear_price + \
          minions_quantity * minion_price + trucks_quantity * truck_price

toys_quantity = puzzle_quantity + doll_quantity + bears_quantity + minions_quantity + trucks_quantity

if toys_quantity > 50:
    discount = revenue * 0.25
else:
    discount = 0

final_price = revenue - discount
rent = final_price * 0.10
profit = final_price - rent

if profit > vacation_price:
    left_money = profit - vacation_price
    print(f'Yes! {left_money:.2f} lv left.')
elif profit < vacation_price:
    left_money = vacation_price - profit
    print(f'Not enough money! {left_money:.2f} lv needed.')
