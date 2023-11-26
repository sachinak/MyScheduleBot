#!/usr/bin/env bash
echo "Creating mongo users..."
mongo admin --host localhost -u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD --eval "db.createUser({user: '$HANDLER', pwd: '$HANDLER_PASSWORD', roles: [{role: 'readWrite', db: 'Schedulebot'}]})"
echo "Mongo users created."