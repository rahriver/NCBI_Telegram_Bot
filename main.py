import APKEY as keys
import NCBI_Funcs as N
from telegram.ext import *
import Responses as R

print("Bip bip boop...")

def start(update, context):
    update.message.reply_text("Genomix is a bot that can help you to get gene data in file format directly from NCBI and do more!\n\n/start -> Start the bot\n")
    update.message.reply_text("Send me the gene id and I will return some information about that gene!")
    update.message.reply_text("Enter Gene ID: ")

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def handle(update, context):
    gene_id = str(update.message.text)
    gene_info = N.gene_id(gene_id)
    update.message.reply_text(gene_info)

# def handle(update, context):
#     text = str(update.message.text).lower()
#     response = R.sample_responses(text)
#     update.message.reply_text(response)

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
