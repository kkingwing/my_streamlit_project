from others.conn import  conn_sql_data

import pyecharts.options as opts
import streamlit as st
from pyecharts.charts import Line, Bar, Pie, Grid
from streamlit_echarts import st_pyecharts
import pandas as pd
from sqlalchemy import create_engine

import os

# === 一、连接sql（导自定义方法）  ===
is_streamlit_sharing = os.getenv("STREAMLIT_SHARE") is not None  # 判断环境
st.write(is_streamlit_sharing)
if is_streamlit_sharing:
    # 在 Streamlit Sharing 上运行的代码 , #  布署于st的写法；
    CON = st.connection("mydb", type="sql", autocommit=True)
    sql = 'SELECT * FROM `ods_sample_data`'
    df = CON.query(sql)
else:
    # 在其他环境（例如本地）运行的代码
    df = conn_sql_data(table_name_="ods_sample_data")

# === 一.2、筛选器  ===
# v1 基本逻辑
# with st.container():
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         label = '月'
#         sizer_month = sorted(df[label].unique(), reverse=False)
#         sel_month = st.multiselect(label=label, options=sizer_month)

# v2 遍历筛选器
# columns = ['月', '品牌', '性别']  # 定义要循环的标签
# selected_values_dict = {}
#
# with st.container():
#     col1, col2, col3, col4, col5 = st.columns(5)
#     for i, label in enumerate(columns):
#         with [col1, col2, col3, col4, col5][i]:  # 使用索引选择要用于此循环迭代的列
#             sizer_column = sorted(df[label].unique(), reverse=False)
#             selected_values = st.multiselect(label=label, options=sizer_column)
#             selected_values_dict[label] = selected_values
#
# # 使用筛选后的值来过滤 DataFrame
# df_sizer = df.copy()  # 复制 DataFrame，以便保留原始数据
# for label, selected_values in selected_values_dict.items():
#     if selected_values:
#         df_sizer = df_sizer[df_sizer[label].isin(selected_values)]


# v3 动态筛选器，与 columns元素数量相连
columns = ['月', '品牌', '性别', '地区', '年龄分段']  # 定义要循环的标签
selected_values_dict = {}  # 用于收集筛选器选择的数据，遍历过滤df
num_columns = len(columns)  # 确定要使用的列数
columns_list = st.columns(num_columns)  # 使用列表收集，在下方调用。不写固定的col1,col2等

with st.container():
    for i, label in enumerate(columns):
        with columns_list[i]:  # 使用索引选择要用于此循环迭代的列
            sizer_column = sorted(df[label].unique(), reverse=False)
            selected_values = st.multiselect(label=label, options=sizer_column)
            selected_values_dict[label] = selected_values

# 使用筛选后的值来过滤 DataFrame
df_sizer = df.copy()  # 复制 DataFrame，以便保留原始数据
for label, selected_values in selected_values_dict.items():
    if selected_values:
        df_sizer = df_sizer[df_sizer[label].isin(selected_values)]

# === 二、数据ETL  ===
## 1.范围筛选
df_filter = df_sizer.copy()
# 时间筛选
# df_filter = df_filter[df_filter['年'] == 2020]  # 数据源 - 行数据筛选
# 其它筛选
# ……

## 2.透视表
# 创建透视表 pivot_table_time
pt_time = df_filter.pivot_table(index=['月'], values=['销售额'], aggfunc='sum')
pt_brand = df_filter.pivot_table(index=['品牌'], values=['销售额'], aggfunc='sum')
pt_gender = df_filter.pivot_table(index=['性别'], values=['销售额'], aggfunc='sum')
pt_area = df_filter.pivot_table(index=['地区'], values=['销售额'], aggfunc='sum')
pt_phonetype = df_filter.pivot_table(index=['型号'], values=['销售额'], aggfunc='sum')
pt_age_range = df_filter.pivot_table(index=['年龄分段'], values=['销售额'], aggfunc='sum')

