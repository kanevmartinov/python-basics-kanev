product = input()
city = input()
quantity = float(input())
price = 0

if city == 'Sofia':
    if product == 'coffee':
        price = 0.50
        final_price = price * quantity
        print(final_price)
    elif product == 'water':
        price = 0.80
        final_price = price * quantity
        print(final_price)
    elif product == 'beer':
        price = 1.20
        final_price = price * quantity
        print(final_price)
    elif product == 'sweets':
        price = 1.45
        final_price = price * quantity
        print(final_price)
    elif product == 'peanuts':
        price = 1.60
        final_price = price * quantity
        print(final_price)
elif city == 'Plovdiv':
    if product == 'coffee':
        price = 0.40
        final_price = price * quantity
        print(final_price)
    elif product == 'water':
        price = 0.70
        final_price = price * quantity
        print(final_price)
    elif product == 'beer':
        price = 1.15
        final_price = price * quantity
        print(final_price)
    elif product == 'sweets':
        price = 1.30
        final_price = price * quantity
        print(final_price)
    elif product == 'peanuts':
        price = 1.50
        final_price = price * quantity
        print(final_price)
elif city == 'Varna':
    if product == 'coffee':
        price = 0.45
        final_price = price * quantity
        print(final_price)
    elif product == 'water':
        price = 0.70
        final_price = price * quantity
        print(final_price)
    elif product == 'beer':
        price = 1.10
        final_price = price * quantity
        print(final_price)
    elif product == 'sweets':
        price = 1.35
        final_price = price * quantity
        print(final_price)
    elif product == 'peanuts':
        price = 1.55
        final_price = price * quantity
        print(final_price)
