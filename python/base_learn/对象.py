class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

    def say_hi(self):
        print(f"大家好，我是{self.name}，欢迎大家多多关照")

stu_1 = Student()
stu_1.name = "yinyueyu"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "河北省"
stu_1.age = 18

print(stu_1.say_hi())
