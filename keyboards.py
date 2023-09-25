from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton

from aiogram.types import InlineKeyboardMarkup


def wel():
    s = ReplyKeyboardMarkup(resize_keyboard=True)
    s_0 = KeyboardButton(text='Раздень подругу ♨️')
    s_5 = KeyboardButton(text='Профиль 🆔')
    s_6 = KeyboardButton(text='Купить подписку')
    s_ = KeyboardButton(text='Поддержка 👩‍🔧')

    
    s_555 = KeyboardButton(text='Настройки ☣️')
    
    s.add(s_6,s_5,s_555).add(s_0).add(s_)

    return s






def wel_5():
    s = InlineKeyboardMarkup()
    s_555 =InlineKeyboardButton(text='Настройки ☣️', callback_data='settings')
    s_5 = InlineKeyboardButton(text='Отправить Картинку(Img to Img) 💢', callback_data=f'image')
    s_6 = InlineKeyboardButton(text='Генерация из Текста(Text to Image) 💢', callback_data=f'picture')


    return s.add(s_5,s_6).add(s_555)


def otmena():
    s = InlineKeyboardMarkup()
    s_6 = InlineKeyboardButton(text='Отменить', callback_data='tat')

    return s.add(s_6)






def otmena_():
    s = InlineKeyboardMarkup()
    s_6 = InlineKeyboardButton(text='Отменить', callback_data='rattt')

    return s.add(s_6)



def otmena_5():
    s = InlineKeyboardMarkup()
    s_5 = InlineKeyboardButton(text='Отменить', callback_data='cansels')

    return s.add(s_5)

def otmena_____():
    s = InlineKeyboardMarkup()
    s_5 = InlineKeyboardButton(text='Отмена', callback_data='canselthis')

    return s.add(s_5)




def fffff(rands, userid):
    s = InlineKeyboardMarkup()
    s_5 = InlineKeyboardButton(text='1 День = 199р', callback_data=f'getit_199_{rands}_1day_{userid}')
    s_6 = InlineKeyboardButton(text='3 Дня = 499р', callback_data=f'getit_499_{rands}_3day_{userid}')
    s_566 = InlineKeyboardButton(text='7 Дней = 1099р', callback_data=f'getit_1099_{rands}_7day_{userid}')
    s_565 = InlineKeyboardButton(text='1 Месяц = 4300р', callback_data=f'getit_4300_{rands}_1month_{userid}')
    s_555 = InlineKeyboardButton(text='18+ контент (5 запросов) = 149р', callback_data=f'getit_149_{rands}_18content_{userid}')
    s_0 = InlineKeyboardButton(text='Запросы 15 шт(если у вас подписка) = 119р', callback_data=f'getit_119_{rands}_15zaprosov_{userid}')
    return s.add(s_5,s_6,s_566).add(s_565).add(s_555).add(s_0)


def fffff_key(rands, userid):
    s = InlineKeyboardMarkup()
    s_5 = InlineKeyboardButton(text='1 День = 99р', callback_data=f'getit_99_{rands}_1day99_{userid}')
    s_6 = InlineKeyboardButton(text='3 Дня = 499р', callback_data=f'getit_499_{rands}_3day_{userid}')
    s_566 = InlineKeyboardButton(text='7 Дней = 1099р', callback_data=f'getit_1099_{rands}_7day_{userid}')
    s_565 = InlineKeyboardButton(text='1 Месяц = 4299р', callback_data=f'getit_4299_{rands}_1month_{userid}')
    s_555 = InlineKeyboardButton(text='18+ контент (5 запросов) = 149р', callback_data=f'getit_149_{rands}_18content_{userid}')
    s_0 = InlineKeyboardButton(text='Запросы 15 шт(если у вас подписка) = 119р', callback_data=f'getit_119_{rands}_15zaprosov_{userid}')
    return s.add(s_5,s_6,s_566).add(s_565).add(s_555).add(s_0)

def sends(userid):
    s = InlineKeyboardMarkup()
    s_5 = InlineKeyboardButton(text='Я оплатил ☑️', callback_data=f'check_{userid}')

    return s.add(s_5)





def accept_(userid):
    s = InlineKeyboardMarkup()
    s_5 = InlineKeyboardButton(text='Принять ☑️', callback_data=f'accepts_{userid}')
    s_6 = InlineKeyboardButton(text='Отклонить', callback_data=f'otmena_{userid}')

    return s.add(s_5,s_6)



def nudity_():
    s = InlineKeyboardMarkup()
    s_5 = InlineKeyboardButton(text='Сгенерировать 18+ контент', callback_data=f'nudity')

    return s.add(s_5)











def nudity_5():
    s = InlineKeyboardMarkup()
    s_5 = InlineKeyboardButton(text='ImageToImage 18+ контент', callback_data=f'pic')
    
    s_6 = InlineKeyboardButton(text='TextToImage 18+ контент', callback_data=f'img')
    return s.add(s_5,s_6)


def otmena_555():
    s = InlineKeyboardMarkup()
    s_5 = InlineKeyboardButton(text='Отмена', callback_data='canselt')

    return s.add(s_5)

def strts():
    s = InlineKeyboardMarkup()
    s_5 = InlineKeyboardButton(text='Рассылка', callback_data='spams')
    s_555 = InlineKeyboardButton(text='Информация', callback_data='balances')

    return s.add(s_555,s_5)