exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = (exam_hour * 60) + exam_minute
arrival_time = (arrival_hour * 60) + arrival_minute

time_left = (exam_time - arrival_time) / 60
min_left = (exam_time - arrival_time) % 60

if exam_hour == arrival_hour and exam_minute == arrival_minute:
    print('On time')
elif time_left < 0:


pass