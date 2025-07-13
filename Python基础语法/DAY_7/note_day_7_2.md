### Python高阶技巧
#### 闭包
- 在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，可以把这个使用外部函数变量的内部函数称之为闭包
- 简单闭包演示：
    ```python
    def outer_func(a):
        def inner_func(b):
            return a + b
        return inner_func
    closure = outer_func(10)
    print(closure(5))  # 输出：15
    ```
- `nonlocal` 关键字
    - `nonlocal` 关键字用于声明一个变量为非局部变量。当在嵌套函数中修改非局部变量时，必须使用 `nonlocal` 关键字来声明该变量。
    - 作用，可用于想在函数外部修改函数内部的变量值
    - ATM程序示例：
    ```python
    def fun_ATM_outer():
    """
    atm防外部篡改的闭包结构简单练习
    :return:
    """
    money = 100000
    def atm_menu():

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
        nonlocal money
        money += int(input("请输入存款金额："))
        print(f"存款成功！您的余额为{money}")

    def atm_out():
        nonlocal money
        out_money = int(input("请输入取款金额："))
        if out_money > money:
            print("取款失败！您的余额不足")
        else:
            money -= out_money
            print(f"取款成功！您的余额为{money}")

    return atm_menu
    ```
- 闭包的优缺点：
    - 优点：
        - 无需定义全局变量即可实现通过函数，持续访问，修改某个变量的值
        - 闭包使用的变量位于外部函数内，难以被错误的调用修改
    - 缺点：
        - 由于内部函数持续引用外部函数的值，所以可能会导致这一部分空间不被释放，一直占用内存
#### 装饰器
- 装饰器也是一种闭包，主要功能就是在不破坏目标函数原有代码和功能的前提下，给目标函数添加新的功能
- 装饰器一般写法(闭包写法):
    ```python
    def outer(func):
        def inner():
            print("这是装饰器")
            func()
            print("这是装饰器")
        return inner
    def sleep():
        print("睡觉")
    func = outer(sleep)
    func()  # 输出：这是装饰器 \n 睡觉 \n 这是装饰器
    ```
- 装饰器语法(糖写法)：
    ```python
    def outer(func):
        def inner():
            print("这是装饰器")
            func()
            print("这是装饰器")
        return inner
    
    @outer
    def sleep():
        print("睡觉")

    sleep()  # 输出：这是装饰器 \n 睡觉 \n 这是装饰器
    ```
    - 装饰器的语法糖写法是通过在函数定义前加上 `@装饰器函数名` 来实现的，这样就不需要手动调用装饰器函数。
    - 糖写法的本质仍然是将原函数作为参数传递给装饰器函数，并返回一个新的函数，但是调用方式更为简洁，**不用手动赋值，直接写原函数名**即可。

#### 设计模式
- 设计模式是解决特定问题的通用解决方案，提供了一种可重用的代码结构和方法。
- 常见的设计模式包括：**单例模式，工厂模式**，观察者模式，策略模式等。
- **单例模式**：保证一个类只有一个实例，并提供一个全局访问点，这就是单例模式。
    - 适用场景：当需要确保一个类只有一个实例时，比如配置管理器，日志记录器等。
    - 基本写法：
        - 创建一个类，并在一个单独的文件中定义一个类，并使用一个静态变量来保存该类的唯一实例
        - 当需要使用的时候，在头部引用该实例，并进行想要的相应操作
    - 优点：
        - 确保全局只有一个实例，节省资源
        - 提供全局访问点，方便管理和使用
