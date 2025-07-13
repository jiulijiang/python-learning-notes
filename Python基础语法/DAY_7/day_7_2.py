import re

def fun_str():
    """
    正则表达式基础练习
    :return:
    """
    s = "1python itheima python itheima python itheima"
    result = re.match(r"python", s)
    print(result)  # 输出：<re.Match object; span=(0, 6), match='python'>
    # print(result.span())  # 输出： (0, 6)
    # print(result.group())  # 输出： python

if __name__ == '__main__':
    fun_str()
    r = '^[1-9]{1}[0-9]{4,10]$'