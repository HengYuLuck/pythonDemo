from pymysql import Connection

# 建立数据库连接
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password=""
)

# 创建游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("world")

# 执行SELECT查询
cursor.execute("SELECT * FROM student")
results = cursor.fetchall()
for r in results:
    print(r)

# 关闭数据库连接
conn.close()
