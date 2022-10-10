class Test:
    attendance = []
    plan = []
    request = 0
    success_hit = 0
    e = 0.0

    def get_data(self, attendance_list, plan_list):
        self.attendance = attendance_list
        self.plan = plan_list
        # 为加快运行速度测试更大数据量情况下的e值故用本地赋值，如果是真实场景从数据库获取信息时可使用以下语句：
        # 头部加上from mysqlOperation import *, 然后加入
        # mysql_op = MySqlOperation()
        # self.attendance = mysql_op.fetch_attendance()
        # self.plan = mysql_op.fetch_plan()

    def count_e(self):
        for i in range(90):
            for j in range(1, 21):
                if self.plan[i][j] == '1':
                    self.request += 1
                    if self.attendance[i][j] == '1':
                        self.success_hit += 1
        self.e = self.success_hit / self.request
        return self.e
