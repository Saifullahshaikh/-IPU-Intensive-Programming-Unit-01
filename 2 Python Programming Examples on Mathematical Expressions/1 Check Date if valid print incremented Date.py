def Check(year, month, day):
    if (( year >= 1500 and year <= 2020) and
        (month >= 1 and month <= 12) and
        (day >= 1 and day <= 31)):
        
        print(day+1,month, year,sep='-')


Check(2020,10,22)
Check(22, 12,22)
