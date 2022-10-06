import random
import heapq
from random import sample


class MyRandom:
    attendance_list = []
    score = []

    score_min = []
    index_min = []

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

    # 实现5-8位同学缺席了该学期80%的课
    def turn_bad_absence(self, score):
        score_min = heapq.nsmallest(20, score)  # 获取最小的20个值并排序
        index_min = map(score.index, score_min)  # 获取最小的20个值的下标
        # print(list(index_min))   map生成的对象要转化成为list才能输出
        absent_number = random.randint(5, 8)
        # print(absent_number)
        absent_list = sample(list(index_min), absent_number)
        # print(absent_list)
        for i in range(absent_number):
            absent_counts = random.sample(range(1, 21), 16)
            for j in range(16):
                list1 = list(self.attendance_list[absent_list[i]])
                list1[absent_counts[j]] = "1"
                self.attendance_list[absent_list[i]] = "".join(list1)
            # print(self.attendance_list[absent_list[i]])

    # 实现每次课程有0-3位同学由于各种原因缺席
    def turn_random_absence(self):
        for i in range(1, 21):
            absent_num = random.randint(0, 3)
            absent_cnt = random.sample(range(0, 89), absent_num)
            for j in range(absent_num):
                list2 = list(self.attendance_list[absent_cnt[j]])
                list2[i] = "1"
                self.attendance_list[absent_cnt[j]] = "".join(list2)

    # 获得随机生成后的出勤序列
    def get_random_attendance(self, score):
        self.turn_bad_absence(score)
        self.turn_random_absence()
        return self.attendance_list
