from sqlalchemy import Column, Integer, String, Time, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import time

engine = create_engine('sqlite:///sales.db')
base = declarative_base()
Session = sessionmaker(engine)
print('Database connection established.')


class Provider(base):
    __tablename__ = 'provider'

    def __init__(self, name: str):
        self.name = name

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    canteens = relationship('Canteen', back_populates='provider')


class Canteen(base):
    __tablename__ = 'canteen'

    def __init__(self, provider_id: int, name: str, location: str, time_open: time, time_closed: time):
        self.provider_id = provider_id
        self.name = name
        self.location = location
        self.time_open = time_open
        self.time_closed = time_closed

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    location = Column(String(64), nullable=False)
    time_open = Column(Time, nullable=False)
    time_closed = Column(Time, nullable=False)
    provider_id = Column(Integer, ForeignKey('provider.id'))
    provider = relationship("Provider", back_populates="canteens")


def create_tables() -> None:
    """Create database tables."""
    base.metadata.create_all(engine)
    print('Tables created.')


def seed_data_list() -> None:
    """Seed data as one list."""
    providers = [Provider('Rahva Toit'),
                 Provider('TTÜ Sport OÜ'),
                 Provider('Baltic Restaurants Estonia AS'),
                 Provider('Bitt OÜ')]

    canteens = [Canteen(1, 'Economics- and social science building canteen', 'Akadeemia tee 3', time(8, 30), time(18, 30)),
                Canteen(3, 'Main building Daily lunch restaurant', 'Ehitajate tee 5', time(9, 00), time(16, 30)),
                Canteen(3, 'Natural Science building canteen', 'Akadeemia tee 15', time(9, 00), time(16, 00)),
                Canteen(3, 'Main building Deli cafe', 'Ehitajate tee 5', time(9, 00), time(16, 30)),
                Canteen(2, 'Sports building canteen', 'Männiliiva 7', time(11, 00), time(20, 00)),
                Canteen(1, 'U06 building canteen', 'Ehitajate tee 5', time(9, 00), time(16, 00)),
                Canteen(1, 'Library canteen', 'Akadeemia tee 1', time(8, 30), time(19, 00)),
                Canteen(3, 'ICT building canteen', 'Raja 15', time(9, 00), time(16, 00))]

    with Session() as session:
        session.add_all(providers)
        print("Data for 'provider' table seeded.")

        session.add_all(canteens)
        print("Data for 'canteen' table seeded.")

        session.commit()


def seed_data_single() -> None:
    """Seed data using separate statement."""
    with Session() as session:
        session.add(Canteen(4, 'bitStop KOHVIK', 'Raja 4c', time(9, 30), time(16, 00)))
        print("Single entry for 'canteen' table seeded.\n")

        session.commit()


def display_open_canteens(open: time, closed: time) -> None:
    """Get canteens which are open at the specified time."""
    with Session() as session:
        result = session.query(Canteen).filter(Canteen.time_open <= open, Canteen.time_closed >= closed)

    print(f'Canteens open between {open} - {closed}')
    for row in result:
        print(f'name: {row.name} | location: {row.location} | open: {row.time_open} | closed: {row.time_closed}')
    print()  # empty line


def display_canteens_by_provider(name: str) -> None:
    """Get canteens by specified provider."""
    with Session() as session:
        result = session.query(Canteen, Provider).where(Canteen.provider_id == Provider.id).filter(Provider.name == name)

    print(f'Canteens found by provider: {name}')
    for (canteen, provider) in result:
        print(f'name: {canteen.name} | location: {canteen.location} | open: {canteen.time_open} | closed: {canteen.time_closed} | provider: {provider.name}')
    print()  # empty line


if __name__ == '__main__':
    create_tables()
    seed_data_list()
    seed_data_single()
    display_open_canteens(time(9, 00), time(16, 20))
    display_canteens_by_provider('Baltic Restaurants Estonia AS')
