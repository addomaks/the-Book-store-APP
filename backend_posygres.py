import psycopg2


def connect():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS iqc(naming TEXT, username TEXT, pgid REAL, "
                "featureid REAL, jiraid INTEGER, rating TEXT, pgupdate TEXT, manager TEXT)")
    conn.commit()
    conn.close()


def insert(naming, username, pgid, featureid, jiraid, rating, pgupdate, manager):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO iqc values(%s,%s,%s,%s,%s,%s,%s,%s)", (naming, username, pgid, featureid, jiraid, rating,
                                                                    pgupdate, manager))
    conn.commit()
    conn.close()


def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM iqc")
    conn.close()


def search(naming, username, pgid, featureid, jiraid, rating, pgupdate, manager):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROMM iqc WHERE naming=%s OR username=%s OR pgid=%s OR featureid=%s OR jiraid=%s OR rating=%s"
                "OR pgupdate=%s OR manager=%s", (naming, username, pgid, featureid, jiraid, rating, pgupdate, manager))
    rows=cur.fetchall()
    conn.close()
    return rows


connect()
#insert('John', 'Johnny', 46156, 113131, 224242, 'YES', 'NO', 'MEGHA')

#search(naming='John')
print(view())

