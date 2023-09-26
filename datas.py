import aiosqlite

from datas import *

import asyncio


async def state_tbase():
    async with aiosqlite.connect('vis.db') as tc:
        await tc.execute('CREATE TABLE IF NOT EXISTS users(userid PRIMARY KEY,balance DEFAULT 0, try_text_balance DEFAULT 3,balance_99 DEFAULT 1, try_pic_balance DEFAULT 3,nudify_content DEFAULT 0, try_balance DEFAULT 0)')
        await tc.execute('CREATE TABLE IF NOT EXISTS targets(msgids,rands)')
        await tc.execute('CREATE TABLE IF NOT EXISTS settings(userid PRIMARY KEY,scale REAL DEFAULT 7.5,safety_balance INTEGER DEFAULT 0,date, safety)')
        await tc.execute('CREATE TABLE IF NOT EXISTS fetch(userid, fetches)')
        await tc.commit()






async def state_0(userid,balance):
    async with aiosqlite.connect('vis.db') as tc:
        await tc.execute('INSERT OR IGNORE INTO users(userid,balance) VALUES(?, ?)', (userid,balance,))
        await tc.commit()






async def state_5(userid, scale, safety, safety_balance, date):
    async with aiosqlite.connect('vis.db') as tc:
        await tc.execute('INSERT OR IGNORE INTO settings(userid, scale, safety, safety_balance, date) VALUES(?, ?, ?, ?, ?)', (userid,scale,safety,safety_balance,date,))
        await tc.commit()









async def state_6(userid):
    async with aiosqlite.connect('vis.db') as tc:
        await tc.execute('UPDATE settings SET scale = scale + 0.5 WHERE userid = ?', (userid,))
        
        await tc.commit()





async def state_666(userid):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('UPDATE settings SET scale = scale - 0.5 WHERE userid = ?', (userid,))
       await tc.commit()

async def state_safety(userid, yes):
    async with aiosqlite.connect('vis.db') as tc:
        
       await tc.execute('UPDATE settings SET safety = ? WHERE userid = ?', (yes,userid,))
        
       await tc.commit()

async def state_safetys(userid, no):
    async with aiosqlite.connect('vis.db') as tc:
        await tc.execute('UPDATE settings SET safety = ? WHERE userid = ?', (no,userid,))
        await tc.commit()






async def state_safets(date,safety_balance, userid):
    async with aiosqlite.connect('vis.db') as tc:
        await tc.execute('UPDATE settings SET date = ?, safety_balance = ? WHERE userid = ?', (date,safety_balance,userid,))
        await tc.commit()


async def state_565(balance,userid):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('UPDATE users SET balance = balance + ? WHERE userid = ?', (balance,userid,))
       await tc.commit()

async def state_55555(msgids,rands):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('INSERT INTO targets(msgids,rands) VALUES(?, ?)', (msgids,rands,))
       await tc.commit()

async def state_deletes(rands):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('DELETE FROM targets WHERE msgids = ?', (rands,))
       await tc.commit()

async def state_tryttttt(userid):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('UPDATE users SET try_text_balance = try_text_balance - 1 WHERE userid = ?', (userid,))
       await tc.commit()

async def state_tryttttt_(userid):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('UPDATE users SET try_balance = try_balance - 1 WHERE userid = ?', (userid,))
       await tc.commit()









async def state_times(useri):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('UPDATE users SET try_balance = 19 WHERE userid = ?', (useri,))
       await tc.commit()
    


async def state_times_safety(useri):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('UPDATE settings SET safety_balance = 0 WHERE userid = ?', (useri,))
       await tc.commit()






async def state_nudify(useri):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('UPDATE users SET nudify_content = 5 WHERE userid = ?', (useri,))
       await tc.commit()

async def state_nudify_(useri):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('UPDATE users SET nudify_content = nudify_content - 1 WHERE userid = ?', (useri,))
       await tc.commit()













async def state_pic_balance(userid):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('UPDATE users SET try_pic_balance = try_pic_balance - 1 WHERE userid = ?', (userid,))
       await tc.commit()





async def state_balance_99(userid):
    async with aiosqlite.connect('vis.db') as tc:
       await tc.execute('UPDATE users SET balance_99 = 0 WHERE userid = ?', (userid,))
       await tc.commit()







async def state_15(userid):
    async with aiosqlite.connect('vis.db') as tc:
        await tc.execute('UPDATE users SET try_balance = try_balance + 15 WHERE userid = ?', (userid,))
        await tc.commit()