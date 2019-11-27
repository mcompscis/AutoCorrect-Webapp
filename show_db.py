import psycopg2
from collections import Counter
# import time

# start_time = time.process_time()
if __name__ == "__main__":
    print("Running show.py")
    getDbPairs()

def getDbPairs():
    conn = psycopg2.connect(database="word_count", user="postgres", password="munk21", host="localhost")

    cur = conn.cursor()

    cur.execute("SELECT SUM(count), word FROM word_count GROUP BY word ORDER BY word")
    rows = cur.fetchall()
    count = 0
    my_dict = dict()
    for row in rows:
        # print("Word: ", row[1])
        # print("Count: ", row[0])
        # print("\n")
        count += 1
        my_dict[row[1]] = row[0]
    # print(count)
    conn.close()
    db_pairs = my_dict
    return db_pairs


# print(len(list(db_pairs.keys())))
# print("--- %s seconds ---" % (time.process_time() - start_time))

# print(Counter(db_pairs).most_common(50))
