nylon_needed_square_m = int(input())
paint_needed_litres = int(input())
paint_diluent_litres = int(input())
working_hours = int(input())
nylon_price = 1.50
paint_price = 14.50
paint_diluent_price = 5
bags_price = 0.40

total_price_materials = (nylon_needed_square_m + 2) * nylon_price + \
                        paint_needed_litres * 1.1 * paint_price + \
                        paint_diluent_litres * paint_diluent_price + \
                        bags_price
workers_salary = (total_price_materials * 0.3) * working_hours
total_cost = total_price_materials + workers_salary

print(total_cost)
