import os
import datetime
import pymysql

# Get username from Gitpod workspace - saved as an environment variable
# Modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-02-06 23:04")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
        #note that the above will still display a warning (not error) if the
        #table already exists
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
