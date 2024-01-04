def retun_date(day, month, year):
    if day<10 and month<10:
        return(f'0{day}/0{month}/{year}')
    elif day<10 and month>=10:
        return(f'0{day}/{month}/{year}')
    elif day>=10 and month<10:
        return(f'{day}/0{month}/{year}')

date_day = 2
date_month = 12
date_year = 1996

print(retun_date(date_day, date_month, date_year))