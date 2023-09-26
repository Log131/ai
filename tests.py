from datas import *

import asyncio


async def ffffff():
    async with aiosqlite.connect('vis.db') as tc:
        await tc.execute('UPDATE users SET try_pic_balance = 3')
        await tc.commit()







asyncio.run(ffffff())