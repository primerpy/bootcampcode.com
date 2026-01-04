# File: services/users/project/db/Dockerfile

# base image
FROM postgres:16-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
