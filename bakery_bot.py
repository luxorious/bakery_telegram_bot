'''Есть маленькая пекарня: пирожные, пирожки, салаты, котлеты, вареники и тд , кофе.
находиться в новом ЖК из уже заселенных 16 домов и строящихся 10- ЖК « Варшавский» Киев.
основная целевая аудитория  -жители, кто не хочет готовить , бригады по ремонту , молодёжь .
конкуренты на территории -кулинария Новуса, семейной пекарни по пирожкам.
Сейчас рекламной кампании нет , только проходящий трафик.
нужен бот автоматического приема заказа с адресом доставки . Можно обсудить так же рекламу через Инстаграм -
только с релевантными результатами в нише 

Прошу подавать ставки только тем специалистам, кто имеет результативный опыт в продвижении еды в Инстаграм и 
создании подобных ботов : сроки ограничены и важно, чтобы человек знал специфику успеха в этой нише 
'''

import sqlite3
import config
import menu
import telebot
from telebot import types
from PIL import Image

bot = telebot.TeleBot(config.TOKEN)

hello_count = []
data_base = []

base = sqlite3.connect('data base.db', check_same_thread=False)
cursor = base.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS shopping_cart (
    describe  TEXT,
    size TEXT,
    quantity INT
    )""")
base.commit()

SMS = None

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Графік і адреса")
    item2 = types.KeyboardButton("Асортимент")
    item3= types.KeyboardButton("Корзина")
    item4= types.KeyboardButton("/start")
 
    markup.add(item1, item2,item3,item4)

    bot.send_message(message.chat.id, "Привіт {0.first_name}!\nВітаємо в нашій маленькій пекарні".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    global SELF_ID
    SELF_ID = message.chat.id
    print(SELF_ID)

@bot.message_handler(content_types=['text'])
def language(message):
    if message.chat.type == 'private':
        if message.text == "Графік і адреса":
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Наша адреса",  url='https://goo.gl/maps/dHuhDU1jPPrin9uk9')

            markup.add(item1)

            bot.send_message(message.chat.id, 'Ми працюємо з 8.00 до 18.00', reply_markup=markup)
        if message.text == "Асортимент":
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Піца",  callback_data='pizza')
            item2 = types.InlineKeyboardButton("Пиріжки",  callback_data='pyrizhky')
            #item3= types.InlineKeyboardButton("Салати",  callback_data='salaty')
            #item4 = types.InlineKeyboardButton("Холодні напої",  callback_data='cold_drinks')
            item5 = types.InlineKeyboardButton("Гарячі напої",  callback_data='hot_drinks')

            markup.add(item1,item2,item5)

            bot.send_message(message.chat.id, 'Виберіть категорію', reply_markup=markup)

        elif message.text == "Корзина":
            bot.send_message(message.chat.id, "нажаль ми все ще працюємо над створенням цієї функції 😢")
            bot.send_message(message.chat.id, "😢")
            for value in cursor.execute("SELECT * FROM shopping_cart"):
                bot.send_message(call.message.chat.id, value)
                print(value)
        else:
            pass

@bot.callback_query_handler(func=lambda call: True )
def callback_inline(call):
    try:          
        if call.data == 'pizza':
            print('pizza')

            markup_shunka_syr = types.InlineKeyboardMarkup(row_width=1)
            markup_syry_4 = types.InlineKeyboardMarkup(row_width=1)
            markup_diabola = types.InlineKeyboardMarkup(row_width=1)
            item8 = types.InlineKeyboardButton("В корзину 30см", callback_data='in_shopping cart_30_shunka_syr')
            item9 = types.InlineKeyboardButton("В корзину 50см", callback_data='in_shopping cart_50_shunka_syr')
            item10 = types.InlineKeyboardButton("В корзину 30см", callback_data='in_shopping cart_30_4_s')
            item11 = types.InlineKeyboardButton("В корзину 50см", callback_data='in_shopping cart_50_4_s')
            item12 = types.InlineKeyboardButton("В корзину 30см", callback_data='in_shopping cart_30_dia')
            item13 = types.InlineKeyboardButton("В корзину 50см", callback_data='in_shopping cart_50_dia')

            markup_shunka_syr.add(item8, item9)
            markup_syry_4.add(item10, item11)
            markup_diabola.add(item12, item13)



            s_s=open('photo\\shunka_syr.jfif', 'rb')
            s4=open('photo\\syry_4.jfif', 'rb')
            dia=open('photo\\diabola.jfif', 'rb')

            bot.send_photo(call.message.chat.id, s_s, menu.shunka_syr,
                                                        parse_mode='html', reply_markup=markup_shunka_syr)
            bot.send_photo(call.message.chat.id, s4, menu.syry_4,
                                                        parse_mode='html', reply_markup=markup_syry_4)
            bot.send_photo(call.message.chat.id, dia, menu.diabola,
                                                        parse_mode='html', reply_markup=markup_diabola)
            print(SMS)
            s_s.close()
            s4.close()
            dia.close()
            
        elif call.data == 'pyrizhky':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item8 = types.InlineKeyboardButton("Додати в корзину", url='https://goo.gl/maps/dHuhDU1jPPrin9uk9')

            markup.add(item8)
            bot.send_photo(call.message.chat.id, open('photo\\p_syr.jfif', 'rb'), menu.p_syr,
                                                        parse_mode='html', reply_markup=markup)

            bot.send_photo(call.message.chat.id, open('photo\\p_kartoplia.jfif', 'rb'), menu.p_kartoplia,
                                                        parse_mode='html', reply_markup=markup)
            bot.send_photo(call.message.chat.id, open('photo\\p_varenia.jpg', 'rb'), menu.p_varenia,
                                                        parse_mode='html', reply_markup=markup)
              

        elif call.data == 'hot_drinks':
            print(SELF_ID)
            markup = types.InlineKeyboardMarkup(row_width=1)
            item8 = types.InlineKeyboardButton("Додати в корзину", url='https://goo.gl/maps/dHuhDU1jPPrin9uk9')

            markup.add(item8)

            bot.send_photo(call.message.chat.id, open('photo\\hd_coffe.jpg', 'rb'), menu.hd_coffe,
                                                        parse_mode='html', reply_markup=markup)
            bot.send_photo(call.message.chat.id, open('photo\\hd_capuchino.png', 'rb'), menu.hd_capuchino,
                                                        parse_mode='html', reply_markup=markup)
            #bot.send_message(call.message.chat.id, menu.hd_capuchino, reply_markup=markup) #просто текст без фото
            bot.send_photo(call.message.chat.id, open('photo\\hd_tea.jpg', 'rb'), menu.hd_tea,
                                                        parse_mode='html', reply_markup=markup)

        elif call.data == 'in_shopping cart_30_dia':
            cursor.execute(f"SELECT describe FROM shopping_cart WHERE describe = 'Діабола'")

            if cursor.fetchone() is None:
                sql = ("INSERT INTO shopping_cart VALUES (?,?,?)")
                val = ('Діабола', '30 см', 1)
                cursor.execute(sql, val)
                base.commit()
                print('доддано в бд')
                for value in cursor.execute("SELECT * FROM shopping_cart"):
                    print(value)
            else:
                cursor.execute(f'UPDATE shopping_cart SET quantity = quantity+1 WHERE describe = "Діабола"')
                base.commit()

        elif call.data == 'in_shopping cart_50_dia':
            cursor.execute("SELECT * FROM shopping_cart")
            for value in cursor.fetchall():
                data_base.append((str(value[0]) +' '+ str(value[1])+' '+str(value[2])))
                print(value)
                print('data')
                print(data_base)
            bot.send_message(call.message.chat.id, data_base)
            print(data_base)



            # remove inline buttons
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="тут має бути текст, який можна видалити з інлайнових клавіатур?",
                #reply_markup=None)

 
    except Exception as e:
        print(repr(e))

while True:  # Запускаем бота
    try:
        bot.polling(none_stop=True)
    except OSError:
        bot.polling(none_stop=True)
