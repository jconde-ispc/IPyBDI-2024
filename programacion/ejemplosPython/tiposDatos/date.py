import datetime
today = datetime.date.today()
print('Today:', today)
yesterday = today - datetime.timedelta(days=1)
print('Yesterday:', yesterday)
tomorrow = today + datetime.timedelta(days=1)
print('Tomorrow:', tomorrow)
print('Time between tomorrow and yesterday:', tomorrow - yesterday)

"""
Today: 2023-07-26
Yesterday: 2023-07-25
Tomorrow: 2023-07-27
Time between tomorrow and yesterday: 2 days, 0:00:00
"""


x = datetime.datetime.now()

print(x.strftime("%x"))#09/08/23 (septiembre)
print(x.strftime("%m"))

print(x.strftime("%B"))

print(x.strftime("%Y"))#2023
print(x.strftime("%y"))
print(x.strftime("%G"))#2023
print(x.strftime("%X"))#09:30:14
print(x.strftime("%M"))# Minute 00-59	
print(x.strftime("%p"))#AM/PM	


