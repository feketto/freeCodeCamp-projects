def add_time(start, duration, day_start = 'empty'):
    dow = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    dow_final = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if not day_start == 'empty':
        dow_index = dow.index(day_start.lower())
    else:
        dow_index = None
    
    times, pora = start.split(' ')
    hours, minutes = map(int, times.split(':'))
    time_current = 0
    if pora == "PM":
        hours += 12

    time_start = hours * 60 + minutes #w jakiej minucie dnia 1 jestesmy
    ttnd = 1440 - time_start #ile minut do kolejnego dnia
    hoursta, minutesta = map(int, duration.split(':')) #ile godzin i minut do dodania
    tta = hoursta * 60 + minutesta #ile czasu  w minutach do dodania

    total_minutes = time_start + tta
    days_later = total_minutes // 1440

    if days_later == 1:
        ndays = '(next day)'
    elif days_later > 1:
        ndays = f'({days_later} days later)'
    else:
        ndays = ''

    if dow_index is not None:
        current_day = dow_final[(dow_index + days_later) % 7]
    else:
        current_day = ''



    time_current = total_minutes % 1440
    hoursf = time_current // 60 % 12
    if hoursf == 0:
        hoursf= 12
    minutesf = time_current % 60
    pora_final = 'AM' if 0<=time_current<=719 else 'PM'


    if current_day and ndays:
        new_time = f"{hoursf}:{minutesf:02d} {pora_final}, {current_day} {ndays}"
    elif current_day and not ndays:
        new_time = f"{hoursf}:{minutesf:02d} {pora_final}, {current_day}"
    elif ndays:
        new_time = f"{hoursf}:{minutesf:02d} {pora_final} {ndays}"
    else:
        new_time = f"{hoursf}:{minutesf:02d} {pora_final}"
    return new_time

print(add_time('3:30 PM', '2:12', 'Monday'))
