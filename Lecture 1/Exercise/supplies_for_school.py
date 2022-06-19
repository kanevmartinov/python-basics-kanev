pen_packages = int(input())
highlighter_packages = int(input())
mr_propper_litres= int(input())
discount_percent = int(input())

pen_packages_price = pen_packages * 5.80
highlighter_packages_price = highlighter_packages * 7.20
mr_propper_price = mr_propper_litres * 1.20
total_price = pen_packages_price + highlighter_packages_price + mr_propper_price
discounted_percent_conversion = discount_percent / 100
final_price = total_price - total_price * discounted_percent_conversion
print(final_price)