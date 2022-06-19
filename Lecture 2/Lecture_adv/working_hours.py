hour = int(input())
weekday = input()

if hour >= 10 and hour <= 18 and weekday == 'Monday':
    print('open')
elif hour >= 10 and hour <= 18 and weekday == 'Tuesday':
    print('open')
elif hour >= 10 and hour <= 18 and weekday == 'Wednesday':
    print('open')
elif hour >= 10 and hour <= 18 and weekday == 'Thursday':
    print('open')
elif hour >= 10 and hour <= 18 and weekday == 'Friday':
    print('open')
elif hour >= 10 and hour <= 18 and weekday == 'Saturday':
    print('open')
else:
    print('closed')