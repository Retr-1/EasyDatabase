import random
import sqlite3
from datetime import datetime
from datetime import timedelta

def populate_table():
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()
    for i in range(1, 21):
        room_number = 100 + i
        capacity = random.choice([1, 2, 3, 4])
        has_bathroom = random.choice([0, 1])
        has_balcony = random.choice([0, 1])
        price = round(random.uniform(50, 300), 2)
        cursor.execute("""
            INSERT INTO Rooms (room_number, capacity, has_bathroom, has_balcony, price)
            VALUES (?, ?, ?, ?, ?)
        """, (room_number, capacity, has_bathroom, has_balcony, price))

    # Insert dummy RoomImages (1 image per room, just simulating as binary data)
    for room_id in range(1, 21):
        dummy_image = b"This would be binary image data"
        cursor.execute("""
            INSERT INTO RoomImages (room_id, image)
            VALUES (?, ?)
        """, (room_id, dummy_image))

    # Sample names and addresses
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Chris', 'Diana', 'Eva', 'Frank', 'Grace', 'Henry']
    last_names = ['Smith', 'Doe', 'Brown', 'Taylor', 'Wilson', 'Clark', 'Lopez', 'Lee', 'Turner', 'White']
    streets = ['Main St', 'High St', 'Maple Ave', 'Oak Rd', 'Pine Ln']

    # Insert People
    for i in range(1, 21):
        first = random.choice(first_names)
        last = random.choice(last_names)
        address = f"{random.randint(100, 999)} {random.choice(streets)}, City {random.randint(1, 10)}"
        phone = f"+421 9{random.randint(0,9)}{random.randint(1000000, 9999999)}"
        cursor.execute("""
            INSERT INTO People (first_name, last_name, address, phone)
            VALUES (?, ?, ?, ?)
        """, (first, last, address, phone))

    # Insert Bookings (20 total, matching existing room and person IDs)
    for i in range(1, 21):
        room_id = random.randint(1, 20)
        person_id = random.randint(1, 20)
        check_in = datetime.now() + timedelta(days=random.randint(-10, 10))
        check_out = check_in + timedelta(days=random.randint(1, 10))
        cursor.execute("""
            INSERT INTO Bookings (room_id, person_id, check_in_date, check_out_date)
            VALUES (?, ?, ?, ?)
        """, (room_id, person_id, check_in.strftime("%Y-%m-%d %H:%M:%S"), check_out.strftime("%Y-%m-%d %H:%M:%S")))

    # Commit and close
    conn.commit()
    conn.close()

    print("Mock data successfully inserted into hotel.db")

if __name__ == '__main__':
    populate_table()