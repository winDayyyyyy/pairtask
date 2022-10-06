from myRandom import *
from Train import *
from Test import *
from mysqlOperation import *

if __name__ == '__main__':
    op = MySqlOperation()
    op.create_table("table1")
    rand_producer = MyRandom()
    score_list = rand_producer.get_normal_score()
    attendance_list = rand_producer.get_random_attendance()
    for i in range(90):
        op.add_attendance("table1", i+1, attendance_list[i])
        op.update_score("table1", i+1, score_list[i])

    trainer = Train(attendance_list, score_list)
    plan_list = trainer.train()
    for i in range(90):
        op.update_plan("table1", i+1, plan_list[i])
    op.free_link()

    T = Test()
    T.get_data("table1")
    e = T.count_e()
    print(e)
