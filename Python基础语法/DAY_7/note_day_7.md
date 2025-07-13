## day_7
### 面向对象
- **初识对象：** 对象是对现实世界中事物的抽象，具有属性和方法。
    - **类的定义：** 类是对象的蓝图，通过类可以创建多个对象。
    - **实例化：** 通过类创建对象的过程称为实例化。
    - **属性与方法：** 对象的属性是描述其特征的数据，方法是对象可以执行的操作。
    - 就像是现实世界的一张表格，设计表格是"创建类”，打印表格是"实例化类"，也叫“创建对象”，填写表格是“对象属性赋值”
- #### **类的定义和使用：** 
    - 类的定义语法：
        ```python
        class ClassName:
            name = ""  # 属性示例

            def run(self):
                print("对象正在运行")
        ```
        - `class` 关键字用于定义类，`ClassName` 是类的名称，通常以大写字母开头。
        - 类的属性是类的变量，用于存储类的数据。（成员变量）
        - 类的行为是类的方法，用于定义类可以执行的操作。(成员方法)
    - 类的方法：
        - 类的方法是定义在类内部的函数，用于定义类的行为。
        - 方法的第一个参数通常是 `self`，表示类的实例本身。
        - 方法可以访问类的属性和其他方法。
        - 定义语法：
        ```python  
        def method_name(self, 其他参数):
            方法体
        ```
- #### **类和对象的关系：**
    - 类是对象的模板或蓝图，对象是类的实例。
    - 一个类可以创建多个对象，每个对象都有自己的属性和方法。
    - 类定义了对象的行为和状态，而对象是类的具体实现。
    ```python
    class Clock:
        def __init__(self, id=None, price=None):
            # __init__ 是构造方法，用于初始化对象属性
            self.id = id  # 对象属性: 对象id
            self.price = price  # 对象属性: 对象价格

        def ring(self):
            print("叮铃铃...")

    clock1 = Clock(id=1, price=100)  # 实例化对象并初始化属性
    clock1.ring()
    ```
    - ``__init__`` 方法是类的构造方法，用于初始化对象的属性,
      当创建对象时会自动调用。
    - ``__init__`` 方法的第一个参数必须是 `self`，用于接收实例本身，其他参数用于初始化属性，方法没有返回值（返回None）。
