import pymysql.cursors
from util.read_ini import ReadIni

class DB:
    def __init__(self, lib):
        read_init = ReadIni()
        try:
            self.conn =pymysql.connect(host=read_init.get_value(lib, 'host'),
                            port=int(read_init.get_value(lib, 'port')),
                            user=read_init.get_value(lib, 'user'),
                            password=read_init.get_value(lib, 'password'),
                            db=read_init.get_value(lib, 'db_name'),
                            )
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    #获取单条数据
    def select_one(self,sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except:
            print('Error: unable to fetch data')
    #获取所有数据
    def select_all(self,sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except:
            print('Error: unable to fetch data')

    #更新数据
    def update(self,sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()


    def close(self):
        self.conn.close()


if __name__ == '__main__':
    # a = get_value('core_mysqlconf', 'user')
    # print(a)
    db = DB('cforder')
    order_no ='YXHZSO19061310000005'
    sql = "UPDATE t_yx_order_settlement SET state=3, deposit_state=1 WHERE order_no=" + "'" + order_no + "'"
    print(sql)
    db.update(sql)
    db.close()
    #data = db.select_one(sql)
    #print(data)
    # for i in data:
    #     a = i
    # print(a)