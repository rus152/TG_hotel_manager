from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import dotenv as dotenv
import telebot
import logging
import socket



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

def send_test_signal():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))
    client_socket.send("TEST".encode())
    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")
    client_socket.close()

if __name__ == "__main__":
    dotenv.load_dotenv()
    print("Привет!")
    send_test_signal()

