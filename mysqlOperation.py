import pymysql


class MySqlOperation:
    con = pymysql.connect(host='localhost', password='123456', port=3306, user='root',
                          db="attendance", charset='utf8')
    cur = con.cursor()

    def __init__(self):
        self.con = pymysql.connect(host='localhost', password='123456', port=3306, user='root',
                                   db="attendance", charset='utf8')
        self.cur = self.con.cursor()

    def create_table(self, table_name):
        create_word = "create table if not exists " \
                      "{}(id int AUTO_INCREMENT PRIMARY KEY NOT NULL, attendance varchar(20) NOT NULL);"\
                      .format(table_name)
        self.cur.execute(create_word)

    def add_student(self, table_name, stu_id, attendance):
        add_word = "insert into {}(id, attendance) value({}, {});".format(table_name, stu_id, attendance)
        self.cur.execute(add_word)
        self.con.commit()

    def free_link(self):
        self.cur.close()
        self.con.close()
