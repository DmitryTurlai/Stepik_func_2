from datetime import datetime, timedelta
def is_available_date(booked_dates, date_for_booking):
    res = []
    for s in booked_dates:
        #s = '05.11.2021-12.11.2021'

        try:
            start_str, end_str = s.split('-')
            start_date = datetime.strptime(start_str, '%d.%m.%Y').date()
            end_date = datetime.strptime(end_str, '%d.%m.%Y').date()
        except ValueError:
            start_date = end_date = datetime.strptime(s, '%d.%m.%Y').date()

        if start_date == end_date:
            res.append(start_date)
        else:
            dt = start_date
            while dt <= end_date:
                res.append(dt)
                dt += timedelta(days=1)
    date_for_live = []
    try:
        start_str, end_str = date_for_booking.split('-')
        start_date = datetime.strptime(start_str, '%d.%m.%Y').date()
        end_date = datetime.strptime(end_str, '%d.%m.%Y').date()
    except ValueError:
        start_date = end_date = datetime.strptime(date_for_booking, '%d.%m.%Y').date()

    if start_date == end_date:
        date_for_live.append(start_date)
    else:
        dt = start_date
        while dt <= end_date:
            date_for_live.append(dt)
            dt += timedelta(days=1)

    common_values = True
    for value in date_for_live:
        if value in res:
            common_values = False
            break
    return common_values
result = is_available_date(['04.11.2021', '05.11.2021-09.11.2021'], '01.11.2021')
print(result)