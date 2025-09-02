import os
from sqlmodel import create_engine, Session, SQLModel

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}

def drop_db_file():
    # Dispose engine before deleting the file to release any locks
    if os.path.exists(sqlite_file_name):
        try:
            engine.dispose()
        except Exception:
            pass
        try:
            os.remove(sqlite_file_name)
        except PermissionError:
            print("PermissionError: database.db is in use. Please close all processes using it and try again.")
            return False
    return True

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def migrate_fresh():
    global engine
    # Dispose engine before dropping file
    if drop_db_file():
        # Recreate engine after file deletion
        engine = create_engine(sqlite_url, connect_args=connect_args)
        create_db_and_tables()
        print("Database file deleted and tables recreated (migrate:fresh)")

engine = create_engine(sqlite_url, connect_args=connect_args)

if __name__ == "__main__":
    migrate_fresh()