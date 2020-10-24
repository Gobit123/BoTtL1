import logging

from telegram.ext import Updater, CommandHandler




updater = Updater(token='1158936869:AAH7LOubpd0DuQROcGQIiYrT26rVcPvj2Ds')
dispatcher = updater.dispatcher

def start(upd, ctx):
    ctx.bot.send_message(
        chat_id=upd.effective_chat.id,
        text="Hello World!",
    )


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

if __name__ == '__main__':
    updater.start_polling()