# 截取
pt_phonetype = pt_phonetype.sort_values(by='销售额', ascending=False)  # 排序截取前10个，只显示这部分
if len(pt_phonetype) >= 10:  # 过长时截取前10项
    pt_phonetype = pt_phonetype[:10]
pt_phonetype = pt_phonetype.sort_values(by='销售额', ascending=True)  # 逆序一下

# df_to_ls
ls_month = [str(month) + "月" for month in pt_time.index.tolist()]  # 注意，横轴不能是数值，只能是字符串构成
ls_brand = pt_brand.index.to_list()
ls_gender = pt_gender.index.to_list()
ls_area = pt_area.index.to_list()
ls_phonetype = pt_phonetype.index.to_list()
ls_age_range = pt_age_range.index.to_list()

# 各透视结果的对应销售额
ls_consume_month = pt_time['销售额'].to_list()
ls_consume_brand = sorted(pt_brand['销售额'].to_list(), reverse=False)
ls_consume_gender = pt_gender['销售额'].to_list()
ls_consume_area = pt_area['销售额'].to_list()
ls_consume_phonetype = pt_phonetype['销售额'].to_list()
ls_consume_age_range = pt_age_range['销售额'].to_list()

# == 全局色系 ==
color_1 = "#5470C6"  # blue ，默认蓝  red:"#d14a61" , black:"#304656"
color_2 = "#91CC75"  # green 默认绿


# === 三、连接pyecharts  ===
def line_month():  # 行1列1图
    # 透视表-数据
    x = ls_month  # 传入数据
    y = [round(x / 100000000, 2) for x in ls_consume_month]  # 除以亿
    # 创建折线图
    line = (
        Line(init_opts=opts.InitOpts(bg_color="#FFFFFF", )  # 背景色
             # animation_opts=opts.AnimationOpts(animation_delay=1000, animation_easing="elasticOut"),  # 动画延迟，
             )
        .add_xaxis(x)
        .add_yaxis("销售额",
                   y,
                   color=color_1,  # 色系1。 对这个数据系列都使用这个颜色，包括：线条、标记、图例等。
                   # areastyle_opts=opts.AreaStyleOpts(opacity=0.1),  # 面积图， opacity 不透视明度
                   # is_smooth=True, # 曲线
                   label_opts=opts.LabelOpts(is_show=False, ),  # 系列数据标签. 下方系列生效，其它系列不生效要其设置为False
                   # linestyle_opts=opts.LineStyleOpts(width=1),  # 「y轴线条不包含标点」的设置，一般不用，color="green"
                   # is_connect_nones=True,  # 跳过null空点连接
                   # is_symbol_show=True,  # 是否显示标记点
                   # is_step = True, # 阶梯样式
                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(name="最小值", type_="min"),  # 数据特征->标点
                                                           opts.MarkPointItem(name="最大值", type_="max"),
                                                           # opts.MarkPointItem(name="平均值",ttype_="average")
                                                           # opts.MarkPointItem(name="指定", coord=[x[2], y[2]], value=y[2])
                                                           ], ),
                   markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="平均线", type_="average"),  # 数据特征->标线
                                                         # opts.MarkLineItem(name="最小线",type_="min"),
                                                         # opts.MarkLineItem(name="最大线",type_="max"),
                                                         # opts.MarkLineItem(name="自定义线", y=100),
                                                         ], ),
                   )
        # .set_series_opts(label_opts=opts.LabelOpts(is_show=False,position="right", formatter="{c}亿"),)
        .set_global_opts(title_opts=opts.TitleOpts(title="月度趋势"),  # 标题。 「方法： 全局设置」
                         legend_opts=opts.LegendOpts(type_="scroll",  # 图例 -> 过长图例可滚动
                                                     orient="horizontal",  # 「图例」调整， # horizontal 水平，  vertical 垂直的
                                                     selected_map={"商家B": False,  # 将某数据系列不显示
                                                                   "商家C": False,
                                                                   "商家D": False,
                                                                   "商家E": False,
                                                                   "商家F": False,
                                                                   },
                                                     pos_left=None,  # 左边距，默认居中。 "35%"
                                                     pos_top=None,  # 上边距  "0%"
                                                     ),
                         xaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show=True),  # 是否显示「轴线条」
                                                  splitline_opts=opts.SplitLineOpts(is_show=False),  # 去x轴网格线
                                                  axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                                                  # 面积图是否「贴靠到轴」
                                                  boundary_gap=True,  # 中间点于「轴还是中间」,True在网格中间
                                                  is_show=True,  # x轴的轴身是否显示
                                                  min_=0,  # 0  # x轴最小值，只在数值时起效
                                                  # max_=10, # x轴最大值
                                                  name="月份",  # 轴轴标题
                                                  offset=10,  # 轴数值偏移
                                                  ),
                         yaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show=True, ),  # 是否显示「轴线条」
                                                  splitline_opts=opts.SplitLineOpts(is_show=False),  # 去y轴网格线
                                                  # type_="log",  # 设置为「对数轴」
                                                  is_show=True,  # y轴的轴身是否显示
                                                  name="金额",  # y轴轴标题
                                                  # min_=0,  # y轴最小值，起始点非0
                                                  # max_=200, # y轴最大值
                                                  # offset=-30,  # 轴数值偏移
                                                  # position="middle",  # ? 未知
                                                  # name_location='end',  # 轴标题位置
                                                  axislabel_opts=opts.LabelOpts(formatter="{value}亿"),  # 标签格式
                                                  ),
                         tooltip_opts=opts.TooltipOpts(
                             trigger="axis", axis_pointer_type="cross", formatter="{c}亿",  # 鼠标移至时的互动提示
                         ),
                         )
    )
    show_width = str((1920 - 300) * 2 / 3)
    st_pyecharts(line, height="380px", width="100%")


