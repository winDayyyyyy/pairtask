from mysqlOperation import *
from myRandom import *

if __name__ == '__main__':
    op = MySqlOperation()
    op.create_table("table1")
    rand_attendance = MyRandom()
    attendance_list = rand_attendance.get_list()

    for i in range(1, 91):
        op.add_student("table1", i, attendance_list[i])
    op.free_link()
