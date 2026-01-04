# File: services/users/Dockerfile

# 1. Use a modern, slim, and secure base image
FROM python:3.12-slim-bullseye

# 2. Set a consistent working directory
WORKDIR /usr/src/app

# 3. Install dependencies first to leverage Docker's layer caching
# Copy only the requirements file
COPY ./requirements.txt .
# Install the dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the application code
COPY . .

# 5. Expose the port FastAPI runs on
EXPOSE 8000

# 6. Define the command to run the application
# Use the FastAPI CLI for the production-ready 'run' command
CMD ["fastapi", "run", "project", "--host", "0.0.0.0", "--port", "8000"]
