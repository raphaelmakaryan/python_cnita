import sqlite3
connection = sqlite3.connect('../bottle_venv/todo.db') # Warning: This file is created in the current directory
cursor = connection.cursor()
cursor.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
cursor.execute("INSERT INTO todo (task,status) VALUES ('Read the Python tutorial to get a good introduction into Python',0)")
cursor.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
cursor.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
cursor.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
connection.commit()