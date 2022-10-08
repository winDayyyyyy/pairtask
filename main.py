from myRandom import *
from Train import *
from Test import *
from mysqlOperation import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    table_num = 6
    e = []
    mysql_op = MySqlOperation()
    for j in range(1, table_num):
        table_name = "table{}".format(str(j))
        # 初次创建时保留此语句，想多次运行测试稳定性时需将此语句注释掉，否则重复创建表会报错
        # mysql_op.ini_table(table_name)

        rand_producer = MyRandom()
        score_list = rand_producer.get_normal_score()
        attendance_list = rand_producer.get_random_attendance()
        # 该循环是为了将生成的数据集写入数据库，只想测试e值时可以注释掉，可以大幅提升时间
        # for i in range(90):
        #     mysql_op.update_attendance(table_name, i + 1, attendance_list[i])
        #     mysql_op.update_score(table_name, i + 1, score_list[i])

        trainer = Train(attendance_list, score_list)
        plan_list = trainer.train()
        # 该循环是为了将生成的数据集写入数据库，只想测试e值时可以注释掉，可以大幅提升时间
        # for i in range(90):
        #     mysql_op.update_plan(table_name, i + 1, plan_list[i])

        T = Test()
        T.get_data(attendance_list, plan_list)
        e.append(T.count_e())

        del rand_producer
        del T
        score_list.clear()
        attendance_list.clear()
        plan_list.clear()

    mysql_op.free_link()
    x = []
    for i in range(1, table_num):
        x.append(i)

    plt.scatter(x, e)
    plt.show()
    print("e = {}".format(e))
    print("aver(e) = {}".format(np.mean(e)))
    print("var(e) = {}".format(np.var(e)))

    # # clear tables
    # mysql_op = MySqlOperation()
    # for j in range(1, table_num):
    #     table_name = "table{}".format(str(j))
    #     mysql_op.drop_table(table_name)
