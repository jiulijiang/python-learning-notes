def str_reverse(str1):
    """
    接受传入字符串，将传入字符串反转并返回
    :param str1:
    :return:
    """
    return str1[::-1]
def substr(str1, x, y):
    """
    按照下标x,y对字符进行切片
    :param str1:
    :param x: 起始下标
    :param y: 结束下标
    :return:
    """
    return  str1[x:y]

if __name__ == '__main__':
    print(str_reverse("hello"))
    print(substr("hello", 1, 3))