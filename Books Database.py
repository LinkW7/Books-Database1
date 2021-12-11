import sqlite3
connection = sqlite3.connect('books.db')

import pandas as pd
pd.options.display.max_columns = 10
# Demonstrate authers table
print(pd.read_sql('SELECT * FROM authors', connection, index_col=['id']))
print()

# Demonstrate titles table
print(pd.read_sql('SELECT * FROM titles', connection))
print()

# Demonstrate auther_ISBN table
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
print(df.head())
print()

print(pd.read_sql('SELECT first, last FROM authors', connection))
print()

# Filter the records that match the criteria
print(pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection))
print()

print(pd.read_sql("""SELECT id, first, last FROM authors WHERE last LIKE 'D%'""", connection, index_col=['id']))
print()

print(pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""", connection, index_col=['id']))
print()

# Sort by some columns
print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))
print()

print(pd.read_sql('SELECT id, first, last FROM authors ORDER BY last, first', connection, index_col=['id']))
print()

print(pd.read_sql('SELECT id, first, last FROM authors ORDER BY last DESC, first ASC', connection, index_col=['id']))
print()

print(pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title""", connection))
print()

print(pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first""", connection).head())
print()

cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")
print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))
print()
 
cursor = cursor.execute("""UPDATE authors SET last='Black' WHERE last='Red' AND first='Sue'""")
print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))
print()

cursor = cursor.execute('DELETE FROM authors WHERE id=6')
print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))
print()
