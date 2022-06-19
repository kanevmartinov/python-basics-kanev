chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

chicken_menus_price = 10.35
fish_menus_price = 12.40
vegetarian_menus_price = 8.15
delivery_price = 2.50

menus_cost = chicken_menus * chicken_menus_price + \
             fish_menus * fish_menus_price + \
             vegetarian_menus * vegetarian_menus_price

dessert_price = menus_cost * 20 / 100

total_cost = menus_cost + dessert_price + delivery_price

print(total_cost)