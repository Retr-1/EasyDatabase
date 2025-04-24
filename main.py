import sqlite3

connection = sqlite3.connect('hilbert_hotel.db')
cursor = connection.cursor()

ROOM_MAIN_TABLE = """
CREATE TABLE IF NOT EXISTS Rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number INTEGER NOT NULL,
    capacity INTEGER,
    has_bathroom BOOL,
    has_balcony BOOL,
    price REAL,
)
"""

ROOM_IMAGES_TABLE = """
CREATE TABLE IF NOT EXISTS RoomImages (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    image MEDIUMBLOB,
)
"""

PEOPLE_TABLE = """
CREATE TABLE IF NOT EXISTS People (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    address TEXT,
    phone TEXT,
)
"""

RESERVATIONS_TABLE = """
CREATE TABLE IF NOT EXISTS Reservations (
    room_id 
)
"""