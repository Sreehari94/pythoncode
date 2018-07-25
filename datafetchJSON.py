import urllib.request, json
import MySQLdb

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

   with urllib.request.urlopen("http://www.gamifyi.com/assets/thlist_1.json") as url:
      data = json.loads(url.read().decode())
      #print(data.get('body').get('treasureHunts'))
      treasureHuntDetail = data.get('body').get('treasureHunts')
      result = []

   sql_stmt="CREATE TABLE th_master( id int auto_increment primary key,th_id int,th_name varchar(255),city_id int);"
   cursor.execute(sql_stmt)
   #sql_stmt="INSERT INTO devices(name) VALUES('Router F1'),('Switch 1'),('Switch 2');"
   #cursor.execute(sql_stmt)
   
   for item in treasureHuntDetail:
      my_dict = {}
      my_dict['thId'] = item.get('treasureHuntId')
      my_dict['thName'] = item.get('treasureHuntName')
      my_dict['cityId'] = item.get('cityId')
      sql_stmt='INSERT INTO th_master(th_id,th_name,city_id) VALUES('+str(my_dict['thId'])+',"'+my_dict['thName']+'",'+str(my_dict['cityId'])+');'
      print(sql_stmt);
      cursor.execute(sql_stmt);
      if cursor.lastrowid:
         print('last insert id', cursor.lastrowid)
      else:
         print('last insert id not found')      
      db_connection.commit()

    # Closing Database Connection 
   db_connection.close()
 
# Function Call For Connecting To Our Database
mysqlconnect()