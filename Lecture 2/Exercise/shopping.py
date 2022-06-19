# input_quantities
budget = float(input())
gpu_quantity = int(input())
cpu_quantity = int(input())
ram_quantity = int(input())

gpu_price = 250  # set price for gpu
gpu_total = gpu_quantity * gpu_price

cpu_price = gpu_total * 0.35
cpu_total = cpu_quantity * cpu_price

ram_price = gpu_total * 0.1
ram_total = ram_quantity * ram_price

total_cost = gpu_total + cpu_total + ram_total

if gpu_quantity > cpu_quantity:
    discount = total_cost * 0.15
    total_cost = (gpu_total + cpu_total + ram_total) - discount
else:
    pass

difference = abs(budget - total_cost)

if total_cost <= budget:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
