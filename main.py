from myRandom import *
from Train import *
from Test import *
from mysqlOperation import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    table_num = 500
    e = []
    for j in range(1, table_num):
        table_name = "table{}".format(str(j))
        op = MySqlOperation()

        # 初次创建时保留此语句，想多次运行测试稳定性时需将此语句注释掉
        # op.ini_table(table_name)

        rand_producer = MyRandom()
        score_list = rand_producer.get_normal_score()
        attendance_list = rand_producer.get_random_attendance(score_list.copy())
        for i in range(90):
            op.update_attendance(table_name, i + 1, attendance_list[i])
            op.update_score(table_name, i + 1, score_list[i])

        trainer = Train(attendance_list, score_list)
        plan_list = trainer.train()
        for i in range(90):
            op.update_plan(table_name, i + 1, plan_list[i])
        op.free_link()

        T = Test()
        T.get_data(table_name)
        e.append(T.count_e())

        del op
        del rand_producer
        del T
        score_list.clear()
        attendance_list.clear()
        plan_list.clear()

    x = []
    for i in range(1, table_num):
        x.append(i)

    plt.scatter(x, e)
    plt.show()
    print("e = {}".format(e))
    print("aver(e) = {}".format(np.mean(e)))
    print("var(e) = {}".format(np.var(e)))

    # # clear tables
    # op = MySqlOperation()
    # for j in range(1, table_num):
    #     table_name = "table{}".format(str(j))
    #     op.drop_table(table_name)
