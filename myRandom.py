import random


class MyRandom:
    attendance_list = []
    score = []


    # 默认一开始所有学生都满勤，0代表没缺课
    def __init__(self):
        for i in range(90):
            self.attendance_list.append("\"00000000000000000000\"")

    # 产生正态分布的初始学生得分值，现实中可以综合如绩点等多种因素生成该得分值
    def get_normal_score(self):
        for _ in range(90):
            val = random.normalvariate(50, 16.67)
            if val >= 100:
                val = 100
            elif val <= 0:
                val = 0
            self.score.append(val)
        return self.score

    # # 实现5-8位同学缺席了该学期80%的课
    # def turn_bad_absence(self):
    #
    #
    # # 实现每次课程有0-3位同学由于各种原因缺席
    # def turn_random_absence(self):


    # 获得随机生成后的出勤序列
    def get_random_attendance(self):
        # self.turn_bad_absence()
        # self.turn_random_absence()
        return self.attendance_list
