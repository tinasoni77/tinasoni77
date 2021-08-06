import sqlite3
connection=sqlite3.connect('Movies.db')
cursor=connection.cursor()


command1=""" CREATE TABLE IF NOT EXISTS Movies(name TEXT PRIMARY KEY,actor TEXT,actress TEXT, director TEXT,year INTEGER) """

cursor.execute(command1)


cursor.execute(" INSERT INTO Movies VALUES ('Holiday','Akshay Kumar','Sonakshi Sinha','A.R. Murugadoss',2014)")
cursor.execute(" INSERT INTO Movies VALUES ('Housefull4','Akshay Kumar','Kriti Sanon','Farhad Samji',2019)")
cursor.execute(" INSERT INTO Movies VALUES ('Golmaal3','Ajay Devgan','Kareena Kapoor','Rohit Shetty',2010)")
cursor.execute(" INSERT INTO Movies VALUES ('Bol Bachchan','Abhishek Bachchan','Asin Khan','Rohit Shetty',2012)")
cursor.execute(" INSERT INTO Movies VALUES ('Kabhi Khushi Kabhi Ghum','Shahrukh Khan','Kareena Kapoor','Karan Johar',2001)")


cursor.execute("SELECT * FROM Movies")
results=cursor.fetchall()

cursor.execute("SELECT * FROM Movies WHERE actor='Akshay Kumar'")
results2=cursor.fetchall()

#print the results
print('Movies: \n', results)
print('\n')
print("Information:\n",results2)
