from sqlmodel import SQLModel, Session, create_engine
from models import Department, Employee

DB_FILE = 'db.sqlite3'
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True, connect_args={"check_same_thread": False})

def create_tables():
    """Create the tables registered with SQLModel.metadata (i.e classes with table=True).
    More info: https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata
    """
    SQLModel.metadata.create_all(engine)

def get_session():
    """ Dependency function - yields Session object to FastAPI routes """
    with Session(engine) as session:
        yield session

if __name__ == '__main__':
    # creates the table if this file is run independently, as a script
    create_tables()