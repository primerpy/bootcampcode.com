# FastAPI Microservices with Docker

[![CI](https://github.com/primerpy/bootcampcode.com/actions/workflows/main.yml/badge.svg)](https://github.com/primerpy/bootcampcode.com/actions/workflows/main.yml)

A production-ready FastAPI microservice with PostgreSQL, Docker, and comprehensive testing.

## Quick Start

```bash
# Build and start containers
docker compose up -d --build

# Create database tables
docker compose exec users python manage.py recreate_db

# Seed the database
docker compose exec users python manage.py seed_db

# Run tests
docker compose exec users python manage.py test
