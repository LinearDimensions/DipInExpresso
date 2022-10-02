from turtle import update
from telegram.ext import *
from dotenv import load_dotenv
from response import getResponse
import os

def configure():
    load_dotenv()

def sample_responses(input_text) :
    user_message = str(input_text).lower()
    print(user_message)
    return user_message

print("Bot Started")

def start_command(update, context):
    update.message.reply_text('Expresso helps to track your mental wellbeing through journal entries. Get reminders at random intervals and obtain advice to live a more positive life.')

def help_command(update, context):
    update.message.reply_text('/alarm :: set journal reminders \n/breakdown :: split into individual scores \n/past :: view past records \n ')

def handle_messages(update, context):
    text = str(update.message.text).lower()
    update.message.reply_text(getResponse(text))

def error(update, context):
    print("Update {} caused error {}".format(update, context.error))

def main():
    configure()
    updater = Updater(os.getenv('API_KEY'), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))

    dp.add_handler(MessageHandler(Filters.text,handle_messages))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
    
main()