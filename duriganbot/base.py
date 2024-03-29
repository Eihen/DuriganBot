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
        'Here are the list of available commands:' +
        '\n/nft: real-time NFT data' +
        '\n/rand {a} {b} {n}: generate {n} random integer numbers between {a} and {b}' +
        '\n/randf {a} {b} {n}: generate {n} random real numbers between {a} and {b}'
    )

# /nft
def nft_handler(bot, update):
    update.message.reply_text('Not here, bye!')
    bot.kick_chat_member(update.message.chat.id, update.message.from_user.id)

def add_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(CommandHandler('help', help_handler))
    dispatcher.add_handler(CommandHandler('nft', nft_handler))
