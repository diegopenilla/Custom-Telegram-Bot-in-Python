#!/usr/bin/env python
BOT_TOKEN = "" # TODO: put your bot token here

import logging
import random
from telegram import ForceReply, Update, ReplyKeyboardMarkup
from telegram.constants import ParseMode, ChatAction
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from utils import send_action


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)
logger = logging.getLogger(__name__)


#_______________________________HANDLERS____________________________________
@send_action(ChatAction.TYPING)
async def respond_hello(update: Update,
                        context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /hello is issued."""
    user = update.effective_user
    if user:
        await update.message.reply_text(
            f"Yoo {user.username}!",
            reply_markup=ForceReply(selective=True),
        ) 

@send_action(ChatAction.TYPING)
async def markdown_response(update: Update,
                            context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /markdown is issued."""
    bot, chat = context.bot,update.effective_chat
    if bot and chat:
        await bot.send_message(chat_id=chat.id, 
                    text='''*bold* _italic_ `code` [text](link)''', # TODO: put medium link
                    parse_mode=ParseMode.MARKDOWN_V2)

@send_action(ChatAction.TYPING)
async def compute_sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args, chat = context.args, update.effective_chat
    if args and chat:
        result = [arg for arg in args if arg.isdigit()]
        await context.bot.send_message(
            chat_id=chat.id,
            text=f"Sum of given numbers is: {sum(map(int, result))}.")

@send_action(ChatAction.TYPING)
async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    if chat:
        await context.bot.send_message(
            chat_id=chat.id,
            text="I don't know how to respond to that command.")


async def return_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    custom_keyboard = [['/sum 1 1', '/sum 2 2 2 2'], 
                   ['/sum 3 3 3', '/sum 4 4 4']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    
    chat = update.effective_chat
    if chat:
        await context.bot.send_message(
            chat_id=chat.id, 
            text="Simple Keyboard Example", 
            reply_markup=reply_markup
        )

async def random_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    seed = random.randint(1, 100)
    if chat:
        await context.bot.send_document(chat_id=chat.id, document=f'https://picsum.photos/seed/{str(seed)}/200/300')

#_______________________________MAIN________________________________________


def main() -> None:
    """Start the bot."""
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("hello", respond_hello))
    app.add_handler(CommandHandler("markdown", markdown_response))
    app.add_handler(CommandHandler("sum", compute_sum))
    app.add_handler(CommandHandler("sum_keyboard", return_keyboard))
    app.add_handler(CommandHandler("random_image", random_image))
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command)) 
    
    app.run_polling()


if __name__ == "__main__":
    main()