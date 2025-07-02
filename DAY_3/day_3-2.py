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
    list1 =  [1, 2, 3, [4, 5, 6], 7, 8, 9, 5]
    print(list1[3])
    print(list1[-1])

fun1()
