from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import dotenv as dotenv
import telebot
import logging
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

def setup():
    

if __name__ == "__main__":
    dotenv.load_dotenv()
    print("Привет!")

