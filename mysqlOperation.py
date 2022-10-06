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
        create_word = "create table if not exists {}(id int NOT NULL, " \
                      "attendance varchar(21) NOT NULL, plan varchar(21), score float);".format(table_name)
        self.cur.execute(create_word)

    def add_attendance(self, table_name, stu_id, attendance):
        add_word = "insert into {}(id, attendance) value({}, {});".format(table_name, stu_id, attendance)
        self.cur.execute(add_word)
        self.con.commit()

    def update_plan(self, table_name, stu_id, plan):
        add_word = "update {} set plan = {} where id = {};".format(table_name, plan, stu_id)
        self.cur.execute(add_word)
        self.con.commit()

    def update_score(self, table_name, stu_id, score):
        add_word = "update {} set score = {} where id = {};".format(table_name, score, stu_id)
        self.cur.execute(add_word)
        self.con.commit()

    def fetch_attendance(self, table_name):
        attendance = []
        sel_att_word = "select attendance from {};".format(table_name)
        self.cur.execute(sel_att_word)
        result = self.cur.fetchall()
        for i in result:
            attendance.append(i[0])
        self.con.commit()
        return attendance

    def fetch_plan(self, table_name):
        plan = []
        sel_plan_word = "select plan from {};".format(table_name)
        self.cur.execute(sel_plan_word)
        result = self.cur.fetchall()
        for i in result:
            plan.append(i[0])
        self.con.commit()
        return plan

    def drop_table(self, table_name):
        drop_word = "drop table {};".format(table_name)
        self.cur.execute(drop_word)

    def free_link(self):
        self.cur.close()
        self.con.close()
