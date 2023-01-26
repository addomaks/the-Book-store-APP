import psycopg2


def connect():
    conn1=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur1=conn1.cursor()
    cur1.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn1.commit()
    conn1.close()


def insert(item, quantity, price):
    conn1=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur1=conn1.cursor()
    cur1.execute("INSERT INTO store values(%s,%s,%s)", (item, quantity, price))
    conn1.commit()
    conn1.close()


#insert('Apple232', 25, 150.5)


def delete(item):
    conn1=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur1=conn1.cursor()
    cur1.execute("DElETE FROM store WHERE item=%s", (item,))
    conn1.commit()
    conn1.close()


#delete("Apple232")


def update(quantity, price, item):
    conn1=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur1=conn1.cursor()
    cur1.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn1.commit()
    conn1.close()


#update(56, 87.5, 'Apple')


def view():
    conn1=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur1=conn1.cursor()
    cur1.execute("SELECT * FROM store")
    rows=cur1.fetchall()
    conn1.close()
    return rows


print(view())