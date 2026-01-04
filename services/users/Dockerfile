# 1. Use a modern, slim, and secure base image
FROM python:3.12-slim-bullseye

# 2. Set a consistent working directory
WORKDIR /usr/src/app

# 3. Install system dependencies for the entrypoint script
RUN apt-get update && apt-get install -y netcat-openbsd

# 4. Install python dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the entrypoint script
COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

# 6. Copy the rest of the application code
COPY . .

# 7. Expose the port FastAPI runs on
EXPOSE 8000

# 8. Define the command to run the application
CMD ["./entrypoint.sh"]
