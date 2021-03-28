class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    #     注册
    def enroll(self, stu_obj):
        print("为学员%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, tea_obj):
        print("招聘%s作为老师" % tea_obj.name)
        self.teachers.append(tea_obj)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
            ---------info Teacher:%s----------
            name:%s
            age:%s
            sex:%s
            salary:%s
            course:%s
        ''' % (self.name, self.name, self.age, self.sexm, self.salary, self.course))

    def teach(self):
        print('%s 教%s' % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
            ---------info Student:%s----------
            name:%s
            age:%s
            sex:%s
            stu_id:%s
            grade:%s
        ''' % (self.name, self.name, self.age, self.sexm, self.stu_id, self.grade))

    def pay_tuition(self, amount):
        print('%s交了%s元学费' % (self.name, amount))


school = School("上海高中", "徐汇")
t1 = Teacher("语文老师", 56, '女', 20000, '语文')
t2 = Teacher("数学老师", 36, '男', 20000, '数学')

s1 = Student('张三', '22', '男', '10000', 'Python')
s2 = Student('张四', '23', '女', '10001', '测试')
s3 = Student('张五', '24', '男', '10002', 'DevOps')

school.hire(t1)
school.hire(t2)
school.enroll(s1)
school.enroll(s2)
school.enroll(s3)

school.teachers[0].teach()
