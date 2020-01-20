import psycopg2
from collections import Counter


if __name__ == "__main__":
    print("Running show.py ")
    getDbPairs()

def getDbPairs():
    # print("Running show.py")
    conn = psycopg2.connect(database="word_count", user="postgres", password="munk21", host="localhost")

    cur = conn.cursor()

    cur.execute("SELECT word, sum FROM order_words")
    rows = cur.fetchall()
    count = 0
    my_dict = dict()
    for row in rows:
        # print (row)
        # print("Word: ", row[0])
        # print("Count: ", row[1])
        count += 1
        my_dict[row[0]] = row[1]
    # print(count)
    conn.close()
    db_pairs = my_dict
    return db_pairs


# print(len(list(db_pairs.keys())))
# print(Counter(db_pairs).most_common(50))
