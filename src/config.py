import os
TOKEN = os.getenv("TOKEN") if os.getenv("TOKEN") else "YOUR TOKEN HERE" 
connection_string = "localhost:27017"
db_name = "DB"