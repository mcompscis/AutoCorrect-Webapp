import psycopg2

print("Running database.py")

conn = psycopg2.connect(database="word_count", user="postgres", password="munk21", host="localhost")

cur = conn.cursor()

cur.execute('''CREATE TABLE WORD_COUNT
          (COUNT INT NOT NULL, WORD TEXT NOT NULL);''')
print("table created successfully")

conn.commit()
conn.close()
