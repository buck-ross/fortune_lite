#!/usr/bin/env python3
"""
Provides the implementation of the fortune module.

Copyright 2019 Buckley Ross

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Import all dependencies:
from sqlite3 import connect


# Connect to the database:
def get_connection(location):
    """
    Obtains a handle to the database
    :return: A tuple representing the database connection & cursor.
    """
    conn = connect(location)
    cursor = conn.cursor()

    # Create the database:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            offensive BOOLEAN NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fortunes (
            id INTEGER PRIMARY KEY,
            category INTEGER NOT NULL,
            data TEXT NOT NULL,
            FOREIGN KEY (category) REFERENCES categories (id)
        )
    """)
    return (conn, cursor)


# Close connection:
def close_connection(conn):
    """
    Closes the provided connection.
    :param conn: A handle to the database connection which needs to be closed.
    """
    conn[0].close()


# Define a method to obtain a list of all categories:
def list_categories(conn):
    """
    Obtains a list of all fortunes from the database.
    :param conn: A handle to the database connection.
    :return: A list of all categories.
    """
    conn[1].execute("SELECT name, offensive FROM categories")
    res = conn[1].fetchall()
    out = []
    for i in res:
        if i[1]:
            out.append("off/" + i[0])
        else:
            out.append(i[0])
    return out


# Define a method to obtain a list of all offensive categories:
def list_offensive_categories(conn):
    """
    Obtains a list of all offensive fortunes from the database.
    :param conn: A handle to the database connection.
    :return: A list of all categories.
    """
    conn[1].execute("SELECT name FROM categories WHERE offensive = 1")
    res = conn[1].fetchall()
    out = []
    for i in res:
        out.append("off/" + i[0])
    return out


# Define a method to obtain a list of all appropriate categories:
def list_appropriate_categories(conn):
    """
    Obtains a list of all appropriate fortunes from the database.
    :param conn: A handle to the database connection.
    :return: A list of all categories.
    """
    conn[1].execute("SELECT name FROM categories WHERE offensive = 0")
    res = conn[1].fetchall()
    out = []
    for i in res:
        out.append(i[0])
    return out


# Define a method to select a random category from the database:
def select_random_category(conn):
    """
    Obtains one random category from the database.
    :param conn: A handle to the database connection.
    :return: A random category id.
    """
    conn[1].execute("SELECT id FROM categories ORDER BY RANDOM() LIMIT 1")
    return conn[1].fetchall()[0][0]


# Define a method to select a random offensive category from the database:
def select_random_offensive_category(conn):
    """
    Obtains one random offensive category from the database.
    :param conn: A handle to the database connection.
    :return: A random category id.
    """
    conn[1].execute("SELECT id FROM categories WHERE offensive = 1 ORDER "
                    + "BY RANDOM() LIMIT 1")
    return conn[1].fetchall()[0][0]


# Define a method to select a random appropriate category from the database:
def select_random_appropriate_category(conn):
    """
    Obtains one random appropriate category from the database.
    :param conn: A handle to the database connection.
    :return: A random category id.
    """
    conn[1].execute("SELECT id FROM categories WHERE offensive = 0 ORDER "
                    + "BY RANDOM() LIMIT 1")
    return conn[1].fetchall()[0][0]


# Define a method to select a random fortune from a given category:
def select_random_from_category(conn, cat):
    """
    Obtains a random fortune from a given category.
    :param conn: A handle to the database connection.
    :param cat: The category ID.
    :return: The text of the fortune.
    """
    conn[1].execute("SELECT data FROM fortunes WHERE category = ? ORDER BY "
                    + "RANDOM() LIMIT 1", (str(cat),))
    return conn[1].fetchall()[0][0]


# Define a method to select a random fortune:
def select_random(conn):
    """
    Obtains a random fortune.
    :param conn: A handle to the database connection.
    :return: The text of the fortune.
    """
    conn[1].execute("SELECT data FROM fortunes ORDER BY RANDOM() LIMIT 1")
    return conn[1].fetchall()[0][0]


# Define a method to select a random offensive fortune:
def select_random_offensive(conn):
    """
    Obtains a random offensive fortune.
    :param conn: A handle to the database connection.
    :return: The text of the fortune.
    """
    conn[1].execute("SELECT data FROM fortunes INNER JOIN categories ON "
                    + "fortunes.category = categories.id WHERE offensive = "
                    + "1 ORDER BY RANDOM() LIMIT 1")
    return conn[1].fetchall()[0][0]


# Define a method to select a random appropriate fortune:
def select_random_appropriate(conn):
    """
    Obtains a random appropriate fortune.
    :param conn: A handle to the database connection.
    :return: The text of the fortune.
    """
    conn[1].execute("SELECT data FROM fortunes INNER JOIN categories ON "
                    + "fortunes.category = categories.id WHERE offensive = "
                    + "0 ORDER BY RANDOM() LIMIT 1")
    return conn[1].fetchall()[0][0]
