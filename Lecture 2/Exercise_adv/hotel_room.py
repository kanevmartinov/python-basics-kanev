month = input()
number_of_nights = int(input())
studio_price = 0
apartment_price = 0

if month == 'May':
    studio_price = 50
    apartment_price = 65
    if 7 < number_of_nights < 14:
        studio_price *= 0.95
    elif number_of_nights > 14:
        studio_price *= 0.70
        apartment_price *= 0.90
elif month == 'October':
    studio_price = 50
    apartment_price = 65
    if 7 < number_of_nights < 14:
        studio_price *= 0.95
    elif number_of_nights > 14:
        studio_price *= 0.70
        apartment_price *= 0.90
elif month == 'June':
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_nights > 14:
        studio_price *= 0.80
        apartment_price *= 0.90
elif month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_nights > 14:
        studio_price *= 0.80
        apartment_price *= 0.90
elif month == 'July':
    studio_price = 76
    apartment_price = 77
    if number_of_nights > 14:
        apartment_price *= 0.90
elif month == 'August':
    studio_price = 76
    apartment_price = 77
    if number_of_nights > 14:
        apartment_price *= 0.90
total_price_apartment = apartment_price * number_of_nights
total_price_studio = studio_price * number_of_nights

print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')
