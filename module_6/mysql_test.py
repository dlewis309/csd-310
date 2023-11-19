import mysql.connector
from mysql.connector import errorcodes

config = {
    "user": "root",
    "password": "@Fatdaddy22",
    "host": "127.0.0.1",
    "Database": "movie",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
  
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
   
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()