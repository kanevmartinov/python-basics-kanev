cm_lentgh = int(input())
cm_width = int(input())
cm_height = int(input())
filled_percent = float(input())

fish_tank_volume = cm_lentgh * cm_height * cm_width
fish_tank_volume_in_litres = fish_tank_volume / 1000
filled_percent_in_litres = filled_percent / 100

needed_water = fish_tank_volume_in_litres * (1-filled_percent_in_litres)

print(needed_water)