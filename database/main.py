import sqlite3
conn = sqlite3.connect('database/college.sqlite3')
cursor = conn.cursor()
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            age INTEGER,
            address TEXT
        )
    """)
    conn.commit()
    print('Table created successfully')

# create_table()


def insert_data(name,email,age,address):
    cursor.execute("""INSERT INTO students(name,email,age,address) VALUES(?,?,?,?)""",(name,email,age,address))
    conn.commit()
    print('Data inserted successfully')


# name = input('Enter your name: ')
# email = input('Enter your email: ')
# age = int(input('Enter your age: '))
# address = input('Enter your address: ')
# insert_data(name,email,age,address)


def show_record():
    # cursor.execute("""SELECT * FROM students""")
    cursor.execute("""SELECT name,email FROM students WHERE name='sophia' """)
    data = cursor.fetchall()
    # data = cursor.fetchone()
    # data = cursor.fetchmany(2)
    print(data)
   
# show_record()


def delete_data(id):
    cursor.execute("""DELETE FROM students WHERE id=?""",(id,))
    conn.commit()
    print('Data deleted successfully')


# delete_data(1)


def update(name,email,age,address,id):
    cursor.execute("""UPDATE students SET name=?,email=?,age=?,address=? WHERE id=?""",
                   (name,email,age,address,id))
    conn.commit()
    print('Data updated successfully')


update('ram','ran@gmail',25,'new york',2)
