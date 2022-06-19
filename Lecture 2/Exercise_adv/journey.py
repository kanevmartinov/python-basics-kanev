budget = float(input())
season = input()
destination = ''
destination_price = 0
accommodation_type = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        destination_price = budget * 0.30
        accommodation_type = 'Camp'
    elif season == 'winter':
        destination_price = budget * 0.70
        accommodation_type = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        destination_price = budget * 0.40
        accommodation_type = 'Camp'
    elif season == 'winter':
        destination_price = budget * 0.80
        accommodation_type = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    destination_price = budget * 0.90
    accommodation_type = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{accommodation_type} - {destination_price:.2f}')
