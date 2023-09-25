import schedule

import time

from datas import *
from datetime import datetime






def funcs():
    with tbase:
        s = tc.execute('SELECT userid,safety_balance FROM settings').fetchall()
    for i in s:
        if i[1] != 0:




            
            
            
           
            try:
                state_times(useri=int(i[0]))
            except:
                pass

schedule.every().day.at('06:00').do(funcs)
def funcs_5():

    with tbase:
        s = tc.execute('SELECT userid,date FROM settings').fetchall()
    dates = datetime.now()
    try:
        for i in s:
            dates_ = datetime.strptime(i[1], '%Y-%m-%d %H:%M')
            if dates >= dates_:
        
                state_times_safety(useri=int(i[0]))

    except:
        
        pass






schedule.every(5).seconds.do(funcs_5)

while True:
    schedule.run_pending()
    time.sleep(3)
