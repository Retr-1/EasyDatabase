import sqlite3

def create_table():
    connection = sqlite3.connect('hotel.db')
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON")

    ROOM_MAIN_TABLE = """
    CREATE TABLE IF NOT EXISTS Rooms (
        room_id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_number INTEGER UNIQUE,
        capacity INTEGER,
        has_bathroom BOOL,
        has_balcony BOOL,
        price REAL
    );
    """

    ROOM_IMAGES_TABLE = """
    CREATE TABLE IF NOT EXISTS RoomImages (
        image_id INTEGER PRIMARY KEY,
        room_id INTEGER,
        image MEDIUMBLOB,
        description BLOB,
        FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
    );
    """

    PEOPLE_TABLE = """
    CREATE TABLE IF NOT EXISTS People (
        person_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        address TEXT,
        phone TEXT
    );
    """

    BOOKINGS_TABLE = """
    CREATE TABLE IF NOT EXISTS Bookings (
        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_id INTEGER,
        check_in_date DATETIME,
        check_out_date DATETIME,
        FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
    );
    """
    GUESTS_TABLE = """
    CREATE TABLE IF NOT EXISTS Guests (
        booking_id INTEGER,
        person_id INTEGER,
        UNIQUE (booking_id, person_id),
        FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id),
        FOREIGN KEY (person_id) REFERENCES People(person_id)
    );
    """

    for table in (ROOM_MAIN_TABLE, ROOM_IMAGES_TABLE, PEOPLE_TABLE, BOOKINGS_TABLE, GUESTS_TABLE):
        # print(table)
        cursor.execute(table)

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_table()