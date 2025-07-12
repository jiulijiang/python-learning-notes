## day_6
### JSON数据格式
- JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，易于人阅读和编写，同时也易于机器解析和生成，本质上是一个带有特定格式的字符串
- 主要功能：一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互
- JSON的基本格式：
    ```json
    {
        "name": "张三",
        "age": 18,
        "is_student": true,
        "courses": ["数学", "英语", "物理"],
        "address": {
            "city": "北京",
            "zip_code": "100000"
        }
    }
    ```  

    - json数据格式相当于Python中的字典（dict），也可以是外面是列表，里面是字典的数据结构，比如：
    ```json
    [
        {
            "name": "张三",
            "age": 18
        },
        {
            "name": "李四",
            "age": 20
        }
    ]
    ```
- Python数据和json数据转换：
    - Python对象转json字符串：使用`json.dumps(data)`方法,如果有中文，需要设置`ensure_ascii=False`
    - json字符串转Python对象：使用`json.loads(data)`方法
    - `data`是一个Python对象，可以是字典或者嵌套字典的列表等
### `pyecharts`模块
- `pyecharts`是一个用于生成图表的Python库，支持多种图表类型，如折线图、柱状图、饼图等
- `pyecharts`的安装：使用`pip install pyecharts`命令安装
- 构建基础折线图：
    ```python
    #导包，导入Line类
    from pyecharts.charts import Line  
    #创建Line对象
    line = Line()
    #添加x轴数据
    line.add_xaxis(["1月", "2月", "3月", "4月", "5月"])
    #添加y轴数据
    line.add_yaxis("销售额", [120, 200, 150, 80, 70])
    #生成图表
    line.render("line_chart.html")
    ```
    - `add_yaxis`方法添加y轴数据，参数包括系列名称和数据列表。
    - `add_xaxis`方法添加x轴数据，参数为一个列表。
    - `render`方法生成图表并保存为HTML文件，可以在浏览器中查看。
- `set_global_opts`方法设置全局配置项，如标题、图表大小、坐标轴标签、工具栏等。
    ```python
    line.set_global_opts(
        title="销售数据",  # 设置图表标题
        xaxis_title="月份",  # 设置x轴标题
        yaxis_title="销售额",  # 设置y轴标题
        toolbox_opts={  # 添加工具栏
            "show": True,
            "feature": {
                "saveAsImage": {}
            }
        }
    )
    ```
    - 标题配置:`title = "标题"`
    - x轴配置:`xaxis_title = "x轴标题"`
    - y轴配置:`yaxis_title = "y轴标题"`
    - 工具栏配置:`toolbox_opts = {"show": True, "feature": {"saveAsImage": {}}}`，可以添加保存为图片等功能
    - 更多功能可以参考`pyecharts`的[官方文档](https://pyecharts.org/#/zh-cn/global_options)，了解如何自定义图表样式、添加图例、设置颜色等。
