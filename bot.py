import logging
import test
import time
import subprocess
import requests
import json
import pytest
import sys
import subprocess
import time
from selenium.webdriver.common.by import By
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters


TOKEN = ''
ALLURE_URL = 'http://10.127.0.133'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Web E2E test bot started")

    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fetch_url = str(update.message.text)
    message_id = str(update.message.id)
    result = f'Check: {fetch_url} id: {message_id}'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)
    # create new project Allure
    requests.post(f"{ALLURE_URL}:5050/projects", headers={'Content-Type': 'application/json'}, json={'id': message_id})
    # run pytest
    pytest.main(['-svv', '-q', '--browser_name=chrome', f'--alluredir=results/projects/{message_id}/results/', f'--message_id={message_id}'])
    # send video
    await context.bot.send_document(chat_id=update.effective_chat.id, document=f'./results/video/{message_id}.mp4')
    # send reports URL
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{ALLURE_URL}/allure-docker-service-ui/projects/{message_id}/reports/latest')


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    application.run_polling()


updater.start_polling()
