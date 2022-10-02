from turtle import update
from telegram.ext import *
from os import API_KEY
import NLP


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
    output = ''
    ##for sentiment, category in NLP.predict(text):
    output += ('{}: \t['.format('Gayness') + '='*10 + '-'*(10-10) + '] {}0%'.format(10) + '\n')
    output += ('{}: \t['.format('Sexiness') + '='*10 + '-'*(10-10) + '] {}0%'.format(10) + '\n')
    output += ('{}: \t8'.format('Cock size') + '='*10 + '-'*(10-10) + 'D  <3' '\n')
    update.message.reply_text(output)

def error(update, context):
    print("Update {} caused error {}".format(update, context.error))

def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))

    dp.add_handler(MessageHandler(Filters.text,handle_messages))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
    
main()