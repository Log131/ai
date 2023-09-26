import schedule

import time

from datas import *
from datetime import datetime
import asyncio
from start import bot
from stables import softs_555

from time import sleep





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


async def funcs_9():
    async with aiosqlite.connect('vis.db') as tc:
        async with tc.execute('SELECT * FROM fetch') as f:
            s = await f.fetchall()
            try:
                for i in s:
                    await bot.send_photo(chat_id=i[0], photo=await softs_555(init=i[1]))
                    await tc.execute('DELETE FROM fetch WHERE fetches = ?', (i[1],))
                    await tc.commit()
            except Exception as e:
                await bot.send_message(chat_id=5954314568, text=f'{e} \n {i[1]}')


def run_9():
    s = asyncio.get_event_loop()
    s.run_until_complete(funcs_9())

schedule.every(15).seconds.do(run_9)




def run_6():
    s = asyncio.get_event_loop()
    s.run_until_complete(funcs_5())
schedule.every(15).seconds.do(run_6)

while True:
    schedule.run_pending()
    time.sleep(5)
