flower_type = input()
flower_quantity = int(input())
budget = int(input())
roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50
total_price = 0

if flower_type == 'Roses':
    total_price = flower_quantity * roses_price
    if flower_quantity > 80:
        total_price *= 0.9
    else:
        pass
elif flower_type == 'Dahlias':
    total_price = flower_quantity * dahlias_price
    if flower_quantity > 90:
        total_price *= 0.85
    else:
        pass
elif flower_type == 'Tulips':
    total_price = flower_quantity * tulips_price
    if flower_quantity > 80:
        total_price *= 0.85
    else:
        pass
elif flower_type == 'Narcissus':
    if flower_quantity < 120:
        total_price = (flower_quantity * narcissus_price) + (flower_quantity * narcissus_price) * (15/100)
    else:
        total_price = flower_quantity * narcissus_price
elif flower_type == 'Gladiolus':
    if flower_quantity < 120:
        total_price = (flower_quantity * gladiolus_price) + (flower_quantity * gladiolus_price) * (20/100)
    else:
        total_price = flower_quantity * gladiolus_price

left_sum = abs(total_price - budget)

if total_price > budget:
    print(f'Not enough money, you need {left_sum:.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {flower_quantity} {flower_type} and {left_sum:.2f} leva left.')
