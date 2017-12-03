from telegram.ext import CommandHandler
from telegram import ParseMode


# /start
def start_handler(bot, update):
    update.message.reply_text(
        'Hi, I\'m *Durigan*, your virtual concierge!\nFor information about what I can do use /help',
        parse_mode=ParseMode.MARKDOWN
    )


# /help
def help_handler(bot, update):
    update.message.reply_text(
        'Here are the list of available commands:'
    )


def add_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(CommandHandler('help', help_handler))
