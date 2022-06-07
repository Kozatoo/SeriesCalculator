import sqlite3
import os


def create_db(database_filename):
    # connect to SQLite
    con = sqlite3.connect(database_filename)

    # Create a Connection
    cur = con.cursor()

    # Drop users table if already exsist.
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("DROP Table IF EXISTS calculations")
    # Create users table  in db_web database
    sql = '''CREATE TABLE "users" (
			"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
			"username"	TEXT,
			"email"	TEXT,
			"password" TEXT
		)'''
    cur.execute(sql)
    sql = '''CREATE TABLE "calculations" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "owner" INTEGER,
            "type" TEXT,
            "input" NUMBER,
            "output" NUMBER
            )'''
    cur.execute(sql)
    # commit changes
    con.commit()

    # close the connection
    con.close()


if __name__ == '__main__':
    database_filename = os.environ.get('DATABASE_FILENAME', '../../database.db')
    create_db(database_filename)
