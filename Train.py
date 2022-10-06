import random


class Train:
    attendance_list = []
    plan_list = []
    score_list = []

    def __init__(self, attendance_list, score_list):
        self.attendance_list = attendance_list.copy()
        self.score_list = score_list.copy()

    def train(self):
        success_choose = []
        fail_choose = []
        for i in range(90):
            self.plan_list.append("\"")
            success_choose.append(0)
            fail_choose.append(0)

        chose_num = 8
        chose_end = 20
        for j in range(1, 21):
            score_copy = self.score_list.copy()
            sorted_score = sorted(enumerate(score_copy), key=lambda x: x[1])
            # idx为分数排名对应的下标，如idx[0] = 3代表分数最小的是3号学生
            idx = [i[0] for i in sorted_score]
            # 前chose_end差的学生中选出chose_num个抽点
            chosen = random.sample(range(0, chose_end), chose_num)
            sel_stu_id = []
            for k in range(chose_num):
                sel_stu_id.append(idx[chosen[k]])

            for i in range(90):
                if i in sel_stu_id:
                    self.plan_list[i] += "1"
                    if self.attendance_list[i][j] == "1":
                        self.score_list[i] -= 50
                        success_choose[i] += 1
                        if success_choose[i] >= 2:
                            success_choose[i] = 0
                            self.score_list[i] -= 1000
                    else:
                        self.score_list[i] += 20
                        fail_choose[i] += 1
                        if fail_choose[i] >= 2:
                            fail_choose[i] = 0
                            self.score_list[i] += 500
                            if chose_end > 8:
                                chose_end -= 1

                else:
                    self.plan_list[i] += "0"

        for i in range(90):
            self.plan_list[i] += "\""
        return self.plan_list
