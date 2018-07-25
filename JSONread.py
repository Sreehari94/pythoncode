import MySQLdb
 
# Function for connecting to MySQL database
def mysqlconnect():
   #Trying to connect 
   try:
      db_connection= MySQLdb.connect("localhost","root","Test@123","employee")
   # If connection is not successful
   except:
      print("Can't connect to database")
      return 0
   # If Connection Is Successful
   print("Connected")
 
   # Making Cursor Object For Query Execution
   cursor=db_connection.cursor()
 
   # Executing Query
   cursor.execute("DROP TABLE IF EXISTS events")

   #sql_stmt="CREATE TABLE events( id int auto_increment primary key, event_name varchar(255), visitor varchar(255), properties json, browser json);"
   #cursor.execute(sql_stmt)
   #sql_stmt="INSERT INTO devices(name) VALUES('Router F1'),('Switch 1'),('Switch 2');"
   #cursor.execute(sql_stmt)
   
   '''sql_stmt="SELECT id, browser->'$.name' browser FROM events;"
   cursor.execute(sql_stmt)
   results = cursor.fetchall()
   for row in results:
      id=row[0]
      browser=row[1]
      print("id="+str(id)+",browser="+browser)
   if cursor.lastrowid:
      print('last insert id', cursor.lastrowid)
   else:
      print('last insert id not found')'''
   db_connection.commit()
    # Closing Database Connection 
   db_connection.close()
 
# Function Call For Connecting To Our Database
mysqlconnect()