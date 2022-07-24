def add_time(start_time,duration_time,day= None):
    time,time_period = start_time.split()
    start_hour,start_minutes = time.split(':')
    added_hours, added_minutes = duration_time.split(':')

    start_hour = int(start_hour)
    start_minutes = int(start_minutes)
    added_hours = int(added_hours)
    added_minutes = int(added_minutes)

    return_minutes = start_minutes + added_minutes

    if return_minutes >= 60:
        return_minutes -= 60
        added_hours += 1

    if len(str(return_minutes)) == 1:
        return_minutes = '0' + str(return_minutes)

    if time_period == 'PM':
        start_hour_24hr = start_hour + 12
    else:
        start_hour_24hr = start_hour

    count = 0
    return_hours_24hr = start_hour_24hr + added_hours

    while return_hours_24hr >= 24:
        return_hours_24hr -= 24
        count += 1

    if count == 1:
        n = '(next day)'
    elif count > 1:
        n = f"({count} days later)"

    else:
        n = ''

    if start_hour < 12:
        mid_diff = 12 - start_hour
        if added_hours > mid_diff:
            mid = added_hours - mid_diff
            if time_period == 'AM':
                time_period = 'PM'
            else:
                time_period = 'AM'

    if added_hours > 12:
        twelve_hour_count = mid // 12
        if twelve_hour_count % 2 == 1:
            if time_period == 'AM':
                time_period = 'PM'
            else:
                time_period = 'AM'

    return_hours = start_hour + added_hours
    while return_hours >= 24:
        return_hours -= 24

    if return_hours == 0:
        return_hours = 12

    elif return_hours > 12:
        return_hours -= 12

    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    if day != None:
        pos = days.index(day.lower())
        new_position = pos + count
        while new_position >= 7:
            new_position -= 7
        result_day = days[new_position].title()

    if day != None:
        print(f"# Returns: {return_hours}:{return_minutes} {time_period}, {result_day} {n} ")

    else:
        print(f"# Returns: {return_hours}:{return_minutes} {time_period} {n}")

add_time("11:30 AM", "2:32", "Monday")