'''
In this kata, we will make a function to test whether a period is late.

Our function will take three parameters:

last - The Date object with the date of the last period

today - The Date object with the date of the check

cycleLength - Integer representing the length of the cycle in days

If the today is later from last than the cycleLength, the function should return true. We consider it to be late if the number of passed days is larger than the cycleLength. Otherwise return false.
'''

import datetime 

class date():
    def __init__ (self, year, month, day ):
        self.year = year
        self.month = month
        self.day = day
    def show(self):
        print(self.year)
        print(self.month)
        print(self.day) 
def period_is_late(last,today,cycle_length):
        l = datetime.datetime(last.year, last.month, last.day) 
        t = datetime.datetime(today.year, today.month, today.day)
        delta = t-l
        return (delta.days)>cycle_length#your code here
            