- **工厂模式**：提供一个创建对象的接口，但不暴露对象创建的具体实现。
    - 适用场景：当需要创建的对象类型较多，或者需要根据不同条件创建不同类型的对象时。
    - 基本写法：
        - 创建一个工厂类，并在该类中定义一个方法，根据传入的参数返回不同类型的对象
        - 使用工厂类来创建对象，而不是直接使用构造函数
    - 优点：
        - 大批量创建对象时，有统一的入口，易于代码维护
        - 当发生修改，仅修改工厂类的创建方法即可
        - 符合现实世界模式，即由工厂来制作产品(对象)
    - 示例:
        ```python
        class Person:
            pass
        class Student(Person):
            pass
        class Teacher(Person):
            pass
        class Worker(Person):
            pass
        class Factory:
            def get_person(self, type):
                if type == 's':
                    return Student()
                elif type == 't':
                    return Teacher()
                else:
                    return Worker()
        factory = Factory()
        stu = factory.get_person('s')  # 创建一个学生对象
        tea = factory.get_person('t')  # 创建一个教师对象
        wor = factory.get_person('w')  # 创建一个工人对象
        ```

#### 多线程编程
- **进程：**就是一个程序，运行在系统之上，称这个程序为一个运行进程，分配进程id方便系统管理
- **线程：**线程是归属于进程的，一个进程可以开启多个线程，执行不同的任务，是进程实际工作的最小单位
- 进程之间的内存是隔离的，线程之间共享内存，就像进程是一家公司，线程是公司里的员工
- **并行执行：**指同一时间做不同的工作，进程之间就是并行的，线程也可以并行执行，称为多线程并行执行
- `threading`模块：Python提供了`threading`模块来支持多线程编程
    - 基本语法:`线程名 = threading.Thread(target=方法名, args=(参数1, 参数2, ...))`
        - `target`: 线程要执行的函数(方法)
        - `args`: 线程执行函数的参数
    - 启动线程:`线程名.start()`
#### Socket网络编程
- 双端：
    - 服务端：负责监听客户端的请求，处理客户端的连接和数据交互
    - 客户端：负责向服务端发送请求，接收服务端的响应
- 服务端编程基本步骤：
    - 1.创建Socket对象
        ```python
        import socket
        socket_server = socket.socket()
        ```
    - 2.绑定IP地址和端口号
        ```python
        socket_server.bind(host, port)
        ```
    - 3.监听客户端的连接请求
        ```python
        socket_server.listen(backlog)   
        # backlog为int整数，表述允许连接的数量，超出会等待，可以不填，不填会自动设置一个合理值
        ```
    - 4.接收客户端的连接，获得连接对象
        ```python
        conn, addr = socket_server.accept()
        print(f"接收到客户端，连接来自{addr}")
        # accept方法是阻塞方法，如果没有连接会卡在当前这一行不向下执行
        # accept方法返回的是一个二元元组，可以使用上述形式，用两个变量接收二元元组的内容
        ```
    - 5.接收客户端发送的数据
        ```python
        data = conn.recv(bufsize).decode("utf-8")
        # bufsize为int整数，表示接收数据的最大字节数,一般设置为1024
        # 返回的是字节类型数据，可以使用decode方法转换为字符串
        print(data)
        ```
    - 6.发送消息给客户端
        ```python
        msg = input("请输入要发送给客户端的消息：").encode("utf-8")
        conn.send(msg)
        ```
    - 7.关闭连接
        ```python
        conn.close()
        socket_server.close()
        ```
    - 5和6步可以重写成无限循环，这样服务端就可以一直收发客户端的消息：
        ```python
        print(f"接收到客户端，连接来自{addr}")
        while True:
            data = conn.recv(bufsize).decode("utf-8")
            if not data:  # 如果没有数据，说明客户端关闭了连接
                print("客户端已断开连接")
                break
            print(data)
            msg = input("请输入要发送给客户端的消息：").encode("utf-8")
            if msg.lower() == 'exit':
                print("退出服务端")
                break
            conn.send(msg)
        conn.close()
        ```
