def print_file_info(file_path):
    """
    接收文件路径，打印文件内全部内容，
    如果文件不存在则捕获异常并输出信息，
    通过`finally`关闭文件对象
    :param file_path:
    :return:
    """
    f = None
    try:
        f = open(file_path, "r", encoding="utf-8")
        for line in f:
            print(line)
    except Exception as e:
        print("打开文件错误")
        print(e)
    finally:
        if f:
            f.close()

def append_to_file(file_path, data):
    """
    接收文件路径和数据，将数据追加到文件末尾
    :param file_path:
    :param data:
    :return:
    """
    with open(file_path, "a", encoding="UTF-8") as f:
        for i in data:
            f.write(i)


if __name__ == '__main__':
    print_file_info("word.txt")
    append_to_file("word.txt", ["hello", "world"])