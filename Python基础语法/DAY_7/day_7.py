import time
import threading
class stu:
    """
    学生信息类,用于练习基本的类属性和方法
    """

    def __init__(self, name=None, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address


class phone:
    """
    带有私有成员的手机类，用于加深私有成员的理解
    """

    def __init__(self, __is_5g_enable=False):
        self.__is_5g_enable = __is_5g_enable

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭,使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


class student_new(stu):
    """
    单继承练习
    """

# 多态练习
class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("汪汪汪")
class Cat(Animal):
    def make_sound(self):
        print("喵喵喵")


def make_sound(animal: Animal):
    animal.make_sound()



def __init__(self, name=None, age=None, address=None, face_id=None):
    self.name = name
    self.age = age
    self.address = address
    self.face_id = face_id

    def infomation_out(self):
        print(f"学生姓名{self.name}，学生年龄{self.age}，学生地址{self.address}，学生人脸识别ID{self.face_id}")


class student_new_2(stu):
    """
    多继承练习
    """


def fun_stu_info(stu_info_list: list):
    for i in range(0, 10):
        stu_info = stu(name=input("请输入学生姓名"), age=input("请输入学生年龄"), address=input("请输入学生地址"))
        stu_info_list.append(stu_info)
        print(
            f"第{i + 1}位学生信息录入完成，信息为：学生姓名{stu_info.name}，学生年龄{stu_info.age}，学生地址{stu_info.address}")


def fun_ATM_outer():
    """
    atm防外部篡改的闭包结构简单练习
    :return:
    """
    money = 100000
    def atm_menu():

        while True:
            print("-----------主菜单-----------")
            print("用户你好，欢迎来到ATM机，请输入操作")
            print("1.查询余额")
            print("2.取款")
            print("3.存款")
            print("4.退出")
            print("请输入你的选择：")
            choise = int(input())
            if choise == 1:
                atm_enquiry()
            elif choise == 2:
                atm_out()
            elif choise == 3:
                atm_in()
            elif choise == 4:
                print("感谢使用ATM机，再见")
                break
            else:
                print("请输入正确的选择!")

    def atm_enquiry():
        print(f"您的余额是{money}")

    def atm_in():
        nonlocal money
        money += int(input("请输入存款金额："))
        print(f"存款成功！您的余额为{money}")

    def atm_out():
        nonlocal money
        out_money = int(input("请输入取款金额："))
        if out_money > money:
            print("取款失败！您的余额不足")
        else:
            money -= out_money
            print(f"取款成功！您的余额为{money}")

    return atm_menu

def fun_outer(func):
    """
    简单的装饰器练习
    :param func:
    :return:
    """
    def inner():
        print("装饰器装饰前段")
        func()
        print("装饰器装饰后段")
    return inner

@fun_outer
def fun_tang():
    print("这里是被装饰的函数")



#  工厂模式练习
class Person:
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class Worker(Person):
    pass


class Factory:
    def get_person(self, type):
        if type == 's':
            return Student()
        elif type == 't':
            return Teacher()
        else:
            return Worker()


# 多线程编程练习
def fun_sleep_1(msg):
    while True:
        print(msg)
        time.sleep(2)

def fun_sleep_2(msg):
    while True:
        print(msg)
        time.sleep(1.5)


if __name__ == '__main__':
    print("day_7")
    # stu_list = []
    # fun_stu_info(stu_list)
    # iphone = phone()
    # iphone.call_by_5g()
    # stu_new = student_new(name = 1,age = 2,address = 3,face_id = 4)
    # stu_new.infomation_out()
    # var_1: int = 1
    # var_2: str = "你好"
    # var_3 = []  # type: list[int]
    # dog = Dog()
    # cat = Cat()
    # make_sound(dog)  # 输出：汪汪汪
    # make_sound(cat)  # 输出：喵喵喵
    # fun1 = fun_ATM_outer()
    # fun1()
    # fun_tang()
    # factory = Factory()
    # stu = factory.get_person('s')  # 创建一个学生对象
    # tea = factory.get_person('t')  # 创建一个教师对象
    # wor = factory.get_person('w')  # 创建一个工人对象
    # threading_1 = threading.Thread(target= fun_sleep_1,args=("这里是线程1",))
    # threading_2 = threading.Thread(target= fun_sleep_2,args=("这里是线程2",))
    # threading_1.start()
    # threading_2.start()
