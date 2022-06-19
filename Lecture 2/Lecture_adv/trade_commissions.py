city_name = input()
sales_volume = float(input())

if city_name == 'Sofia':
    if sales_volume < 0:
        print('error')
    elif sales_volume <= 500:
        commission_percentage_calculation = sales_volume * 0.05
        print(f'{commission_percentage_calculation:.2f}')
    elif sales_volume <= 1000:
        commission_percentage_calculation = sales_volume * 0.07
        print(f'{commission_percentage_calculation:.2f}')
    elif sales_volume <= 10000:
        commission_percentage_calculation = sales_volume * 0.08
        print(f'{commission_percentage_calculation:.2f}')
    elif sales_volume > 10000:
        commission_percentage_calculation = sales_volume * 0.12
        print(f'{commission_percentage_calculation:.2f}')

elif city_name == 'Varna':
    if sales_volume < 0:
        print('error')
    elif sales_volume <= 500:
        commission_percentage_calculation = sales_volume * 0.045
        print(f'{commission_percentage_calculation:.2f}')
    elif sales_volume <= 1000:
        commission_percentage_calculation = sales_volume * 0.075
        print(f'{commission_percentage_calculation:.2f}')
    elif sales_volume <= 10000:
        commission_percentage_calculation = sales_volume * 0.10
        print(f'{commission_percentage_calculation:.2f}')
    elif sales_volume > 10000:
        commission_percentage_calculation = sales_volume * 0.13
        print(f'{commission_percentage_calculation:.2f}')

elif city_name == 'Plovdiv':
    if sales_volume < 0:
        print('error')
    elif sales_volume <= 500:
        commission_percentage_calculation = sales_volume * 0.055
        print(f'{commission_percentage_calculation:.2f}')
    elif sales_volume <= 1000:
        commission_percentage_calculation = sales_volume * 0.08
        print(f'{commission_percentage_calculation:.2f}')
    elif sales_volume <= 10000:
        commission_percentage_calculation = sales_volume * 0.12
        print(f'{commission_percentage_calculation:.2f}')
    elif sales_volume > 10000:
        commission_percentage_calculation = sales_volume * 0.145
        print(f'{commission_percentage_calculation:.2f}')
else:
    print('error')
