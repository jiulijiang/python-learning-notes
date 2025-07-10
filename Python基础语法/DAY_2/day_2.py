import random

def fun1(str1):  # 快速格式化字符串
    print(f"这是快速输出的字符串：{str1}")


def fun2():  # 表达式的格式化
    a = 100
    b = 20
    print("a + b = %d" % (a + b))


def fun3():  # 股价计算小程序
    name = input("请输入公司名称")
    stock_price = float(input("请输入股价"))
    stock_code = input("请输入股票代码")  # 数字类型不可以以0开头
    stock_price_daily_growth_factor = float(input("请输入股价日增长因子"))
    growth_days = int(input("请输入股价增长天数"))
    print(f"公司:{name},股票代码:{stock_code},当前股价：{stock_price}")
    print("每日增长系数%0.1f,经过%d天的增长后，股价达到了：%0.2f" % (
        stock_price_daily_growth_factor, growth_days, stock_price * (stock_price_daily_growth_factor ** growth_days)))


def fun4():  # input输入
    name = input("请输入你的姓名")
    age = input("请输入你的年龄")
    print("你的姓名是：%s，你的年龄是：%s" % (name, age))


def fun5():  # 布尔类型
    bool_1 = True
    bool_2 = False
    print(f"bool_1 = {bool_1},bool_2 = {bool_2},类型是：{type(bool_1)}")
    a, b = 10, 100
    bool_1 = a < b
    print(f"a<b的结果是：{bool_1}")
    # 演示>=,<=,!=,==,>,<
    num_1 = 10
    num_2 = 100
    print(f"num_1 = {num_1},num_2 = {num_2}")
    print(f"num_1 >= num_2 的结果是：{num_1 >= num_2}")
    print(f"num_1 <= num_2 的结果是：{num_1 <= num_2}")
    print(f"num_1 != num_2 的结果是：{num_1 != num_2}")
    print(f"num_1 == num_2 的结果是：{num_1 == num_2}")


def fun6():  # if()语句的基本格式应用
    age = int(input("请输入你的年龄"))
    if age >= 18:
        print("你已经成年了")
        print("即将步入大学生活")
    print("时间过得真快")


def fun7():  # if语句小案例
    print("欢迎来到游乐园，儿童免费，成人收费10元")
    age = int(input("请输入你的年龄："))
    if age >= 18:
        print("你已经成年了，请购买门票")
    print("祝你游玩愉快")


def fun8():  # if else组合判断小案例
    print("欢迎来到游乐园，身高1.2米以下免费，1.2米以上收费10元")
    height = float(input("请输入身高（cm）："))
    if height < 120:
        print("您的身高未超出120cm，免费")
    else:
        print("您的身高超过120cm，游玩需要10元")
    print("祝你游玩愉快")


def fun9():  # if_elif_else组合判断小案例
    num_1 = 88
    if int(input("请输入第一次猜想数字：")) == num_1:
        print("一次就猜对了，真厉害！")
    elif int(input("不对，再猜一次：")) == num_1:
        print("恭喜你！猜对了！")
    elif int(input("不对，再猜最后一次：")) == num_1:
        print("恭喜你！猜对了！")
    else:
        print("sorry，你全猜错了，答案是%d" % num_1)

def fun10(): #判断语句嵌套使用小案例
    answer = random.randint(1,10)
    answer_input = int(input("请输入第一次猜想的数字："))
    if answer_input == answer:
        print("恭喜你，一次猜对了！")
    else:
        if answer_input > answer:
            print("猜大了")
        else:
            print("猜小了")
        answer_input = int(input("请输入第二次猜想的数字："))
        if answer_input == answer:
            print("恭喜你，两次猜对了！")
        else:
            if answer_input > answer:
                print("猜大了")
            else:
                print("猜小了")
            answer_input = int(input("请输入第三次猜想的数字："))
            if answer_input == answer:
                print("恭喜你，最后一次猜对了！")
            else:
                print("三次机会用完了，答案是%d" % answer)


# main
fun1("hello world")
fun2()
# fun3()
# fun4()
# fun5()
# fun6()
# fun7()
# fun8()
# fun9()
fun10()