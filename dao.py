import sqlite3

class DBTool(object):
    def __init__(self):
        """
        初始化函数，创建数据库连接
        """
        self.conn = sqlite3.connect("test.db")
        self.c = self.conn.cursor()
    def createTable(self,sql):
        try:
            self.c.execute(sql)
            print("创建表成功")
        except Exception as e:
            print("新建表报错：",e)

    def executeUpdate(self,sql,ob):
        """
        数据库插入，修改函数
        :param sql: 传入的sql语句
        :param ob: 传入数据
        :return: 返回操作数据库状态
        """
        try:
            self.c.executemany(sql,ob)
            i = self.conn.total_changes
        except Exception as e:
            print("错误类型： ",e)
        finally:
            self.conn.commit()
        if i >0:
            return True
        else:
            return False

    def excuteDelete(self,sql,ob):
        """
        操作数据库数据删除的函数
        :param sql: 传入的sql语句
        :param ob: 传入数据
        :return: 返回操作数据库的装填
        """
        try:
            self.c.executemany(sql,ob)
            i = self.conn.total_changes
        except Exception as e:
            print("错误类型：",e)
        finally:
            self.conn.commit()
        if i>0:
            return True
        else:
            return False

    def executeQuery(self,sql,ob):
        """
        数据库数据查询
        :param sql:
        :param ob:
        :return:
        """
        data = self.c.executemany(sql,ob)
        return data

    def close(self):
        """
        关闭数据库相关连接的函数
        :return:
        """
        self.c.close()
        self.conn.close()

if __name__ == "__main__":
    db = DBTool()
    # db.createTable('create table stu(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(30) NOT NULL, age INTEGER)')
    # name = input("输入姓名")
    # age = input("输入年龄")
    # ob = [(name,age)]
    # sql = 'insert into stu (name,age) values (?,?)'
    # T = db.executeUpdate(sql,ob)
    # if T:
    #     print("插入成功")
    # else:
    #     print("插入失败")
    sql_for_query = 'select * from stu where name=?'
    try:
        data = db.executeQuery(sql_for_query,'heyanshen')
        if data:
            for s in data:
                print(s[0],s[1])
        else:
            print("失败")
    except Except as e:
        print(e)
