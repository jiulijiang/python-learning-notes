#变量
def bianliang():
    money = 100
    print("money = ",money) #通过print()函数输出变量
    money = money + 100
    print("买了100块钱的东西，现在money = ",money)

def check_type():
    a = 100
    b = 100.0
    c = "100"
    print("a = ",a,"type = ",type(a))
    print("b = ",b,"type = ",type(b))
    print("c = ",c,"type = ",type(c))

def type_change():
    a = 100
    b = 100.0
    c = "100"
    print("a = ",a,"type = ",type(a))
    print("b = ",b,"type = ",type(b))
    print("c = ",c,"type = ",type(c))
    a = int(a)
    b = int(b)
    c = int(c)
    print("a = ",a,"type = ",type(a))
    print("b = ",b,"type = ",type(b))

def str_link():
    name = "九离"
    age = "18"
    print(name + age)

def str_geshi():
    num1 = 11
    num2 = 11.12345
    print("数字1宽度限制5,结果是：%5d" % num1)
    print("数字1宽度限制1，结果是：%1d" % num1)
    print("数字2宽度限制7，精度限制2，结果是：%7.4f" % num2)
    print("数字2宽度不限制，精度限制2，结果是：%.5f" % num2)

# main
bianliang()
check_type()
type_change()
str_link()
str_geshi()