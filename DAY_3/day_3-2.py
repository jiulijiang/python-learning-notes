def fun1():  # 列表的定义list()
    # 字面量
    list1 = [1, 2, 3, 4]
    # 定义变量
    list2 = ['a', 'b', 'c', 2, 3, 4]
    # 定义空列表
    list3 = []
    list4 = list()
    # 列表嵌套列表
    list5 = [1, 2, 3, [4, 5, 6], 7, 8, 9]  # 列表中的列表称为子列表
    print(list1, list2, list3, list4, list5)


def fun2():  # 列表的下标索引
    list1 = [1, 2, 3, [4, 5, 6], 7, 8, 9, 5]
    print(list1[2])  # 正序输出
    print(list1[-1])  # 倒序输出
    print(list1[3][2])  # 嵌套列表的下标索引


def fun3():  # 列表的常用方法
    list1 = [1, 2, 3, [4, 5, 6], 7, 8, 9, 5]
    index_1 = list1.index(5)  # 查找某元素在列表中的下标索引值
    print("5在列表中的下标为：", index_1)
    list1[0] = 100  # 修改列表中特定下标索引元素的值
    print(list1[0])
    list1.insert(0, 101)  # 在列表中指定下标索引位置插入元素
    print(list1)
    list1.append(102)  # 在列表末尾添加元素
    print("在列表末尾添加元素", list1)
    list2 = [103, 104, 105]
    list1.extend(list2)  # 在列表末尾添加另一个列表
    print("在列表末尾添加另一个列表", list1)
    list1.remove(102)  # 删除列表中指定元素第一个出现的位置
    print("删除列表中指定元素内容", list1)
    list1.pop()  # 删除列表中最后一个元素
    print("删除列表中最后一个元素", list1)
    list_pop = list1.pop(0)  # 删除列表中指定元素并返回该元素
    print("删除列表中指定下标索引的元素pop版本", list1, "删除的元素为", list_pop)
    del list1[0]  # 删除列表中指定下标索引的元素
    print("删除列表中指定下标索引的元素del版本", list1)
    list1 = [55, 95, 46, 34, 11]
    list1.sort()  # 对列表进行排序
    print("对列表进行排序", list1)
    list1.reverse()  # 对列表进行反序
    print("对列表进行反序", list1)
    count = len(list1)  # 获取列表长度
    print("获取列表长度", count)
    list1.clear()  # 清空列表
    print("清空列表", list1)


def fun4():  # 列表常用功能小案例
    list_1 = [21, 25, 21, 23, 22, 20]
    list_1.append(31)
    print(list_1)
    list_1.extend([29, 33, 30])
    print(list_1)
    print(list_1.pop(0))
    print(list_1.pop())
    print(list_1.index(31))


def list_while():  # 对列表的循环while
    list_1 = [21, 25, 21, 23, 22, 20]
    index = 0
    while index < len(list_1):
        print(f"while循环第{index + 1}个元素为{list_1[index]}")
        index += 1


def list_for():  # 对列表的循环for
    list_1 = [21, 25, 21, 23, 22, 20]
    for index in range(len(list_1)):
        print(f"for循环第{index + 1}个元素为{list_1[index]}")


def fun5():  # 列表循环的小案例
    """
    从1-10的列表中取出偶数，使用while循环和for循环分别实现并打印
    :return:
    """
    list_1 = range(1, 11)
    list_while_1 = []
    list_for_1 = []
    i = 0
    while i < len(list_1):
        if list_1[i] % 2 == 0:
            list_while_1.append(list_1[i])
        i += 1
    print(list_while_1)
    for i in range(len(list_1)):
        if list_1[i] % 2 == 0:
            list_for_1.append(list_1[i])
    print(list_for_1)


def fun6():  # 元组的基本使用与方法
    t1 = (1, 2, 3, 4, "a", "b", "c")
    index = t1.index("b")
    print("元组中b的下标为", index)
    num_count = t1.count(1)
    print("元组中1的个数为", num_count)
    print("元组元素个数为", len(t1))
    i = 0
    while i < len(t1):  # 元组while循环
        print(f"第{i + 1}个元素为{t1[i]}")
        i += 1
    for i in range(len(t1)):  # 元组for循环
        print(f"第{i + 1}个元素为{t1[i]}")


def fun7():  # 元组的小案例
    """
    定义一个元组，内容是：('周杰轮',11,['football','music'])，记录的是一个学生的信息（姓名、年龄、爱好）
    请通过元组的功能（方法），对其进行
    1．查询其年龄所在的下标位置
    2. 查询学生的姓名
    3.删除学生爱好中的football
    4. 增加爱好：coding到爱好list内
    :return:
    """
    t1 = ('周杰轮', 11, ['football', 'music'])
    print("年龄所在下标是", t1.index(11))
    print(f"学生姓名：{t1[0]}")
    t1[2].remove('football')  # 取出元组中list元素时，此时该元素为list，需要使用list的方法
    print(f"删除football后的爱好为：{t1[2]}")
    t1[2].append('coding')
    print(f"增加coding后的爱好为：{t1[2]}")


def fun8():  # 字符串的基本使用与方法
    str_1 = " 121Never put off what you can do today until tomorrow.122 "
    print(str_1[2])  # 正序索引查询
    print(str_1[-5])  # 逆序索引查询
    new_str_1 = str_1.replace(" ", "*")  # 替换字符串中的某字符串为另一个字符串
    print(new_str_1)
    new_list_1 = str_1.split(" ")  # 以空格为分隔符，将字符串分割成列表
    print(new_list_1)
    print("在字符串中查找Never的下标为%s" % str_1.index("Never"))  # 查找字符串中某字符串的下标
    new_str_2 = str_1.strip()
    print("去除字符串两端空格后的字符串为%s" % new_str_2)  # 去除字符串两端空格
    new_str_3 = new_str_2.strip("12")
    print("去除字符串两端12后的字符串为%s" % new_str_3)  # 去除字符串两端指定字符串
    print("字符串长度为%s" % len(str_1))  # 获取字符串长度
    print("字符串中e的个数为%s" % str_1.count("e"))  # 统计字符串中某字符串出现的次数


def fun9():  # 字符串的小案例
    """
    给定一个字符串："itheima itcast boxuegu"
    统计字符串内有多少个"it"字符
    将字符串内的空格，全部替换为字符："|"
    并按照"|"进行字符串分割，得到列表
    :return:
    """
    str_1 = "itheima itcast boxuegu"
    print(f"字符串中有{str_1.count('it')}个it")
    new_str_1 = str_1.replace(" ", "|")
    print(f"替换空格后的字符串为{new_str_1}")
    new_list_2 = new_str_1.split("|")
    print(f"分割后的列表为{new_list_2}")
# fun1()
# fun2()
# fun3()
# fun4()
# list_while()
# list_for()
# fun5()
# fun6()
# fun7()
# fun8()
fun9()