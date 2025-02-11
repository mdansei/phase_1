# Dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

ENV PYTHONPATH=/app/investor_bulletin
# Install Poetry
RUN pip install poetry "poetry==2.0.1"

# Copy the poetry.lock and pyproject.toml files into the container
COPY pyproject.toml poetry.lock ./

# Install the dependencies using Poetry
RUN poetry install --no-root

# Copy the entire application code into the container
COPY . .


# Expose the port that the app runs on
EXPOSE 8000

# Command to run the migrations and the application
ENTRYPOINT ["sh", "./entrypoint.sh"]
