import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Execute query to fetch titles in alphabetical order
cursor.execute("SELECT title FROM books ORDER BY title ASC")
titles = cursor.fetchall()

# Print titles
for title in titles:
    print(title[0])

# Close connection
conn.close()
