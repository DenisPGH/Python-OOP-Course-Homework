"""Create a class called Time. Upon initialization,
it should receive hours, minutes, and seconds (integers).
 The class should also have class attributes max_hours equal to 23, max_minutes equal to 59,
 and max_seconds equal to 59. You should also create 3 additional instance methods:"""
class Time():
    max_hours=23
    max_minutes=59
    max_seconds=59
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self,hours, minutes, seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    def get_time(self) :
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        all_sec=((self.hours)*3600 + self.minutes*60 + self.seconds)
        new_sec=all_sec+1
        a = new_sec // 3600
        if a>23:
            a=0
        b = (new_sec % 3600) // 60
        c = (new_sec % 3600) % 60
        self.hours=a
        self.minutes=b
        self.seconds=c
        return self.get_time()




"""-	set_time(hours, minutes, seconds) - updates the time with the new values
-	get_time() - returns "{hh}:{mm}:{ss}"
-	next_second() - updates the time with one second 
(use the class attributes for validation) and returns the new time (use the get_time() method)
"""



#time = Time(9, 30, 59)
#print(time.next_second())
# print(time.get_time())
#
# time = Time(10, 59, 59)
# print(time.next_second())
# print(time.get_time())
#
# time = Time(23, 59, 59)
# print(time.next_second())
# print(time.get_time())

# time = Time(1, 20, 30)
# #print(time.get_time())
# print(time.next_second())
# #print(time.get_time())

#
#
