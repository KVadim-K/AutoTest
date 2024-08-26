import sqlite3

def init_db():
   conn = sqlite3.connect(':memory:')  #данные будут сохраняться не на диске, а только в оперативной памяти и только во время работы программы;
   # conn = sqlite3.connect('users.db')  # база данных будет сохраняться в файле users.db на диске
   cursor = conn.cursor()
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY,
   name TEXT,
   age INTEGER)
   ''')
   return conn
def add_user(conn, name, age):
   cursor = conn.cursor()
   cursor.execute('''
   INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
   conn.commit()


def get_user(conn, name):
   cursor = conn.cursor()
   cursor.execute('''
   SELECT * FROM users WHERE name = ?''', (name,))
   return cursor.fetchone()  # используем метод fetchone для извлечения первой строки результата.