def bar_brand():
    """条形图"""
    x = ls_brand
    y = [round(x / 100000000, 2) for x in ls_consume_brand]  # 除以亿

    c = (
        Bar()
        .add_xaxis(x)
        .add_yaxis(
            "销售额",
            y,
            category_gap="60%",
            color=color_1,
        )
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right", formatter="{c}亿"))
        .set_global_opts(title_opts=opts.TitleOpts(title="品牌排名"),  # 标题。 「方法： 全局设置」
                         legend_opts=opts.LegendOpts(type_="scroll",  # 图例 -> 过长图例可滚动
                                                     orient="horizontal",  # 「图例」调整， # horizontal 水平，  vertical 垂直的
                                                     selected_map={"商家B": False,  # 将某数据系列不显示
                                                                   "商家C": False,
                                                                   "商家D": False,
                                                                   "商家E": False,
                                                                   "商家F": False,
                                                                   },
                                                     pos_left=None,  # 左边距，默认居中。 "35%"
                                                     pos_top=None,  # 上边距  "0%"

                                                     ),
                         xaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show=False),  # 是否显示「轴线条」
                                                  splitline_opts=opts.SplitLineOpts(is_show=False),  # 去x轴网格线
                                                  axistick_opts=opts.AxisTickOpts(is_align_with_label=True, ),
                                                  # 面积图是否「贴靠到轴」
                                                  boundary_gap=True,  # 中间点于「轴还是中间」,True在网格中间
                                                  # is_show=False,  # x轴的轴身是否显示
                                                  # min_=0,  # 0  # x轴最小值，只在数值时起效
                                                  max_=int(max(y) * 1.35),  # 条形图，x轴的最大值
                                                  # max_=10, # x轴最大值
                                                  # name="月份",  # y轴轴标题
                                                  ),
                         yaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show=True, ),  # 是否显示「轴线条」
                                                  splitline_opts=opts.SplitLineOpts(is_show=False),  # y轴网格线
                                                  # type_="log",  # 设置为「对数轴」
                                                  # is_show=True,  # y轴的轴身是否显示
                                                  # min_=0,  # y轴最小值，起始点非0
                                                  # max_=int(max(ls_consume_brand) * 1.2),  # ,200, # y轴最大值
                                                  name="金额",  # y轴轴标题
                                                  ),
                         tooltip_opts=opts.TooltipOpts(trigger="axis",
                                                       axis_pointer_type="cross",
                                                       formatter="{b} {c}亿"
                                                       ),  # 鼠标移动时显示两轴标签
                         )
    )

    st_pyecharts(c, height="755px", width="100%")


