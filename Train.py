import random


class Train:
    attendance_list = []
    plan_list = []
    score_list = []

    def __init__(self, attendance_list, score_list):
        self.attendance_list = attendance_list.copy()
        self.score_list = score_list.copy()

    def train(self):
        for i in range(90):
            self.plan_list.append("\"")

        for j in range(1, 21):
            score_copy = self.score_list.copy()
            sorted_score = sorted(enumerate(score_copy), key=lambda x: x[1])
            # idx为分数排名对应的下标，如idx[0] = 3代表分数最小的是3号学生
            idx = [i[0] for i in sorted_score]
            # 前20差的学生中选出15个抽点
            chosen = random.sample(range(0, 20), 15)
            sel_stu_id = []
            for k in range(15):
                sel_stu_id.append(idx[chosen[k]])
            for i in range(90):
                if i in sel_stu_id:
                    self.plan_list[i] += "1"
                    if self.attendance_list[i][j] == "1":
                        self.score_list[i] -= 5
                    else:
                        self.score_list[i] += 3
                else:
                    self.plan_list[i] += "0"

        for i in range(90):
            self.plan_list[i] += "\""
        return self.plan_list
