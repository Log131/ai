from aiogram import Dispatcher,Bot,executor,types



from stables import softs_5, softstexts
from datas import *
from keyboards import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


from datetime import datetime, timedelta

import random

with tbase:
    tc.execute('CREATE TABLE IF NOT EXISTS users(userid PRIMARY KEY,balance DEFAULT 0, try_text_balance DEFAULT 3,balance_99 DEFAULT 1, try_pic_balance DEFAULT 1,nudify_content DEFAULT 0, try_balance DEFAULT 0)')
    tc.execute('CREATE TABLE IF NOT EXISTS targets(msgids,rands)')
    
    tc.execute('CREATE TABLE IF NOT EXISTS settings(userid PRIMARY KEY,scale REAL DEFAULT 7.5,safety_balance INTEGER DEFAULT 0,date, safety)')











bot = Bot(token='6573671049:AAEEjlb_kT9prPzOB35cGvl1dXo_JkRO_Vo')
dp = Dispatcher(bot=bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def state_starts(msg: types.Message):
    photos = 'https://imgv3.fotor.com/images/side/create-various-types-of-random-image-using-fotor-random-image-generator.jpg'
    state_0(userid=msg.from_user.id, balance=0)
    state_5(userid=msg.from_user.id,scale=7.5, safety='yes', safety_balance=0, date='0')
    await msg.answer_photo(photo=photos,caption='Наш канал - @kaif_Ai', reply_markup=wel_5())
    


    




@dp.message_handler(text='Раздень подругу ♨️')
async def states_5(msg: types.Message):
    
    await msg.answer('В разработке ожидайте новостей 🙃')


@dp.callback_query_handler(text='settings')
async def stateSettings(css: types.CallbackQuery):

    await css.answer()
    try:
        with tbase:
            nudify = tc.execute('SELECT nudify_content FROM users WHERE userid = ?', (css.from_user.id,)).fetchone()
        await css.message.delete()

        if nudify[0] != 0:
            await css.message.answer('Вам доступен 18+ контент', reply_markup=nudity_())
            await css.message.answer('Ваши настройки', reply_markup=wel())
        else:
            await css.message.answer('Ваши настройки', reply_markup=wel())
    except Exception as e:
        print(e)




class photo_states(StatesGroup):
    promts_ = State()
    photos_ = State()

class picture_states(StatesGroup):
    promts_5 = State()




class nudes_pic_states(StatesGroup):
    promts_555 = State()
    promts = State()

class nudes_img_states(StatesGroup):
    promts_0 = State()






class spams_states(StatesGroup):
    spams_ = State()



@dp.callback_query_handler(text='nudity')
async def nudes_(css: types.CallbackQuery):
    await css.answer()
    await css.message.delete()
    
    await css.message.answer('18+ контент', reply_markup=nudity_5())



@dp.callback_query_handler(text='img', state=None)
async def tudity_(css: types.CallbackQuery, state: FSMContext):
    await css.answer()
    await css.message.delete()
    
    
    with tbase:
        s = tc.execute('SELECT nudify_content FROM users WHERE userid = ?',(css.from_user.id,)).fetchone()
    
    
    
    
    
    
    if s[0] != 0:
        
        await css.message.answer('Напишите PROMT пример(girl,naked,pussy)',reply_markup=otmena_5())

        await nudes_img_states.promts_0.set()



@dp.message_handler(state=nudes_img_states.promts_0)
async def tudity_5(msg: types.Message, state: FSMContext):
    with tbase:
        scales = tc.execute('SELECT scale FROM settings WHERE userid = ?', (msg.from_user.id,)).fetchone()


    try:
        await msg.answer('Генерируется подождите')
        await state.finish()
        await msg.answer_photo(photo=await softstexts(promts=msg.text,safety='no',scale=scales))
        state_nudify_(useri=msg.from_user.id)
    except Exception as e:
        print(e)
        await state.finish()
        await msg.answer('Чтото пошло не так')

@dp.callback_query_handler(text='cansels', state=nudes_img_states.promts_0)
async def tudity_cansel(css: types.CallbackQuery, state: FSMContext):
    await css.answer()
    await state.finish()
    await css.message.delete()



@dp.callback_query_handler(text='pic', state=None)
async def rands(css: types.CallbackQuery, state: FSMContext):
    await css.answer()
    await css.message.delete()
    
    with tbase:
        s = tc.execute('SELECT nudify_content FROM users WHERE userid = ?', (css.from_user.id,)).fetchone()
    
    if s[0] != 0:
        await css.message.answer('Введите PROMT пример(girl,naked,pussy)',reply_markup=otmena_____())
        await nudes_pic_states.promts_555.set()


@dp.message_handler(state=nudes_pic_states.promts_555)
async def rands_(msg: types.Message, state: FSMContext):
    if msg.text == '/start':
        await state.finish()
        await msg.delete()
    else:
        
        
        
        
        async with state.proxy() as data:
            data['promts_555'] = msg.text

        await msg.answer('Отправьте ФОТО', reply_markup=otmena_____())

        await nudes_pic_states.next()


@dp.message_handler(state=nudes_pic_states.promts, content_types=types.ContentType.PHOTO)
async def rands_states(msg: types.Message, state: FSMContext):
    await msg.delete()
    with tbase:
        scales = tc.execute('SELECT scale FROM settings WHERE userid = ?', (msg.from_user.id,)).fetchone()
    async with state.proxy() as data:
        try:
            t = '6573671049:AAEEjlb_kT9prPzOB35cGvl1dXo_JkRO_Vo'
            s = await bot.get_file(msg.photo[-1].file_id)
            inits = f'https://api.telegram.org/file/bot{t}/{s.file_path}'
            await msg.answer('Генерируется подождите')
            await state.finish()
            await msg.answer_photo(photo=await softs_5(init=inits, promts=data['promts_555'], scale=scales,safety='no'))
            state_nudify_(useri=msg.from_user.id)
        except Exception as e:
            print(e)

            await state.finish()

            await msg.answer('Чтото пошло не так')


@dp.callback_query_handler(text='canselthis', state=[nudes_pic_states.promts_555,nudes_pic_states.promts])
async def state0(css: types.CallbackQuery, state: FSMContext):
    await css.answer()
    await state.finish()
    await css.message.delete()

@dp.callback_query_handler(text='picture', state=None)
async def state_picture(css: types.CallbackQuery, state: FSMContext):
    await css.answer()
    
    await css.message.delete()
    with tbase:
        s_texts = tc.execute('SELECT try_text_balance FROM users WHERE userid = ?', (css.from_user.id,)).fetchone()
        s = tc.execute('SELECT try_balance FROM users WHERE userid = ?', (css.from_user.id,)).fetchone()
        s_ = tc.execute('SELECT safety_balance FROM settings WHERE userid = ?', (css.from_user.id,)).fetchone()
    if s[0] > 0:
        await css.message.answer_photo(photo='https://imgv3.fotor.com/images/side/AI-generate-different-characters-in-Fotor-text-to-image-AI.png', caption='ВВЕДИТЕ PROMT пример(woman,smile,happy)',reply_markup=otmena_())
        await picture_states.promts_5.set()
    elif s[0] > 0 and s_[0] != 0:
        await css.message.answer_photo(photo='https://imgv3.fotor.com/images/side/AI-generate-different-characters-in-Fotor-text-to-image-AI.png', caption='ВВЕДИТЕ PROMT пример(woman,smile,happy)',reply_markup=otmena_())
        await picture_states.promts_5.set()
    else:
        if s_texts[0] != 0:
            await css.message.answer_photo(photo='https://imgv3.fotor.com/images/side/AI-generate-different-characters-in-Fotor-text-to-image-AI.png', caption='ВВЕДИТЕ PROMT пример(woman,smile,happy)',reply_markup=otmena_())
            await picture_states.promts_5.set()
        else:
            await css.message.answer('Слишком много запросов попробуйте чуть позже 🙃')
    
    

@dp.message_handler(state=picture_states.promts_5)
async def state_picture_5(msg: types.Message, state: FSMContext):
    
    if msg.text == '/start':
        await state.finish()
        await msg.answer('Отмена', reply_markup=wel_5())

    
    else:
        with tbase:
            s_ = tc.execute('SELECT try_text_balance FROM users WHERE userid = ?', (msg.from_user.id,)).fetchone()
            s = tc.execute('SELECT try_balance FROM users WHERE userid = ?', (msg.from_user.id,)).fetchone()
        
            
        
        
        try:
            await msg.answer('`Генерируется` подождите  \n \n \n (при некоторых случаях `ИИ` может сгенерировать `18+` контент если видите темное фото это значит что это `18+` контент вы можете включить функцию `18+` в настройках', parse_mode='Markdown')
            with tbase:
                scales = tc.execute('SELECT scale FROM settings WHERE userid = ?', (msg.from_user.id,)).fetchone()
            
                safetys = tc.execute('SELECT safety FROM settings WHERE userid = ?', (msg.from_user.id,)).fetchone()
            
            
            await state.finish()
            await msg.answer_photo(photo=await softstexts(promts=msg.text,safety=safetys[0], scale=scales[0]))
            if s_[0] != 0:
                state_tryttttt(userid=msg.from_user.id)
            elif s[0] != 0 and s_[0] == 0:
                state_tryttttt_(userid=msg.from_user.id)
            if safetys[0] == 'no':
                state_nudify_(useri=msg.from_user.id)
        except Exception as e:
            print(e)
            await state.finish()
            
            
            
            await msg.answer('Что то пошло не так')



@dp.callback_query_handler(text='image',state=None)
async def state_content(css: types.CallbackQuery, state: FSMContext):
    
    
    try:
        await css.answer()
        await css.message.delete()
        with tbase:
            s_555 = tc.execute('SELECT try_balance FROM users WHERE userid = ?', (css.from_user.id,)).fetchone()
            s = tc.execute('SELECT try_pic_balance FROM users WHERE userid = ?', (css.from_user.id,)).fetchone()
            s_ = tc.execute('SELECT safety_balance FROM settings WHERE userid = ?', (css.from_user.id,)).fetchone()
        if s[0] > 0:
            await css.message.answer_photo(photo='https://imgv3.fotor.com/images/videoImage/apply-the-two-cartoon-art-effects-to-the-female-portarit-to-turn-photo-to-art-in-fotor.jpg', caption='Меняйте ваши фото как вам угодно ! \n \n \n ВВЕДИТЕ PROMT пример(woman,smile,happy)', reply_markup=otmena())
            
            await photo_states.promts_.set()
        elif s[0] > 0 and s_[0] != 0:
            await css.message.answer_photo(photo='https://imgv3.fotor.com/images/videoImage/apply-the-two-cartoon-art-effects-to-the-female-portarit-to-turn-photo-to-art-in-fotor.jpg', caption='Меняйте ваши фото как вам угодно ! \n \n \n ВВЕДИТЕ PROMT пример(woman,smile,happy)', reply_markup=otmena())
            
            await photo_states.promts_.set()
        else:
            if s_555[0] != 0:
                await css.message.answer_photo(photo='https://imgv3.fotor.com/images/videoImage/apply-the-two-cartoon-art-effects-to-the-female-portarit-to-turn-photo-to-art-in-fotor.jpg', caption='Меняйте ваши фото как вам угодно ! \n \n \n ВВЕДИТЕ PROMT пример(woman,smile,happy)', reply_markup=otmena())
            
                await photo_states.promts_.set()
            else:
                await css.message.answer('Слишком много запросов попробуйте позже 🙃')
        
    except Exception as e:
        print(e)


@dp.callback_query_handler(text='rattt', state=picture_states.promts_5,)
async def stateCancel_(css: types.CallbackQuery, state: FSMContext):

    await css.answer()
    await state.finish()

    await css.message.delete()






@dp.callback_query_handler(text='tat', state=[photo_states.promts_, photo_states.photos_])
async def stateCancel(css: types.CallbackQuery, state: FSMContext):
    await css.answer()
    await state.finish()
    
    await css.message.delete()

@dp.message_handler(state=photo_states.promts_)
async def state_get_photo(msg: types.Message, state: FSMContext):
    if msg.text == '/start':
        await msg.delete()
        await state.finish()
        await msg.answer('Попробуйте заного', reply_markup=wel_5())
    else:
        try:
            async with state.proxy() as data:
                data['promts_'] = msg.text
            await msg.answer('Отправьте ФОТО',reply_markup=otmena())
            await photo_states.next()
        except Exception as e:
            print(e)
            await state.finish()






@dp.message_handler(state=photo_states.photos_, content_types=[types.ContentType.TEXT, types.ContentType.PHOTO])
async def state_get_promts(msg: types.Message, state: FSMContext):
    if msg.content_type == types.ContentType.TEXT:
        await state.finish()
        await msg.answer('Вы не отправили фото попробуйте заного', reply_markup=wel_5())
    else:
        try:
            with tbase:
                s_555 = tc.execute('SELECT try_balance FROM users WHERE userid = ?', (msg.from_user.id,)).fetchone()
                s_pic = tc.execute('SELECT try_pic_balance FROM users WHERE userid = ?', (msg.from_user.id,)).fetchone()
                s_5 = tc.execute('SELECT safety FROM settings WHERE userid = ?', (msg.from_user.id,)).fetchone()
                scales = tc.execute('SELECT scale FROM settings WHERE userid = ?', (msg.from_user.id,)).fetchone()
            t = '6573671049:AAEEjlb_kT9prPzOB35cGvl1dXo_JkRO_Vo'
            s = await bot.get_file(msg.photo[-1].file_id)
            inits = f'https://api.telegram.org/file/bot{t}/{s.file_path}'
            
            
            
            
            async with state.proxy() as data:
                await msg.answer('`Генерируется` подождите  \n \n \n (при некоторых случаях `ИИ` может сгенерировать `18+` контент если видите темное фото это значит что это `18+` контент вы можете включить функцию `18+` в настройках', parse_mode='Markdown')
        
        
                await state.finish()
                
                await msg.answer_photo(await softs_5(init=inits, promts=data['promts_'], scale=scales[0], safety=s_5[0]))
                
                
                
                
                
                
                
                
                
                if s_pic[0] != 0:
                    state_pic_balance(userid=msg.from_user.id)
                elif s_pic[0] == 0 and s_555[0] != 0:
                    state_tryttttt_(userid=msg.from_user.id)
                if s_5[0] == 'no':
                    state_nudify_(useri=msg.from_user.id)
                
        except Exception as e:
        
            print(e)
        
            await state.finish()
        
            await msg.answer('чтото пошло не так')


@dp.message_handler(text='Профиль 🆔')
async def state_profile(msg: types.Message):
    with tbase:
        nudify = tc.execute('SELECT nudify_content FROM users WHERE userid = ?', (msg.from_user.id,)).fetchone()
        s = tc.execute('SELECT safety_balance FROM settings WHERE userid = ?', (msg.from_user.id,)).fetchone()
        
        s_pic = tc.execute('SELECT try_pic_balance FROM users WHERE userid = ?', (msg.from_user.id,)).fetchone()

        s_____ = tc.execute('SELECT try_text_balance FROM users WHERE userid = ?', (msg.from_user.id,)).fetchone()
        s______ = tc.execute('SELECT try_balance FROM users WHERE userid = ?', (msg.from_user.id,)).fetchone()

        
    
    if s[0] == 0:
        await msg.answer(f'Ваш 🆔 : {msg.from_user.id} \n \n Генераций(TextToImage) - `{s_____[0]}` \n Генераций(imgToimg) - `{s_pic[0]}` \n Генераций 18+ контента - `{nudify[0]}` \n Подписка : Недоступна \n ', parse_mode='Markdown')
    elif s[0] == 1:
        with tbase:
            nudify = tc.execute('SELECT nudify_content FROM users WHERE userid = ?', (msg.from_user.id,)).fetchone()
            s_ = tc.execute('SELECT date FROM settings WHERE userid = ?', (msg.from_user.id,)).fetchone()
        
        tir = datetime.strptime(s_[0], '%Y-%m-%d %H:%M')
        dates = datetime.now()
        f = tir - dates
        await msg.answer(f'Ваш 🆔 : {msg.from_user.id} \n \n Генераций по подписке (обновляется каждый день) - `{s______[0]}` \n Генераций(TextToImage) - `{s_____[0]}` \n Генераций(imgToimg) - `{s_pic[0]}` \nГенераций 18+ контента - `{nudify[0]}` \n Подписка : `{f}` ', parse_mode='Markdown')
    else:
        pass




@dp.message_handler(text='Настройки ☣️')
async def states_555(msg: types.Message):





    with tbase:
        s_ = tc.execute('SELECT scale FROM settings WHERE userid = ?', (msg.from_user.id,)).fetchone()
    row = InlineKeyboardMarkup()
    rows = InlineKeyboardButton(text=f'Увеличить scale + 0.5', callback_data=f'scaleupt_{msg.from_user.id}')
    rows_ = InlineKeyboardButton(text=f'Уменьшить scale - 0.5', callback_data=f'scaledow_{msg.from_user.id}')
    
    row.add(rows,rows_)
    await msg.answer(f'Ваши настройки : \n \n \n `guidance_scale` : {s_[0]} \n (Влияет на ваши запросы Рекомендуется 7.5)', reply_markup=row, parse_mode='Markdown')



@dp.callback_query_handler(text_contains='scale')
async def state_665(css: types.CallbackQuery):
    await css.answer()

    await css.message.delete()
    ans = css.data.split('_')
    if ans[0] == 'scaleupt':
        state_6(userid=css.from_user.id)
        with tbase:
            s_ = tc.execute('SELECT scale FROM settings WHERE userid = ?', (css.from_user.id,)).fetchone()
        row = InlineKeyboardMarkup()
        rows = InlineKeyboardButton(text=f'Увеличить scale + 0.5', callback_data=f'scaleupt_{css.from_user.id}')
        rows_ = InlineKeyboardButton(text=f'Уменьшить scale - 0.5', callback_data=f'scaledow_{css.from_user.id}')
        row.add(rows,rows_)
        await css.message.answer(f'Ваши настройки : \n \n \n `guidance_scale` : {s_[0]} \n (Влияет на ваши запросы Рекомендуется 7.5)', reply_markup=row, parse_mode='Markdown')
    
    elif ans[0] == 'scaledow':
        state_666(userid=css.from_user.id)
        with tbase:
            s_ = tc.execute('SELECT scale,safety FROM settings WHERE userid = ?', (css.from_user.id,)).fetchone()
        
        row = InlineKeyboardMarkup()
        rows = InlineKeyboardButton(text=f'Увеличить scale + 0.5', callback_data=f'scaleupt_{css.from_user.id}')
        rows_ = InlineKeyboardButton(text=f'Уменьшить scale - 0.5', callback_data=f'scaledow_{css.from_user.id}')
        row.add(rows,rows_)
            
        await css.message.answer(f'Ваши настройки : \n \n \n `guidance_scale` : {s_[0]} \n (Влияет на ваши запросы Рекомендуется 7.5)', reply_markup=row, parse_mode='Markdown')
    
    
    else:
        pass







@dp.message_handler(text='Купить подписку')
async def state_555(msg: types.Message):
    with tbase:
        s = tc.execute('SELECT balance_99 FROM users WHERE userid = ?', (msg.from_user.id,)).fetchone()
    
    if s[0] != 0:

        await msg.answer('Подписки', reply_markup=fffff_key(rands=random.randint(11111,99999),userid=f'{msg.from_user.id}'))
    else:
        await msg.answer('Подписки', reply_markup=fffff(rands=random.randint(11111,99999),userid=f'{msg.from_user.id}'))





@dp.callback_query_handler(text_contains='getit')
async def state_fffff(css: types.CallbackQuery):
    with tbase:
        
        s_ = tc.execute('SELECT safety_balance FROM settings WHERE userid = ?', (css.from_user.id,)).fetchone()
    
    s = css.data.split('_')
    await css.answer()
    if s[3] == '15zaprosov' and s_[0] != 0:
        try:
            await css.message.delete()
            await css.message.answer(f'Реквизиты для отправки денег за подписку: \n Тинькофф Банк `5536914054972405` - Приоритетный Банк {s[1]}р \n СберБанк - `2202203293150142` {s[1]}р \n \n С комментарием - `{s[2]}` \n В случае ошибки и отправки денег в другие банки (Qiwi и тд) Возврата нет. Будьте внимательнее при переводах \n \n \n После чего нажмите я оплатил', parse_mode='Markdown', reply_markup=sends(userid=f'{s[1]}_{s[2]}_{s[3]}_{s[4]}'))
        except:
            pass

    elif s[3] != '15zaprosov':
        try:
            await css.message.delete()
            await css.message.answer(f'Реквизиты для отправки денег за подписку: \n Тинькофф Банк `5536914054972405` - Приоритетный Банк {s[1]}р \n СберБанк - `2202203293150142` {s[1]}р \n \n С комментарием - `{s[2]}` \n В случае ошибки и отправки денег в другие банки (Qiwi и тд) Возврата нет. Будьте внимательнее при переводах \n \n \n После чего нажмите я оплатил', parse_mode='Markdown', reply_markup=sends(userid=f'{s[1]}_{s[2]}_{s[3]}_{s[4]}'))

        except:
            pass

    else:
        
        try:
            await css.message.delete()
            await css.message.answer('У вас нет подписки')
        except Exception as e:
            print(e)


@dp.callback_query_handler(text_contains='check')
async def state_srs(css: types.CallbackQuery):
    await css.answer()
    
    s = css.data.split('_')
    s_ = await bot.send_message(chat_id=-1001980460031, text=f'Покупатель - @{css.from_user.username} \n Оплатил - {s[1]}р \n Комментарий - {s[2]} \n Подписка : {s[3]}',reply_markup=accept_(userid=f'{s[1]}_{s[2]}_{s[3]}_{s[4]}'))

    state_55555(msgids=s_.message_id,rands=s[2])   


@dp.callback_query_handler(text_contains='accepts')
async def state_____(css: types.CallbackQuery):
    await css.answer()
    s = css.data.split('_')
    
    
    
    
    
    
    with tbase:
        f = tc.execute('SELECT msgids FROM targets WHERE rands = ?', (s[2],)).fetchone()
    if s[3] == '1day':

        try:
            state_times(useri=int(s[4]))
            state_565(balance=int(s[1]), userid=int(s[4]))
            dates = (datetime.now() + timedelta(hours=23)).strftime('%Y-%m-%d %H:%M')
            state_safets(date=dates,safety_balance=1, userid=int(s[4]))
            await bot.edit_message_text(text='Пользователю выдана подписка ☑️', chat_id=-1001980460031,message_id=f[0])
            try:
                await bot.send_message(chat_id=s[4], text='Вам выдана подписка')
                state_deletes(rands=f[0])
            except Exception as e:
                print(e)
        except Exception as e:
            try:
                await bot.send_message(chat_id=5954314568, text=e)
            except:
                pass

    elif s[3] == '3day':

        try:
            state_times(useri=int(s[4]))
            state_565(balance=int(s[1]), userid=int(s[4]))
            dates = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d %H:%M')
            state_safets(date=dates,safety_balance=1, userid=int(s[4]))
            await bot.edit_message_text(text='Пользователю выдана подписка ☑️', chat_id=-1001980460031,message_id=f[0])
            try:
                await bot.send_message(chat_id=s[4], text='Вам выдана подписка')
                state_deletes(rands=f[0])
            except Exception as e:
                print(e)
        except Exception as e:
            try:
                await bot.send_message(chat_id=5954314568, text=e)
            except:
                pass
    elif s[3] == '7day':

        try:
            state_times(useri=int(s[4]))
            state_565(balance=int(s[1]), userid=int(s[4]))
            dates = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d %H:%M')
            state_safets(date=dates,safety_balance=1, userid=int(s[4]))
            await bot.edit_message_text(text='Пользователю выдана подписка ☑️', chat_id=-1001980460031,message_id=f[0])
            try:
                await bot.send_message(chat_id=s[4], text='Вам выдана подписка')
                state_deletes(rands=f[0])
            except Exception as e:
                print(e)
        except Exception as e:
            try:
                await bot.send_message(chat_id=5954314568, text=e)
            except:
                pass
    
    elif s[3] == '1month':

        try:
            state_times(useri=int(s[4]))
            state_565(balance=int(s[1]), userid=int(s[4]))
            dates = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M')
            state_safets(date=dates,safety_balance=1, userid=int(s[4]))
            await bot.edit_message_text(text='Пользователю выдана подписка ☑️', chat_id=-1001980460031,message_id=f[0])
            try:
                await bot.send_message(chat_id=s[4], text='Вам выдана подписка')
                state_deletes(rands=f[0])
            except Exception as e:
                print(e)
        except Exception as e:
            try:
                await bot.send_message(chat_id=5954314568, text=e)
            except:
                pass
    
    elif s[3] == '18content':
        try:
            state_nudify(useri=int(s[4]))
            state_565(balance=int(s[1]), userid=int(s[4]))

            await bot.edit_message_text(text='Пользователю выдан 18+ режим ☑️', chat_id=-1001980460031,message_id=f[0])
            try:
                await bot.send_message(chat_id=int(s[4]), text='18+ режим активирован Перейдите в настройки там сможете генерировать 18+ контент ❗️')
                state_deletes(rands=f[0])
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
    elif s[3] == '1day99':
        try:
            state_times(useri=int(s[4]))
            state_565(balance=int(s[1]), userid=int(s[4]))
            state_balance_99(userid=int(s[4]))
            dates = (datetime.now() + timedelta(hours=23)).strftime('%Y-%m-%d %H:%M')
            state_safets(date=dates,safety_balance=1, userid=int(s[4]))
            await bot.edit_message_text(text='Пользователю выдана подписка ☑️', chat_id=-1001980460031,message_id=f[0])
            try:
                await bot.send_message(chat_id=s[4], text='Вам выдана подписка')
                state_deletes(rands=f[0])
            except Exception as e:
                print(e)
        except Exception as e:
            try:
                await bot.send_message(chat_id=5954314568, text=e)
            except:
                pass
    elif s[3] == '15zaprosov':
        try:
            state_15(userid=int(s[4]))
            await bot.edit_message_text(text='Пользователю выданы запросы ☑️', chat_id=-1001980460031,message_id=f[0])
            try:
                await bot.send_message(chat_id=s[4], text='Вам выданы запросы')
                state_deletes(rands=f[0])
            except Exception as e:
                print(e)
        except Exception as e:
            try:
                await bot.send_message(chat_id=5954314568, text=e)
            except:
                pass


@dp.callback_query_handler(text_contains='otmena_')
async def fffff_(css: types.CallbackQuery):
    s = css.data.split('_')
    with tbase:
        r = tc.execute('SELECT msgids FROM targets WHERE rands = ?', (s[2],)).fetchone()
    
    




    try:
        await bot.edit_message_text(text='Отменено', chat_id=-1001980460031, message_id=r[0])
        await bot.send_message(chat_id=s[4], text='Вашу оплату отклонили')
        state_deletes(rands=r[0])
    except Exception as e:
        print(e)







@dp.message_handler(text='Поддержка 👩‍🔧')
async def state_supports(msg: types.Message):
    await msg.answer('Наш канал - @kaif_Ai \n \n \n Возникли проблемы? мы рады вам помочь - @kaif_work')



@dp.message_handler(commands=['admin'])
async def state_ads(msg: types.Message):
    chat_admins = await bot.get_chat_member(chat_id=-1001980460031, user_id=msg.from_user.id)
    if chat_admins.status == 'creator' or chat_admins.status == 'administrator':
        await msg.answer('Админка', reply_markup=strts())
    else:
        pass



@dp.callback_query_handler(text='spams', state=None)
async def state_spams(css: types.CallbackQuery, state: FSMContext):
    chat_admins = await bot.get_chat_member(chat_id=-1001980460031, user_id=css.from_user.id)
    if chat_admins.status == 'creator' or chat_admins.status == 'administrator':
        await spams_states.spams_.set()

@dp.message_handler(state=spams_states.spams_)
async def state_spams_(msg: types.Message, state: FSMContext):
    with tbase:
        s = tc.execute('SELECT userid FROM users').fetchall()
    await msg.delete()
    await msg.answer('Введите текст',reply_markup=otmena_555())
    for i in s:
        try:
            await bot.send_message(chat_id=i[0], text=msg.text)
        except:
            pass
    await msg.answer('Рассылено')
    await state.finish()



@dp.callback_query_handler(text='canselt', state=spams_states.spams_)
async def state_spams_5(css: types.CallbackQuery, state: FSMContext):
    await css.answer()
    await css.message.delete()
    await state.finish()


@dp.callback_query_handler(text='balances')
async def state_balances(css: types.CallbackQuery):
    
    await css.answer()
    with tbase:
        r = tc.execute('SELECT COUNT(userid) FROM users').fetchone()
        s = tc.execute('SELECT SUM(balance) FROM users').fetchone()

    await css.message.answer(f'Профит - {s[0]}, \n Пользователей - {r[0]}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)