# Python course duration > 2 months > 64astr.hours
# 2 months = 8 weeek
# 1 session = 3 astr.hours
# 8w x 2 sessions per week -> 16 sessions
# every week = 6 astr.hours
# 8 weeks x 6 astr.hours = 48 astr. hours

weeks_in_month = 4
times_per_week = 2
course_duration = weeks_in_month * times_per_week
y = course_duration
#print(weeks*times_per_week)
print('Python course duration is:', y , 'weeks')
one_session = 3
every_week = one_session*times_per_week
z = one_session * times_per_week
print('Astronomical hours per week', z)
#print(one_session*every_week)
x= course_duration*every_week
print('Total duration in astronomical hours:',"{:.2f}".format(x))


