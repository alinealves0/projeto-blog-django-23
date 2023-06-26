#!/bin/sh
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
    sleep 2
done

echo " Postgres Database Started Sucessfully($POSTGRES_HOST:$POSTGRES_PORT)"