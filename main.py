from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import dotenv as dotenv
import telebot
import logging
import os
import sqlite3



def setup_logging(filename: str) -> None:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(filename, 'a')
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

def sql_headler(comand, return_data=False):
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()

    c.execute(comand)
    conn.commit()
    conn.close()
    pass

def bot_headler():
    token = os.getenv('TG-TOKEN')
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start', 'help'])
    def handle_start_help(message):
        bot.reply_to(message, "Привет! Тут ни*уя не готово :D")

    @bot.message_handler(content_types=['text'])
    def handle_message(message):
        bot.reply_to(message, message.text)

    bot.polling(none_stop=True)


if __name__ == "__main__":
    dotenv.load_dotenv()
    bot_headler()



    
    
    

