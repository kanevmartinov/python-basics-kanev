film_budget = float(input())
statists_quantity = int(input())
statists_clothing_price = float(input())

decor_cost = film_budget * 0.10
clothing_cost = statists_quantity * statists_clothing_price

if statists_quantity > 150:
    clothing_cost *= 0.9

film_cost = decor_cost + clothing_cost
difference = abs(film_budget - film_cost)

if film_cost > film_budget:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
elif film_cost <= film_budget:
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')
