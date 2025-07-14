from Python基础语法.DAY_5.my_utils import str_util, file_util


def fun_try():
    """
    捕获异常练习
    :return:
    """
    try:
        f = open("word.txt", "r", encoding="utf-8")
    except (IOError, FileNotFoundError) as e:
        print("打开文件错误")
        print(e)

    try:
        print(name)  #捕获命名异常前置错误
    except (NameError, AttributeError) as e:
        print("出现了异常")
        print(e)


def fun_packagetest():
    file_util.print_file_info("word.txt")
    str_util.str_reverse("hello")

if __name__ == '__main__':
    fun_packagetest()