def pie_sex():
    x = ls_gender
    y = [round(x / 100000000, 2) for x in ls_consume_gender]  # 除以亿
    data = sorted([list(z) for z in zip(x, y)], reverse=True)
    c = (
        Pie()

        .add("金额",  # 系列名称，在鼠标移过去时的提示名称
             data,  # 数据
             center=["50%", "50%"],  # 饼图位置 [距离左侧距离，距离上方距离]
             radius=["40%", "55%"],  # 中心空白圈大小，饼图缩放比例
             # rosetype="area", # 是否显示为玫瑰图
             )
        .set_global_opts(title_opts=opts.TitleOpts(title="性别占比"),  # 「标题」调整
                         legend_opts=opts.LegendOpts(orient="horizontal",  # 「图例」调整， horizontal水平，vertical垂直
                                                     pos_left="40%",  # 左边距
                                                     pos_top="5%",  # 上边距
                                                     type_="scroll",  # 可滚动，过长的图例碰到边界会自动隐藏
                                                     ), )
        .set_series_opts(tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c}亿 ({d}%)", ),  # 提示
                         label_opts=opts.LabelOpts(formatter="{b}: {d}%", ),  # 直接显示标签 （a系列名称 b名称 c数值 d百分比）
                         )
        # 「颜色」调整. 同一色系不同深浅，取色地址 ：https://0to255.com/254,121,74。 也可设置不同色系
        # .set_colors(["#e13c01", "#fe5317", "#fe6c39", "#fe865b", "#fe865b", "#feab8e", "#ffc4af"])
        .set_colors([color_1, color_2])
    )
    st_pyecharts(c, height="550px", width="100%")  # 内置的只有light和dark，其它的需要设置或安装


def bar_phonetype():
    """条形图"""
    x = ls_phonetype
    y = [round(x / 100000000, 2) for x in ls_consume_phonetype]

    c = (
        Bar()
        .add_xaxis(x)
        .add_yaxis(
            "销售额",
            y,
            category_gap="60%",
            color=color_1,
            bar_width=18,  # 条宽度
        )
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="right", formatter="{c}亿"))
        # 全局设置
        .set_global_opts(title_opts=opts.TitleOpts(title="手机型号", pos_left="20%"),  # 标题，偏移与grid偏移相同
                         legend_opts=opts.LegendOpts(type_="scroll",  # 图例 -> 过长图例可滚动
                                                     orient="horizontal",  # 「图例」调整， # horizontal 水平，  vertical 垂直的
                                                     selected_map={"商家B": False,  # 将某数据系列不显示
                                                                   "商家C": False,
                                                                   "商家D": False,
                                                                   "商家E": False,
                                                                   "商家F": False,
                                                                   },
                                                     pos_left=None,  # 左边距，默认居中。 "35%"
                                                     pos_top=None,  # 上边距  "0%"
                                                     ),
                         xaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show=True),  # 是否显示「轴线条」
                                                  splitline_opts=opts.SplitLineOpts(is_show=False),  # 去x轴网格线
                                                  axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                                                  # 面积图是否「贴靠到轴」
                                                  # boundary_gap=True,  # 中间点于「轴还是中间」,True在网格中间
                                                  is_show=False,  # x轴的轴身是否显示
                                                  # min_=0,  # 0  # x轴最小值，只在数值时起效
                                                  # max_=float(max(y) * 1.35),  # 条形图，x轴的最大值
                                                  # max_=10, # x轴最大值
                                                  # name="月份",  # y轴轴标题
                                                  # offset=-60,  # 标签与轴的距离
                                                  ),
                         yaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show=True, ),  # 是否显示「轴线条」
                                                  splitline_opts=opts.SplitLineOpts(is_show=False),  # 去y轴网格线
                                                  # type_="log",  # 设置为「对数轴」
                                                  # is_show=True,  # y轴的轴身是否显示
                                                  # min_=0,  # y轴最小值，起始点非0
                                                  # max_=int(max(ls_consume_brand) * 1.2),  # ,200, # y轴最大值
                                                  name="金额",  # y轴轴标题
                                                  # offset=-30,  # 标签与轴的距离
                                                  position="left",  # 标签位置，左右

                                                  ),
                         tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross",
                                                       formatter="{b} {c}亿"),  # 鼠标移动时显示两轴标签
                         )
    )
    # 创建网格布局，偏移左边距
    grid = Grid()
    grid.add(c, grid_opts=opts.GridOpts(pos_left="30%", pos_right="20%"))
    # 创建网格布局
    st_pyecharts(grid, height="550px", width="100%")


