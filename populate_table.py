import random
import sqlite3
from datetime import datetime
from datetime import timedelta
from faker import Faker

def populate_table():
    conn = sqlite3.connect("hotel.db")
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON")
    # Insert Rooms
    for i in range(1, 11):
        cursor.execute("""
            INSERT INTO Rooms (room_number, capacity, has_bathroom, has_balcony, price)
            VALUES (?, ?, ?, ?, ?)
        """, (
            100 + i,
            random.choice([1, 2, 3, 4]),
            random.choice([0, 1]),
            random.choice([0, 1]),
            round(random.uniform(50, 200), 2)
        ))

    # Insert RoomImages
    for i in range(1, 11):
        dummy_image = b"binary_image_data"
        description = f"View of Room {100 + i}".encode("utf-8")
        cursor.execute("""
            INSERT INTO RoomImages (image_id, room_id, image, description)
            VALUES (?, ?, ?, ?)
        """, (i, i, dummy_image, description))

    # Insert People
    first_names = ['Anna', 'Ben', 'Cara', 'David', 'Eva', 'Frank', 'Gina', 'Hugo', 'Ivy', 'Jack']
    last_names = ['Smith', 'Brown', 'Taylor', 'Lee', 'Walker', 'Moore', 'Hall', 'Young', 'King', 'Scott']
    streets = ['Oak St', 'Maple Rd', 'Pine Ave', 'Elm Ln']

    for i in range(15):
        cursor.execute("""
            INSERT INTO People (first_name, last_name, address, phone)
            VALUES (?, ?, ?, ?)
        """, (
            random.choice(first_names),
            random.choice(last_names),
            f"{random.randint(100, 999)} {random.choice(streets)}, City {random.randint(1, 5)}",
            f"+421 9{random.randint(0,9)}{random.randint(1000000, 9999999)}"
        ))

    # Insert Bookings
    for i in range(1, 11):
        room_id = random.randint(1, 10)
        check_in = datetime.now() + timedelta(days=random.randint(-30, 10))
        check_out = check_in + timedelta(days=random.randint(1, 7))
        cursor.execute("""
            INSERT INTO Bookings (room_id, check_in_date, check_out_date)
            VALUES (?, ?, ?)
        """, (
            room_id,
            check_in.strftime("%Y-%m-%d %H:%M:%S"),
            check_out.strftime("%Y-%m-%d %H:%M:%S")
        ))

    # Insert Guests (20 total, no duplicate pairs)
    guest_pairs = set()
    while len(guest_pairs) < 20:
        booking_id = random.randint(1, 10)
        person_id = random.randint(1, 15)
        if (booking_id, person_id) not in guest_pairs:
            guest_pairs.add((booking_id, person_id))
            cursor.execute("""
                INSERT INTO Guests (booking_id, person_id)
                VALUES (?, ?)
            """, (booking_id, person_id))

    # Commit and close
    conn.commit()
    conn.close()

    print("Database populated with mock data.")

if __name__ == '__main__':
    populate_table()