exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())
minute_check = abs(exam_minute - arrive_minute)


if exam_hour == arrive_hour and exam_minute == arrive_minute:
    print('On time')
elif arrive_hour < exam_hour:
    if arrive_minute == exam_minute:
        print('On time')
    elif minute_check < 30:
        print('On time')
    elif minute_check > 30:
        print('Early')
elif arrive_hour > exam_hour:
    print('false')


exam_time = (hour_on_examp * 60) + min_on_examp
arrival_time = (hour_on_arrival * 60) + min_on_arrival

time_left = (exam_time - arrival_time) / 60
min_left = (exam_time - arrival_time) % 60