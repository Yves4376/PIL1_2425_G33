from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import os

class DatabaseManager:
    def __init__(self):
        self.engine = create_engine(
            os.getenv("DB_URL"),
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10
        )
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        """Fournit une nouvelle session SQLAlchemy"""
        return self.Session()

# Instance singleton
db_manager = DatabaseManager()