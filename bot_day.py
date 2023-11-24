import logging
from datetime import datetime

from telegram import Update 
from telegram.ext import Updater, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update: Update, context):
    update.message.reply_text("Привет! Я бот, который знает какой сегодня день.")


def get_current_day(update: Update, context):
    current_date = datetime.now().strftime("%d.%m.%Y")
    day_of_week = datetime.now().strftime("%A")
    update.message.reply_text(f'Сегодня {current_date}, {day_of_week}')

    
if __name__ == '__main__':
    updater = Updater("TOKEN")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("Какой сегодня день?", get_current_day))

    updater.start_polling()
    updater.idle()