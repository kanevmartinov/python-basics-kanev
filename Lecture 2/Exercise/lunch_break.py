import math
series_name = input()
episode_lentgh = int(input())
brake_lentgh = int(input())

lunch_time = brake_lentgh * 1/8
relaxation_time = brake_lentgh * 1/4
time_left = brake_lentgh - lunch_time - relaxation_time
time_needed = abs(time_left - episode_lentgh)

if time_left >= episode_lentgh:
    print(f'You have enough time to watch {series_name} and left with {math.ceil(time_needed)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(time_needed)} more minutes.")

