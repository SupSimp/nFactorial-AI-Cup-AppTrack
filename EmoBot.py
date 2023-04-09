#t.me/EmoTerm_bot
#import telebot
#bot = telebot.TeleBot("6183059196:AAHrAIjR_qZJ_foJk6QOI7rhrqaYqdOLPJ0")

# Определение команды /start
#@bot.message_handler(commands=['start'])
#def send_welcome(message):
#    bot.reply_to(message, "Hi, you can use this bot to determ text emotional context")

# Определение обработчика сообщений
#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)

# Запуск бота
#bot.polling



import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello, please write your messages, and I will try to predict the mood of thr person")

def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

updater = Updater(token='6183059196:AAHrAIjR_qZJ_foJk6QOI7rhrqaYqdOLPJ0', use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()



