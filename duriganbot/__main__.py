# System
import configparser
import logging as log
import os
import sys

# Telegram BOT API
from telegram.error import InvalidToken
from telegram.ext import Updater

# Project
import rng
import base

# Configure logging
log.basicConfig(level=log.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Read the config file
log.info('Reading config.ini file...')

config = configparser.ConfigParser()
if not config.read(os.path.abspath(os.path.dirname(__file__)) + '/config.ini'):
    log.error('File config.ini don\'t exists!')
    sys.exit(1)

try:
    API_TOKEN = config.get('API', 'TOKEN')

except configparser.NoSectionError:
    log.error('Could not find section API in config.ini file!')
    sys.exit(1)

except configparser.NoOptionError:
    log.error('Could not find TOKEN in API section of config.ini file!')
    sys.exit(1)

if not API_TOKEN:
    log.error('Value of TOKEN in API section of config.ini is not set!')
    sys.exit(1)

# Start the updater that receives events from telegram with the API key from config
log.info('Starting Bot Updater...')

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
