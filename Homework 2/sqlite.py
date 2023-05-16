import sqlite3
from datetime import time


def create_connection() -> None:
    """Create database connection."""
    global connection
    global cursor

    connection = sqlite3.connect('diners.db')
    cursor = connection.cursor()
    print('Database connection established.')


def create_tables() -> None:
    """Create database tables."""
    provider = """CREATE TABLE provider (id INTEGER PRIMARY KEY NOT NULL,
                                         name VARCHAR(64) NOT NULL);"""

    canteen = """CREATE TABLE canteen (id INTEGER PRIMARY KEY NOT NULL,
                                       provider_id INTEGER NOT NULL,
                                       name VARCHAR(64) NOT NULL,
                                       location VARCHAR(64) NOT NULL,
                                       time_open TIME NOT NULL,
                                       time_closed TIME NOT NULL,
                                       FOREIGN KEY(provider_id) REFERENCES provider(id));"""

    cursor.execute(provider)
    print("Table 'provider' created.")

    cursor.execute(canteen)
    print("Table 'canteen' created.")

    connection.commit()


def seed_campus_data() -> None:
    """Seed data as one list."""
    providers = [('Rahva Toit',),
                 ('TTÜ Sport OÜ',),
                 ('Baltic Restaurants Estonia AS',),
                 ('Bitt OÜ',)]

    canteens = [(1, 'Economics- and social science building canteen', 'Akadeemia tee 3', time(8, 30), time(18, 30)),
                (3, 'Main building Daily lunch restaurant', 'Ehitajate tee 5', time(9, 00), time(16, 30)),
                (3, 'Natural Science building canteen', 'Akadeemia tee 15', time(9, 00), time(16, 00)),
                (3, 'Main building Deli cafe', 'Ehitajate tee 5', time(9, 00), time(16, 30)),
                (2, 'Sports building canteen', 'Männiliiva 7', time(11, 00), time(20, 00)),
                (1, 'U06 building canteen', 'Ehitajate tee 5', time(9, 00), time(16, 00)),
                (1, 'Library canteen', 'Akadeemia tee 1', time(8, 30), time(19, 00)),
                (3, 'ICT building canteen', 'Raja 15', time(9, 00), time(16, 00))]

    # convert time to string
    canteens = [(provider_id, name, location, time_open.strftime('%H:%M'), time_closed.strftime('%H:%M'))
                for provider_id, name, location, time_open, time_closed in canteens]

    cursor.executemany('INSERT INTO provider (name) VALUES (?);', providers)
    print("Data for 'provider' table seeded.")

    cursor.executemany('INSERT INTO canteen (provider_id, name, location, time_open, time_closed) VALUES (?, ?, ?, ?, ?);', canteens)
    print("Data for 'canteen' table seeded.")

    connection.commit()


def seed_ict_data() -> None:
    """Seed data using separate statement."""
    cursor.execute('INSERT INTO canteen (provider_id, name, location, time_open, time_closed) VALUES (?, ?, ?, ?, ?);',
                   (4, 'bitStop KOHVIK', 'Raja 4c', time(9, 30).strftime('%H:%M'), time(16, 00).strftime('%H:%M')))

    connection.commit()
    print("Single entry for 'canteen' table seeded.\n")


def display_open_canteens(open: str, closed: str) -> None:
    """Get canteens which are open at the specified time."""
    result = cursor.execute("""SELECT name, location, time_open, time_closed FROM canteen
                                WHERE time_open <= ? AND time_closed >= ?""", (open, closed)).fetchall()

    print(f'Canteens open between {open} - {closed}')
    for (name, location, time_open, time_closed) in result:
        print(f'name: {name} | location: {location} | open: {time_open} | closed: {time_closed}')
    print()  # empty line


def display_canteens_by_provider(provider: str) -> None:
    """Get canteens by specified provider."""
    result = cursor.execute("""SELECT c.name, c.location, c.time_open, c.time_closed, p.name
                                FROM canteen c, provider p
                                WHERE c.provider_id = p.id AND p.name = ?""", (provider,)).fetchall()

    print(f'Canteens found by provider: {provider}')
    for (name, location, time_open, time_closed, provider) in result:
        print(f'name: {name} | location: {location} | open: {time_open} | closed: {time_closed} | provider: {provider}')
    print()  # empty line


if __name__ == '__main__':
    create_connection()
    create_tables()
    seed_campus_data()
    seed_ict_data()
    display_open_canteens('09:00', '16:20')
    display_canteens_by_provider('Baltic Restaurants Estonia AS')
