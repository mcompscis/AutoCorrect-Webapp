
import psycopg2
from word_counter import word_count_25

print("Running insert_db.py")
try:
    conn = psycopg2.connect(database="word_count", user="postgres", password="munk21", host="localhost")

    curr = conn.cursor()

    first_25_words = list(word_count_25.keys())
    first_25 = list(word_count_25.values())

    count = 2
    for word, count in zip(first_25_words, first_25):
        if count > 0:
            postgres_insert = ''' INSERT INTO WORD_COUNT (COUNT,WORD) \
            VALUES (%s, %s)'''
            record_to_insert = (count, word)
            curr.execute(postgres_insert, record_to_insert)
            conn.commit()
            count -= 1

    print("Records created successfully")
except (Exception, psycopg2.Error) as error:
    print("Postgres error", error)
finally:
    if (conn):
        curr.close()
        conn.close()
