import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import test
import time
import subprocess

TOKEN = ''

import pytest
import sys
import subprocess
from selenium.webdriver.common.by import By
import time

# subprocess.Popen(['pytest', '-vv', '-q', '--browser_name=chrome', '--alluredir=results/allure_report']) #  -vv -q --browser_name="chrome" --alluredir=results/allure_report

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fetch_url = str(update.message.text)
    message_id = str(update.message.id)
    result = f'Check: {fetch_url} id: {message_id}'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    # subprocess.run(['pytest' '-vv' '-q' '--browser_name="chrome"' '--alluredir=results/allure_report'])
    time.sleep(3)
    await context.bot.send_document(chat_id=update.effective_chat.id, document=f'/root/selenoid-seleniumwire/video/{message_id}.mp4')

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    application.run_polling()

updater.start_polling()