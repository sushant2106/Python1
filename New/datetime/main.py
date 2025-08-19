import datetime

d=datetime.datetime(2016,7,24)

print(d.strftime("%y-%m-%d"))

d2=datetime.date.today()
print(d2.strftime("%y-%m-%d"))



print(d2.day)
print("WeekDay:",d2.weekday())
print("isoweekday:",d2.isoweekday())


time_delta=datetime.timedelta(days=7) #7 days before
print(d2 - time_delta)

bday=datetime.date(2016,9,24)

till_bdy=bday-(datetime.date.today())
print(till_bdy)

print(till_bdy.total_seconds())


t=datetime.time(9,30,45,10000)
print(t.hour)

t2=datetime.datetime(2016,7,26,12,30,45,10000)
print(t2)
print(t2.date())
print(t2.year)
print(t2.time)

tdelta=datetime.timedelta(days=7)

# print(dt + tdelta)