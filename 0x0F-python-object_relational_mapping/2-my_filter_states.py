#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
<<<<<<< HEAD
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
=======
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
>>>>>>> 8ab0db420820730e26b3e7617f81a1ef20c6a26b
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
<<<<<<< HEAD
=======

>>>>>>> 8ab0db420820730e26b3e7617f81a1ef20c6a26b