- 客户端编程基本步骤：
    - 1.创建Socket对象
        ```python
        import socket
        socket_client = socket.socket()
        ```
    - 2.连接服务端
        ```python
        socket_client.connect((host, port))
        ```
    - 3.发送消息给服务端
        ```python
        msg = input("请输入要发送给服务端的消息：").encode("utf-8")
        socket_client.send(msg)
        ```
    - 4.接收服务端的响应
        ```python
        data = socket_client.recv(bufsize).decode("utf-8")
        print(data)
        ```
    - 5.关闭连接
        ```python
        socket_client.close()
        ```
    - 4和5步可以重写成无限循环，这样客户端就可以一直收发服务端的消息：
        ```python
        while True:
            msg = input("请输入要发送给服务端的消息：").encode("utf-8")
            if msg.lower() == 'exit':
                print("退出客户端")
                socket_client.close()
                break
            socket_client.send(msg)
            data = socket_client.recv(bufsize).decode("utf-8")
            print(data)
        ```


#### 正则表达式
- 正则表达式又称为规则表达式，是使用单个字符串来描述匹配某个句法规则的字符串，常备用于检索替换符合某个句法规则的文本
- 正则的三个基础方法：
    - `re.match`:从被匹配字符串开头进行匹配，匹配成功就返回匹配对象(包含匹配的信息)，失败就返回`None`(如果开头就不匹配就返回`None`)
        ```python
        import re
        s = "python itheima python itheima python itheima"
        result = re.match(r"python", s)
        print(result)  # 输出：<re.Match object; span=(0, 6), match='python'>
        print(result.span())  # 输出： (0, 6)
        print(result.group())  # 输出： python
        ```
    - `re.search`:搜索整个字符串，找出第一个匹配的字符串就停止，返回匹配的字符串，如果没有匹配的字符串，则返回`None`
        ```python
        s = "1python itheima python itheima python itheima"
        result = re.search(r"python", s)
        print(result)  # 输出：<re.Match object; span=(1, 7), match='python'>
    - `re.findall`:匹配整个字符串，返回所有匹配的字符串，如果没有匹配的字符串，则返回空列表
        ```python
        s = "1python itheima python itheima python itheima"
        result = re.findall(r"python", s)
        print(result)  # 输出：['python', 'python', 'python']
        ```
- 元字符匹配：
    - 单字符匹配
        - `.`:匹配任意字符，除了换行符，`\.`匹配本身
        - `[^]`:匹配任意字符，除了括号列举的字符
        - `[]`:匹配括号列举的字符
        - `\d`:匹配数字，等价于`[0-9]`
        - `\D`:匹配非数字，等价于`[^0-9]`
        - `\s`:匹配空白字符，等价于`[ \t\n\r\f\v]`
        - `\S`:匹配非空白字符，等价于`[^ \t\n\r\f\v]`
        - `\w`:匹配单词字符，等价于`[a-zA-Z0-9_]`
        - `\W`:匹配非单词字符，等价于`[^a-zA-Z0-9_]`
    - 数量匹配：
        - `*`:匹配0个或多个前面的字符
        - `+`:匹配1个或多个前面的字符
        - `?`:匹配0个或1个前面的字符
        - `{n}`:匹配n个前面的字符
        - `{n,}`:匹配n个或多个前面的字符
        - `{n,m}`:匹配n到m个前面的字符
    - 边界匹配：
        - `^`:匹配字符串的开头
        - `$`:匹配字符串的结尾
        - `\b`:匹配单词边界
        - `\B`:匹配非单词边界
    - 分组匹配：
        - `()`:匹配括号内的内容
        - `|`:匹配左右任意一个表达式
#### 递归
- 概念：即函数(方法)直接调用自身的特殊编程写法
    ```python
    def fun():
        if ...:
            fun()
        return ...
    ```
- 使用场景：
    - 解决一些复杂问题时，可以使用递归来简化代码
    - 例如：寻找文件，树形结构的遍历、汉诺塔问题、斐波那契数列等
- 注意事项：
    - 递归调用的终止条件必须明确，否则容易变成无限递归
    - 确保返回值的传递，确保从最内层，一层层返回到最外层

---
基础Python到此结束  
**完结撒花**