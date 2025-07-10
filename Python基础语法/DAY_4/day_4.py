def fun1():  # 切片操作
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list1_1 = list1[:]  # 从头到尾步长为1
    print(f"结果1：{list1_1}")
    turple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    turple1_1 = turple1[:]  # 从头到尾步长为1
    print(f"结果2：{turple1_1}")
    str1 = "1234567890"
    str1_1 = str1[::2]  # 从头到尾步长为2
    print(f"结果3：{str1_1}")
    str1_2 = str1[::-1]  # 从尾到头步长为1
    print(f"结果4：{str1_2}")
    list1_2 = list1[3:1:-1]  # 从下标3到下标1，步长为-1
    print(f"结果5：{list1_2}")
    turle1_2 = turple1[::-2]  # 从头到尾步长为-2
    print(f"结果6：{turle1_2}")


def fun2():  # 切片练习
    """
    取出”黑马程序员“
    :return:
    """
    str1 = "万过薪月，员序程马黑来，nohtyP学"
    mystr = str1.split("，")[1][::-1]
    print(mystr[1:])


def fun3():  # 集合练习
    """
    有如下列表对象：
    my_list =['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
    请:
    定义一个空集合
    通过for循环遍历列表
    在for循环中将列表的元素添加至集合
    最终得到元素去重后的集合对象，并打印输出
    :return:
    """
    my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
    set1 = set()
    for i in my_list:
        set1.add(i)
    print(f"去重后的集合为：{set1}")


def fun4():  # 字典练习
    """
    有如下员工信息，请使用字典完成数据的记录。
    并通过for循环，对所有级别为1级的员工，级别上升1级，薪水增加1000元
    部门
    工资
    级别
    科技部
    姓名
    王力鸿
    3000
    1
    周杰轮
    市场部
    5000
    2
    林俊节
    市场部
    7000
    3
    张学油
    科技部
    4000
    1
    刘德滑
    市场部
    6000
    2
    :return:
    """
    dict1 = {
        "王力宏": {
            '部门': '科技部', '工资': 3000, '级别': 1},
        "周杰伦": {
            '部门': '市场部', '工资': 5000, '级别': 2},
        "林俊节": {
            '部门': '市场部', '工资': 7000, '级别': 3},
        "张学油": {
            '部门': '科技部', '工资': 4000, '级别': 1},
        "刘德滑": {
            '部门': '市场部', '工资': 6000, '级别': 2}}
    for i in dict1:
        if dict1[i]["级别"] == 1:
            dict1[i]["级别"] += 1
            dict1[i]["工资"] += 1000
    print(f"升职加薪后{dict1}")


# fun1()
# fun2()
# fun3()
# fun4()


# 函数作为参数进行传递
# def test_func(fun_need):
#     result = fun_need(9,2)
#     print(result)
# def fun_add(a,b):
#     return a+b
#
# test_func(fun_add)
# test_func(lambda a,b:a*b)

# def fun_file_test():  # 文件操作小练习
#     with open("word.txt", "r", encoding="utf-8") as f:
#         count = 0
#         for line in f:
#             for word in line.split(" "):
#                 if word.replace("\n", "") == "itheima":
#                     count += 1
#     print(f"itheima出现了{count}次")
#
#
# fun_file_test()


def fun_file_bill():
    """
    文件操作综合案例
    :return:
    """
    with open("bill.txt","r",encoding="utf-8") as f1:
        with open("bill_1.txt","a",encoding="utf-8") as f2:
            for line in f1:
                if "测试" in line:
                    continue
                f2.write(line)


fun_file_bill()