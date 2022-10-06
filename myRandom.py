import random


class MyRandom:
    attendance_list = ["\"00000000000000000000\""]
    useless = 1

    # 默认一开始所有学生都满勤，0代表没缺课
    def __init__(self):
        for i in range(0, 90):
            self.attendance_list.append("\"00000000000000000000\"")

    # 实现5-8位同学缺席了该学期80%的课
    def turn_bad_absence(self):
        self.useless += 1

    # 实现每次课程有0-3位同学由于各种原因缺席
    def turn_random_absence(self):
        self.useless += 1

    # 获得随机生成后的出勤序列
    def get_list(self):
        self.turn_bad_absence()
        self.turn_random_absence()
        return self.attendance_list