def bar_area_sale():
    x = ls_area
    y = [round(x / 100000000, 2) for x in ls_consume_area]
    c = (
        Bar()
        .add_xaxis(x, )
        .add_yaxis("销售额", y, color=color_1, )
        # .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="地区销售", ),

                         xaxis_opts=opts.AxisOpts(is_show=True,
                                                  # is_inverse=True, # 上下翻转
                                                  boundary_gap=True,  # ? 未知
                                                  position="start",  # ? 未知
                                                  # offset=-30,  # 轴数值偏移
                                                  # min_=10000,  # 轴最小值
                                                  axislabel_opts=opts.LabelOpts(is_show=True,  # 显示标签
                                                                                rotate=45,  # 签旋转 45 度
                                                                                margin=10,  # 标签与轴线的距离为 10
                                                                                # interval="auto",  # 自动调整标签间隔
                                                                                # position="end",  # 标签显示在轴线的末端
                                                                                )
                                                  ),
                         yaxis_opts=opts.AxisOpts(is_show=True,
                                                  # is_inverse=True, # 上下翻转
                                                  boundary_gap=True,  # ? 未知
                                                  position="end",  # ? 未知
                                                  # offset=-30,  # 轴数值偏移
                                                  # min_=10000,  # 轴最小值
                                                  axislabel_opts=opts.LabelOpts(formatter="{value}亿"),  # 标签格式
                                                  ),

                         )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False, formatter="{c}亿", ),
                         markline_opts=opts.MarkLineOpts(
                             data=[opts.MarkLineItem(type_="average", name="平均值"),
                                   # opts.MarkLineItem(type_="min", name="最小值"),
                                   # opts.MarkLineItem(type_="max", name="最大值"),
                                   ]),
                         markpoint_opts=opts.MarkPointOpts(
                             data=[opts.MarkPointItem(type_="max", name="最大值", ),
                                   opts.MarkPointItem(type_="min", name="最小值"),
                                   # opts.MarkPointItem(type_="average", name="平均值"),
                                   ]),
                         tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{b} {c}亿", ),  # 互动提示
                         )
    )
    st_pyecharts(c, height="350px", width="100%")


# === BI布局 ===

# === 四、连接pyecharts  ===
with st.container():
    col1, col2 = st.columns([3, 2])
    # 此处放往入「平台筛选器」
    with col1:
        with st.container():  # border=True,
            line_month()
            bar_area_sale()

    with col2:
        with st.container():  # border=True,
            bar_brand()

with st.container():
    col1, col2 = st.columns([2, 3])

    with col1:
        pie_sex()

    with col2:
        bar_phonetype()

# 色系 √
# 轴标签 √
# 轴边距 √
# 关联筛选器 √
# 高度集成。
#
