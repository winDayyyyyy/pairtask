import random


class Train:
    attendance_list = []
    plan_list = []
    score_list = []
    next_choose_list = []
    chose_num = 8
    chose_end = 20

    def __init__(self, attendance_list, score_list):
        self.attendance_list = attendance_list
        self.score_list = score_list
        # 为加快运行速度测试更大数据量情况下的e值故用本地赋值，如果是真实场景从数据库获取信息时可使用以下语句：
        # 头部加上from mysqlOperation import *, 然后加入
        # mysql_op = MySqlOperation()
        # self.attendance_list = mysql_op.fetch_attendance()
        # self.score_list = mysql_op.fetch_attendance()

    def train(self):
        success_choose = []
        fail_choose = []
        for i in range(90):
            self.plan_list.append("\"")
            success_choose.append(0)
            fail_choose.append(0)

        for j in range(1, 21):
            sel_stu_id = self.get_sel_stu_id()
            for i in range(90):
                if i in sel_stu_id:
                    self.plan_list[i] += "1"
                    # attendance_list中，1代表缺勤
                    if self.attendance_list[i][j] == "1":
                        self.score_list[i] -= 100
                        self.next_choose_list.append(i);
                        success_choose[i] += 1
                        if success_choose[i] >= 2:
                            self.score_list[i] -= 1000
                    else:
                        # self.score_list[i] += 10
                        fail_choose[i] += 1
                        if fail_choose[i] >= 2:
                            self.score_list[i] += 510
                            if 8 >= self.chose_end >= 6 and fail_choose[i] - success_choose[i] >= 0:
                                self.chose_end -= 1
                                self.chose_num -= 1
                            if self.chose_end > 8:
                                self.chose_end -= 1
                else:
                    self.plan_list[i] += "0"

        for i in range(90):
            self.plan_list[i] += "\""
        return self.plan_list

    def get_sel_stu_id(self):
        score_copy = self.score_list.copy()
        sorted_score = sorted(enumerate(score_copy), key=lambda x: x[1])
        # idx为分数排名对应的下标，如idx[0] = 3代表分数最小的是3号学生
        idx = [i[0] for i in sorted_score]
        # 前chose_end差的学生中选出chose_num个抽点
        chosen = random.sample(range(0, self.chose_end), self.chose_num)
        sel_stu_id = []
        for k in range(self.chose_num):
            sel_stu_id.append(idx[chosen[k]])
        sel_stu_id = list(set(sel_stu_id + self.next_choose_list))
        self.next_choose_list.clear()
        return sel_stu_id
