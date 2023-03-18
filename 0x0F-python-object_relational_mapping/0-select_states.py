#!/usr/bin/python3

"""This module lists all states from a database
It takes the following arguments:
    mysql username
    mysql password
    database name
"""

import MySQLdb
from sys import argv as argv


def db_connect(username, password, database, host="localhost", port=3306):
    connection = None
    connection = MySQLdb.connect(user=username, passwd=password, db=database)
    return connection


def db_cursor(connection):
    cursor = None
    cursor = connection.cursor()
    return cursor


def db_execute(cursor, command):
    rows = None
    rows = cursor.execute(command)
    return rows


def db_print_data(rows):
    data = None
    data = rows.fetchall()
    for row in data:
        print(f"{row}")
    return data


def db_clean_up(cursor, connection):
    cursor.close()
    connection.close()


if __name__ == '__main__':
    if len(argv) < 4:
        print('Usage: argv[0] <username> <password> <database>')
        exit()
    command = 'SELECT * FROM states ORDER BY id'
    connection = db_connect(argv[1], argv[2], argv[3])
    cursor = db_cursor(connection)
    rows = db_execute(cursor, command)
    data = db_print_data(cursor)
    db_clean_up(cursor, connection)
