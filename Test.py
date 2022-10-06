from mysqlOperation import *


class Test:
    test_op = MySqlOperation()
    attendance = []
    plan = []
    request = 0
    success_hit = 0
    e = 0.0

    def get_data(self, table_name):
        self.attendance = self.test_op.fetch_attendance(table_name)
        self.plan = self.test_op.fetch_plan(table_name)

    def count_e(self):
        for i in range(90):
            for j in range(20):
                if self.plan[i][j] == '1':
                    self.request += 1
                    if self.attendance[i][j] == '1':
                        self.success_hit += 1
        self.e = self.success_hit / self.request
        return self.e
