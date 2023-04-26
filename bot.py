import requests
from datetime import datetime
import telebot
from auth_info import TOKEN



def telegram_bot(TOKEN):
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет! Введи price, чтобы узнать курс BTC)")


    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%d-%m-%Y %H:%M')}\nSell BTC price: {sell_price}")
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Что-то пошло не так...")
        else:
            bot.send_message(message.chat.id, "Вы неправильно ввели команду, попробуйте price)))")



    bot.polling()



if __name__ == '__main__':
    telegram_bot(TOKEN)