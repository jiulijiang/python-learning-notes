from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts
import json

def fun_echarts():
    """
    使用pyecharts绘制简单折线图
    :return:
    """
    # 导包，导入Line类
    from pyecharts.charts import Line
    # 创建Line对象
    line = Line()
    # 添加x轴数据
    line.add_xaxis(["1月", "2月", "3月", "4月", "5月"])
    # 添加y轴数据
    line.add_yaxis("销售额", [120, 200, 150, 80, 70])
    # 生成图表
    line.render("line_chart.html")


def fun_test_Line():
    """
    使用pyecharts处理复杂json文件绘制折线图
    :return:
    """
    # 打开文件并处理json数据
    f_i = open("印度.txt","r",encoding="utf-8")
    f_j = open("日本.txt","r",encoding="utf-8")
    f_a = open("美国.txt","r",encoding="utf-8")
    str_i = f_i.read().strip('jsonp_1629350745930_63180();')
    str_j = f_j.read().strip('jsonp_1629350745930_63180();')
    str_a = f_a.read().strip('jsonp_1629350745930_63180();')
    dict_i = json.loads(str_i)
    dict_j = json.loads(str_j)
    dict_a = json.loads(str_a)
    # 浅层剖析json结构
    trend_key_i = dict_i['data'][0]['trend']
    trend_key_j = dict_j['data'][0]['trend']
    trend_key_a = dict_a['data'][0]['trend']
    # 获取各个国家xy轴数据
    x_i = trend_key_i['updateDate'][0:300]
    y_i = trend_key_i['list'][0]['data'][0:300]
    x_j = trend_key_j['updateDate'][0:300]
    y_j = trend_key_j['list'][0]['data'][0:300]
    x_a = trend_key_a['updateDate'][0:300]
    y_a = trend_key_a['list'][0]['data'][0:300]
    # 创建line对象
    line = Line()
    # 添加x轴数据
    line.add_xaxis(x_i)  # 时间是共用的
    # 添加y轴数据
    line.add_yaxis("印度确诊人数", y_i, label_opts=LabelOpts(is_show=False))
    line.add_yaxis("日本确诊人数", y_j, label_opts=LabelOpts(is_show=False))
    line.add_yaxis("美国确诊人数", y_a, label_opts=LabelOpts(is_show=False))
    # 设置图表标题
    line.set_global_opts(
        title_opts=TitleOpts(title="2020年美日印新冠疫情确诊人数", pos_left = "center", pos_top = "1%")

    )
    # 生成图表
    line.render("line_chart.html")

if __name__ == '__main__':
    # fun_echarts()
    fun_test_Line()