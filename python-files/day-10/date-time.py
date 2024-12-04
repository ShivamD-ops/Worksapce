import datetime as dt 
from datetime import datetime

current_date = dt.date.today()

print(current_date)


now  = datetime.now()
t = now.strftime("%H:%M:%S")

print('Time',t)