# System
import logging as log
from os import environ
import sys

# Telegram BOT API
from telegram.error import InvalidToken
from telegram.ext import Updater

# Project
import rng
import base

# Configure logging
log.basicConfig(level=log.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Start the updater that receives events from telegram with the API key from config
log.info('Starting Bot Updater...')

API_TOKEN = environ.get('API_TOKEN')

try:
    updater = Updater(token=API_TOKEN)

except InvalidToken:
    log.error('The API TOKEN is invalid!')
    sys.exit(1)

log.info('Registering command handlers...')
base.add_handlers(updater.dispatcher)
rng.add_handlers(updater.dispatcher)

# Start polling events
log.info('Polling...')
updater.start_polling()
