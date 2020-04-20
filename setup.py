#!/usr/bin/env python3
"""
Packages Fotrune-Lite into a format more suitable for pip

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

# Import dependencies:
from os import listdir, remove
from os.path import dirname, isfile, join, realpath
from setuptools import setup
from sqlite3 import connect

# Declare constants:
DIR = dirname(realpath(__file__))

# Remove the database file, if it exists:
if isfile(join(DIR, "fortune_lite", "fortune.db")):
    remove(join(DIR, "fortune_lite", "fortune.db"))
    print(">> Removed old database")

# Compile the database:
CONN = connect(join(DIR, "fortune_lite", "fortune.db"))
print(">> Created database at \"" + join(DIR, "fortune_lite", "fortune.db") + "\"")
CURSOR = CONN.cursor()

# Create the database:
CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        offensive BOOLEAN NOT NULL
    )
""")
CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS fortunes (
        id INTEGER PRIMARY KEY,
        category INTEGER NOT NULL,
        data TEXT NOT NULL,
        FOREIGN KEY (category) REFERENCES categories (id)
    )
""")
print(">> Initialized local database")


# Define a method to parse a single file:
def readfile(name, location, off):
    """
    Parses the fortunes out of a single database file.
    :param name: The name of the file to open.
    :param location: The location of the fortune file.
    :param off: A boolean representing whether or not the file is considered
        offensive.
    """
    CURSOR.execute("INSERT INTO categories(name, offensive) VALUES (?, ?)",
                   (name, off))
    cat = CURSOR.lastrowid
    handle = open(location)
    data = handle.read().split("%")
    handle.close()

    # Add all entries to the database:
    for entry in range(1, len(data) - 1):
        CURSOR.execute("INSERT INTO fortunes(category, data) VALUES (?, ?)",
                       (cat, data[entry]))

# Read each regular file:
for file in listdir(join(DIR, "fortunes")):
    if isfile(join(DIR, "fortunes", file)):
        readfile(file, join(DIR, "fortunes", file), False)
        print(">> Added file \"" + file + "\"")

# Read each offensive file:
for file in listdir(join(DIR, "fortunes", "off")):
    if isfile(join(DIR, "fortunes", "off", file)):
        readfile(file, join(DIR, "fortunes", "off", file), True)
        print(">> Added offensive file \"" + file + "\"")

# Commit the changes:
CONN.commit()
CONN.close()
print(">> Changes committed")


# Open the README:
file = open("README.md")
readme = file.read()
file.close()

# Setup the package:
setup(name="fortune_lite",
      version="1.0.1",
      description="A Python implementation of fortune",
      long_description=readme,
      long_description_content_type="text/markdown",
      url="https://github.com/buck-ross/fortune_lite",
      author="Buckley Ross",
      author_email="buckleyross42@gmail.com",
      license="Apache 2.0",
      packages=["fortune_lite"],
      package_data={'': ['fortune.db']},
      include_package_data=True,
      scripts=["scripts/fortune"],
      zip_safe=False)
