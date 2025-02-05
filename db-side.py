import sqlite3
import socket

def create_table(conn, c):
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("""
    CREATE TABLE IF NOT EXISTS Clients (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone TEXT,
        email TEXT UNIQUE,
        address TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS Rooms (
        room_id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_number TEXT NOT NULL UNIQUE,
        room_type TEXT NOT NULL,
        floor INTEGER NOT NULL,
        description TEXT,
        price REAL,
        is_occupied INTEGER DEFAULT 0
    );
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS Reservations (
        reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        room_id INTEGER,
        check_in_date DATE NOT NULL,
        check_out_date DATE NOT NULL,
        room_info TEXT,
        status TEXT DEFAULT 'ожидает подтверждения',
        comments TEXT,
        FOREIGN KEY (client_id) REFERENCES Clients(client_id),
        FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
    );
    """)

def handle_client_connection(client_socket, conn, c):
    request = client_socket.recv(1024).decode()
    print(f"Received: {request}")
    # Здесь можно добавить обработку запросов и выполнение SQL команд
    client_socket.send("ACK".encode())
    client_socket.close()

def start_server(conn, c):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)
    print("Server listening on port 9999")

    try:
        while True:
            client_sock, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            handle_client_connection(client_sock, conn, c)
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()
        conn.close()

if __name__ == '__main__':
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    create_table(conn, c)  
    start_server(conn, c)




