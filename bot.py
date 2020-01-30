import telebot

bot = telebot.TeleBot('982070792:AAHa8TSB2EM9EzXBBSq3UjHLMTXDQa6xsNA')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Hello', 'Adios')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, you wrote /start to me', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello, my creator')
    elif message.text.lower() == 'adios':
        bot.send_message(message.chat.id, 'Adios, bro')
    elif message.text.lower() == 'now draft is from 18':
        bot.send_sticker(message.chat.id, 'CAADAgAD5QADGB0GD5OubeaA2IroFgQ')

#for stickers
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling();
