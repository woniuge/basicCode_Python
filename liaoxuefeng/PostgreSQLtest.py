
'''
import psycopg2

#1. 数据库连接参数
conn = psycopg2.connect(database="postgres",user="postgres",password="root",host="127.0.0.1",port="5432")
cur = conn.cursor()

cur.execute("CREATE TABLE test(id serial PRIMARY KEY,num integer,data varchar);")
#2. 插入一项
cur.execute("INSERT INTO test(num,data)VALUES(%s,%s)",(1,'aaa'))
cur.execute("INSERT INTO test(num,data)VALUES(%s,%s)",(2,'bbb'))
cur.execute("INSERT INTO test(num,data)VALUES(%s,%s)",(3,'ccc'))

cur.execute("SELECT * FROM test;")
rows=cur.fetchall() #表中的所有行
print(rows)
for i in rows:
    print(i)
conn.commit()
cur.close()
conn.close()
'''

#简单地调用pg中的存储过程
import psycopg2
conn =psycopg2.connect(database="postgres",user="postgres",password="root",host="127.0.0.1",port="5432")
cur = conn.cursor()
cur.callproc('totalRecords')
result=cur.fetchall()
print(result)
conn.commit()
cur.close()
conn.close()
