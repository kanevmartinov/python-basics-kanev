book_pages = int(input())
pages_read_per_hour = int(input())
reading_days = int(input())

reading_hours_total = book_pages / pages_read_per_hour
reading_hours_per_day = reading_hours_total / reading_days

print(round(reading_hours_per_day))