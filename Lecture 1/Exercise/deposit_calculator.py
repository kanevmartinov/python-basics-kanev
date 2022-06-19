deposited_sum = float(input())
deposit_period = int(input())
annual_interest_percent = float(input())

annual_interest = deposited_sum * annual_interest_percent / 100
monthly_interest = annual_interest / 12
total_sum = deposited_sum + deposit_period * monthly_interest
print(total_sum)

