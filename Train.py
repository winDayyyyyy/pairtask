class Train:
    attendance_list = []
    plan_list = []

    def __init__(self, attendance_list):
        self.attendance_list = attendance_list.copy()

    def train(self):
        for i in range(0, 90):
            s = self.attendance_list[i]
            for j in range(1, 21):
                if s[j] == '0':
                    s1 = "\""
                    s2 = "01000000000000000000"
                    s3 = s1+s2+"\""
                    self.plan_list.append(s3)
                    break
        return self.plan_list
