#import date time library and print date time using string substitution
from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d %02d:%02d:%04d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