- #### **常用内置方法：**
    - `__str__` 方法：返回对象的字符串表示，通常用于打印对象。
        ```python
        class student:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            def __str__(self):
                return "姓名：%s，年龄：%s" % (self.name, self.age)
        stu1 = student("张三", 18)
        print(stu1)  # 结果为："姓名：张三，年龄：18"，如果没有设置__str__方法，则打印对象时，默认打印对象的内存地址
    - `__lt__` 方法：用于比较两个对象的大小，通常用于排序。(只用于小于,大于)
        ```python
        class student:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            def __lt__(self, other):
                return self.age < other.age
        stu1 = student("张三", 18)
        stu2 = student("李四", 20)
        print(stu1 < stu2)  # 结果为：True,如果不设置__lt__方法，会直接报错
        ```
    - `__le__` 方法：用于比较两个对象大小，通常用于排序。(只用于小于等于,大于等于)
        ```python
        class student:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            def __le__(self, other):
                return self.age <= other.age
        stu1 = student("张三", 18)
        stu2 = student("李四", 20)
        print(stu1 <= stu2)  # 结果为：True,如果不设置__le__方法，会直接报错
        ```
    - `__eq__`方法：用于比较两个对象是否相等，通常用于查找。(只用于等于)
        ```python
        class student:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            def __eq__(self, other):
                return self.age == other.age
        stu1 = student("张三", 18)
        stu2 = student("李四", 20)
        print(stu1 == stu2)  # 结果为：False,如果不设置__eq__方法，会直接报错
        ```
- #### **封装：** 封装是把数据（属性）和操作（方法）封装在一起，隐藏内部实现细节，只提供对外的接口。
    - 私有成员：私有成员是以双下划线开头的属性和方法，外部无法直接访问，只能通过类内部的方法访问,现实事物有部分属性和行为是不对使用者开放的，同样在类中描述属性和方法的时候也需要达到这个要求，就需要定义私有成员了
        ```python
        class phone:
            __currrent_voltage = None

            def__keep_single_core(self):
                print("保持单核运行")
        ```
        - 私有成员无法被类对象使用，但是可以被类内部方法使用  
        ```python
            def call_by_5g(self):
                if self.__currrent_voltage >= 5:  
                    print("5G通话")
                else:  
                    self.__keep_single_core()
                    print("电量不充足，使用单核运行")
        ```
- #### **继承：** 继承是类与类之间的关系，子类继承了父类的属性和方法，并添加了新的属性和方法。
    - 为什么要继承？
        - 代码复用：子类可以直接使用父类的属性和方法，减少代码重复。
        - 扩展功能：子类可以在父类的基础上添加新的功能或修改现有功能。
    - 继承的语法：(单继承)
        ```python
        class 类名(父类名):
            类内容体
        ```
    - 多继承的语法：
        ```python
        class 类名(父类1, 父类2, ...):
            类内容体
        ```
        - `pass` 关键字：当类没有任何内容或者继承父类后不想补充新内容，可以使用 `pass` 关键字表示空类。
            ```python
            class 类名(父类1, 父类2, ...):
                pass
            ```
        - 多继承时，当不同父类有同名属性时，会按照从左到右的顺序查找属性，找到第一个匹配的属性。
            ```python
            class A:
                def method(self):
                    print("A method")

            class B:
                def method(self):
                    print("B method")

            class C(A, B):
                pass

            c = C()
            c.method()  # 输出：A method
            ```
- #### **复写：** 复写是子类重新定义父类的方法，子类可以修改或扩展父类的方法。
    - 复写方法：直接在子类中定义与父类同名的属性或者方法，子类的方法会覆盖父类的方法。
    - 调用父类同名成员方法：
        - 1.调用父类成员：`父类名.成员变量/成员方法(self)`
        - 2.调用父类同名方法：`super().成员变量/成员方法名()`
- #### **类型注解:** 方便静态类型检查工具，IDE等第三方工具，在设计代码交互的地方提供数据类型的注解
    - 类型注解基础语法：`变量名: 数据类型 = 值`
    - 示例：
        ```python
        age: int = 18
        name: str = "张三"
        is_student: bool = True
        ```
        - 如上代码就可以告诉静态类型检查工具，变量`age`是整数类型，变量`name`是字符串类型，变量`is_student`是布尔类型。
    - 容器类型注解：
        - 基础语法：`变量名: 容器类型 = 值`
        - 详解类型：`变量名: 容器类型[元素类型] = 值`
            - 字典：`变量名: dict[键类型, 值类型] = 值`
    - 在注释中进行类型注解
        - 语法: `变量名 = 值  # type: 数据类型`  
        - 数据类型对于数据容器注解同样适用
    - 类型注解一般用于无法直接判断数据类型时，比如：
        ```python
        var_1 = random.randint(1, 100)  # type: int
        var_2 = json.loads(data)  # type: dict 
        ```
    - 类型注解是提示性的不是强制性的，它是个备注，即使标错了也不会报错
    - 函数(方法)的类型注解和基础类型注解一致，比如：
        ```python
        def func(a: int, b: int) -> int:
            return a + b
        ```
        - 期中` -> int`是对返回值的类型进行注解，表示该函数返回一个整数。
        - 同样的，函数中的类型注解也是提示性的而不是强制性的，即使类型错误也不会报错。
    - `Union`类型注解：表示一个变量可以是多个类型中的一个，比如：
        ```python
        from typing import Union
        my_list: list[Union[int, str]] = [1, "hello"]
        ```
        - `list[Union[int, str]]`表示my_list是一个列表，列表中的元素可以是整数或字符串。
    - `Union`基础语法：
        ```python
        Union[Type1, Type2, ...]
        ```
- #### **多态:** 多态指的是多种状态，即完成某个行为的时候，使用不同的对象会得到不同的状态
    - 实例展示：
        ```python
        class Animal:
            def make_sound(self):
                pass
        class Dog(Animal):
            def make_sound(self):
                print("汪汪汪")
        class Cat(Animal):
            def make_sound(self):
                print("喵喵喵")
        
        def make_sound(animal: Animal):
            animal.make_sound()
        
        dog = Dog()
        cat = Cat()
        make_sound(dog)    # 输出：汪汪汪
        make_sound(cat)    # 输出：喵喵喵
        ```
    - ~~很奇怪吧，脉门怎么自己开了~~
    - 使用同样的行为(函数)，传入不同的对象，却得到不同的结果，这就是多态
    - 多态经常作用在继承关系上，比如：
        - 函数(方法)形参声明接收父类对象，实机传入父类的子类对象进行工作
        - 即：以父类做定义声明，以子类做具体实现，用以获得统一行为，不同状态
- #### **抽象类(接口):** 由父类来定义一个空方法，具体实现方法由子类自行决定
    - 抽象类:含有抽象方法的类称之为抽象类
    - 抽象方法:方法体是空实现(`pass`)的方法称之为抽象方法
    - 为什么要使用抽象类？
        - 抽象类可以定义一组接口，子类必须实现这些接口，从而保证子类具有统一的行为。
        - 抽象类可以提供一些默认实现，子类可以选择覆盖或使用这些实现。
        - 抽象类好比定义一个标准，子类必须遵循这个标准来实现自己的功能。
    - 配合多态，可以实现:
        - 抽象的父类设计(设计标准)
        - 具体的子类实现(实现标准)