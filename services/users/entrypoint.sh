#!/bin/sh
# File: services/users/entrypoint.sh

echo "Waiting for postgres..."

while ! nc -z users-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

fastapi dev project --host 0.0.0.0 --port 8000
