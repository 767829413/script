import mysql.connector
from mysql.connector import Error


class MySQLConnection:

    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(host=self.host,
                                                      port=self.port,
                                                      database=self.database,
                                                      user=self.user,
                                                      password=self.password)
            if self.connection.is_connected():
                print("成功连接到MySQL数据库")
                return True
        except Error as e:
            print(f"连接MySQL数据库时出错: {e}")
            return False

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL连接已关闭")

    def execute_query(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            print("未连接到数据库")
            return None

        cursor = self.connection.cursor(dictionary=True)
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"执行查询时出错: {e}")
            return None
        finally:
            cursor.close()
