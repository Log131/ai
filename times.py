import schedule

import time

from datas import *
from datetime import datetime
import asyncio





async def funcs():
    async with aiosqlite.connect('vis.db') as tc:
        async with tc.execute('SELECT userid,safety_balance FROM settings')as s:
            r = await s.fetchall()
            for i in r:
                if i[1] != 0:
                    
                    
                    
                    
                    
                    
                    try:
                        await state_times(useri=int(i[0]))
                    except Exception as e:
                        print(e)
                        continue





def run_5():
    s = asyncio.get_event_loop()
    s.run_until_complete(funcs())


schedule.every().day.at('06:00').do(run_5)
async def funcs_5():
    async with aiosqlite.connect('vis.db') as tc:
        await tc.commit()
        async with tc.execute('SELECT userid,date FROM settings') as s:
            
            dates = datetime.now()
            r = await s.fetchall()
            for i in r:
                try:
                    dates_ = datetime.strptime(i[1], '%Y-%m-%d %H:%M')
                    if dates >= dates_:
                        
                        await state_times_safety(useri=int(i[0]))
                except:
                    continue





def run_6():
    s = asyncio.get_event_loop()
    s.run_until_complete(funcs_5())
schedule.every(15).seconds.do(run_6)

while True:
    schedule.run_pending()
    asyncio.sleep(3)
