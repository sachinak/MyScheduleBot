mongosh <<EOF
use $MONGO_INITDB_DATABASE

db.createCollection("Schedulebot")
db.createUser({
  user: '$MONGO_INITDB_USER',
  pwd: '$MONGO_INITDB_PWD',
  roles: [{
    role: 'readWrite',
    db: '$MONGO_INITDB_DATABASE'
  }]
})
EOF