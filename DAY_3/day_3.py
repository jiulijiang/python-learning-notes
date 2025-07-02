import random


def fun1():  # while()循环语句基础应用
    i = 0
    while i < 100:
        print("第%d次循环" % (i + 1))
        i += 1


def fun2():  # while()循环基础小案例
    num = random.randint(1, 100)
    i = True
    count = 0
    while i:
        guess = int(input("请输入猜想的数字："))
        if guess == num:
            print("恭喜你，猜对了！")
            i = False
        else:
            count += 1
            if guess > num:
                print("猜大了")
            else:
                print("猜小了")
    print("你总共猜了%d次" % count)


def fun3():  # while()循环嵌套使用小案例
    """表白一百天，每天赠送10朵花"""
    i = 0
    while i < 100:  # 外层循环控制天数
        j = 0
        while j < 10:  # 内层循环控制送花数
            print("第%d天，送给你%d朵花" % (i + 1, j + 1))
            j += 1
        print("今天是第%d天，小美我爱你" % (i + 1))
        i += 1


def fun4():  # while()循环嵌套使用小案例
    """while循环输出九九乘法表"""
    i = 0
    while i < 9:  # 外层循环控制第二个乘数并负责换行
        j = 0
        while j < i + 1:  # 内存循环控制第一个乘数并负责输出
            print(f"{j + 1}*{i + 1}={(j + 1) * (i + 1)}\t", end='')
            j += 1
        print()  # 空内容，起到换行作用
        i += 1


def fun5():  # for循环的基础语法
    name = "sum_july"
    for i in name:
        print(i)  # 将字符串中的数据逐个取出并打印


def fun6():  # for循环的小案例
    str_1 = "The best preparation for tomorrow is doing your best today."
    count_a = 0
    for i in str_1:
        if i == "a":
            count_a += 1
    print(f"{str_1}中的字母a的个数为{count_a}")


def fun7():  # range()语法基本使用
    for i in range(10):
        print(i)
    for i in range(1, 10):
        print(i)
    for i in range(1, 10, 2):
        print(i)
    for i in range(10, 1, -1):
        print(i)
    for i in range(10, 1, -2):
        print(i)


def fun8():  # range()语法小案例
    """利用range()语法求从1到100有多少偶数(不包含100)"""
    count = 0
    for i in range(1, 100):
        if (i % 2) == 0:
            count += 1
    print(f"从1到100有{count}个偶数")


def fun9():  # for循环嵌套使用小案例
    """结合range语法对fun3()中赠送玫瑰花案例进行优化"""
    i = 0
    for i in range(1, 101):  # 注意range()使用不包含num2
        for j in range(1, 11):
            print(f"第{i}天，送给你{j}朵玫瑰花")
        print(f"第{i}天，小美我爱你")
    print(f"第{i}天，表白成功")  # 想调用循环内临时变量，需要在循环外定义


def fun10():  # for()循环嵌套使用小案例
    """利用for循环优化fun4()中九九乘法表"""
    for i in range(1, 10):  # 通过外层循环控制行数
        for j in range(1, i + 1):  # 通过内层循环控制每行输出内容
            print(f"{j}*{i}={j * i}\t", end='')
        print()


def fun11():  # continue()和break()语句基础使用
    for i in range(1, 10):
        if i == 5:
            print("使用continue函数跳过5的打印")
            continue
        print(i)
    for i in range(1, 10):
        if i == 5:
            print("到达5时，使用break函数跳出循环")
            break
        print(i)


def fun12():  # 循环使用的综合案例
    """某公司，账户余额有1W元，给20名员工发工资。
    员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
    领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
    如果工资发完了，结束发工资。"""
    # 好黑心的公司
    account = 10000
    for employee in range(1, 21):
        if account < 1000:  # 首先判断账户余额是否足够发工资
            print("工资发完了，结束发工资")
            break
        else:
            socre = random.randint(1, 10)
            if socre < 5:  # 判断员工绩效分是否低于5
                print(f"员工{employee}的绩效分为{socre}，不发工资,下一位")
            else:
                account -= 1000
                print(f"员工{employee}的绩效分为{socre}，发工资，账户剩余{account}元")


def add(x, y):  # 简单函数实例
    results = x + y
    print(f"{x} + {y} = {results}")


def fun13():  # 全局变量的使用
    global num_1
    num_1 = 100


def atm_menu():  # 函数综合案例
    """
    简单的模拟ATM机
    :return:
    """
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
    global money
    money += int(input("请输入存款金额："))
    print(f"存款成功！您的余额为{money}")


def atm_out():
    global money
    out_money = int(input("请输入取款金额："))
    if out_money > money:
        print("取款失败！您的余额不足")
    else:
        money -= out_money
        print(f"取款成功！您的余额为{money}")




# main
# fun1()
# fun2()
# fun3()
# fun4()
# fun5()
# fun6()
# fun7()
# fun8()
# fun9()
# fun10()
# fun11()
# fun12()

# num_1 = 500
# print(num_1)
# fun13()
# print(num_1)

money = 100000
atm_menu()
