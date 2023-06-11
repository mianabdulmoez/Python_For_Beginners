# Unpacking a Tuple

weak_days = ('Monday','Teusday','Wednesday','Thrusday','Friday',)
# we have 5 days but we try to unpack 4 that's why it show an error
# (day1, day2, day3, day4) = weak_days
(day1, day2, day3, day4,day5) = weak_days
# We add more than in tuple
# (day1, day2, day3, day4, day5, day6) = weak_days
print(day1)
print(day2)
print(day3)
print(day4)
print(day5)