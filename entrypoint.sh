#!/bin/sh

# Run Alembic migrations
echo "Running Alembic migrations..."
poetry run alembic upgrade head

echo $PYTHONPATH
# Start the FastAPI application
echo "Starting FastAPI application..."
exec poetry run uvicorn investor_bulletin.api.main:app --host 0.0.0.0 --port 8000
