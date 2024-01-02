def time_difference(start_date, end_date):
    s= datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    e = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

    difference = e- s

    minutes = difference.total_seconds() / 60
    hours = minutes / 60
    days = difference.days
    months = days / 30  # Approximate months
    years = days / 365  # Approximate years

    return {
        'minutes': minutes,
        'hours': hours,
        'days': days,
        'months': months,
        'years': years
    }

# Example usage
s_date_time = '2023-01-01 12:00:00'
e_date_time = '2023-12-31 18:30:00'

result = time_difference(s_date_time, e_date_time)
print(result)