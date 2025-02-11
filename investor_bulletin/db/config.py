"""Database configuration module."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool
from typing import Generator

# CockroachDB connection URL
DATABASE_URL = "cockroachdb://root@database:26257/defaultdb?sslmode=disable"

# Create engine with the appropriate driver
engine = create_engine(
    DATABASE_URL,
    poolclass=NullPool,  # Disable connection pooling for CockroachDB
    echo=True  # Set to False in production
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create a new database session
def get_db() -> Generator:
    """
    Get a database session.

    Yields:
        Session: A SQLAlchemy session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
