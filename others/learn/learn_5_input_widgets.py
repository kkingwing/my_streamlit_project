import streamlit as st

"""点击按钮 st.button，选回bool """
# primary 设置默认的「主要样式」，高亮为红色。 默认是secondary，即默认样式。
st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there:smile:')
else:
    st.write('Goodbye')

# 页面分割线 ——————————————————————————
st.divider()

"""下载按钮 st.download_button，返回：最后结果的点击时为True，其它情况为False"""

# """下载csv"""
# (关于如何下载为Excel后面再查「社区交流」)
# 设置一个随机给下载的数据 my_large_df
import pandas as pd
import numpy as np


# 写下面这个函数是为了缓存数据，避免重复计算
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


# 创建一个下载的df
my_large_df = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob', 'Charlie', 'David'],
    'Age': np.random.randint(18, 40, size=5),  # 随机生成年龄在18到40之间的整数
    'Salary': np.random.uniform(30000, 80000, size=5),  # 随机生成在30,000到80,000之间的浮点数
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
})

csv1 = convert_df(my_large_df)
st.download_button(label='Download data as csv',
                   data=csv1,  # 要下载的内容
                   file_name='large_df.csv',  # 下载文件名
                   mime='text/csv',  #
                   )
# """下载一个文本"""
import streamlit as st

text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

# """下载一个二进制文件"""
import streamlit as st

binary_contents = b'example content'
# Defaults to 'application/octet-stream'
st.download_button('Download binary file', binary_contents)

# """下载图片"""
import streamlit as st

# 这个图径是「相对于主程序的路径」，而「不是副页面路径」，（不是当前代码所在的相对路径）。
with open("images/flower.png", "rb") as file:
    btn = st.download_button(
        label="Download image",
        data=file,
        file_name="flower.png",
        mime="image/png"
    )

# 页面分割线 ——————————————————————————
st.divider()

"""超链接 st.link_button，无返回"""
import streamlit as st

# label 标签， url 跳转标签
st.link_button("Go to gallery", "https://streamlit.io/gallery")

# 页面分割线 ——————————————————————————
st.divider()

"""复选框 st.checkbox，返回bool"""
import streamlit as st

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
# 页面分割线 ——————————————————————————
st.divider()

"""切换 st.toggle，返回bool"""
import streamlit as st

on = st.toggle('开启爬虫')  # 使用中间变量，增强可读性与可维护性
if on:
    st.write('爬虫开启。')

# 页面分割线 ——————————————————————————
st.divider()

"""单选项 st.radio，返回选择选项"""
import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

# 页面分割线 ——————————————————————————
st.divider()

"""单选项 - 标签隐藏、水平排列 st.radio"""
import streamlit as st

# （暂未理解逻辑，用时再梳理）

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )

# 页面分割线 ——————————————————————————
st.divider()

"""选择框 st.selectbox"""
import streamlit as st

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

"""选择框 的隐藏与调用"""
st.link_button('见官网，略', 'https://docs.streamlit.io/library/api-reference/widgets/st.selectbox')

# 页面分割线 ——————————————————————————
st.divider()

"""复选框  st.multiselect ，返回「选择列表」"""
import streamlit as st

options = st.multiselect(
    label='What are your favorite colors',  # 注释
    options=['Green', 'Yellow', 'Red', 'Blue'],  # 可选项
    default=['Yellow', 'Red']  # 默认选项
)

st.write('You selected:', options)

# 页面分割线 ——————————————————————————
st.divider()

"""滑动条 st.slider ，返回滑动的当前值"""
# 接受：小数，整数，日期，时间
# 接受，两个值作为一组选择范围
import streamlit as st

# 标签、最小值、最大值、默认值，如果这个value传的是一组数，就是范围选择
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
"""范围滑动条，传入的是元组如：(25.0, 75.0)"""
import streamlit as st

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
"""时间范围滑动条，"""
import streamlit as st
from datetime import time

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
"""日期滑动条"""
import streamlit as st
from datetime import datetime

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="YYYY-MM-DD HH:mm")
st.write("Start time:", start_time)

# 页面分割线 ——————————————————————————
st.divider()

"""另一种滑动条 st.select_slider，接受任何类型，返回当前选择值"""
import streamlit as st

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

"""同理的范围选择"""
import streamlit as st

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

# 页面分割线 ——————————————————————————
st.divider()

"""文本输入  st.text_input，返回组件的当前值"""
# 可以密码输入为*，详情见参数文档
import streamlit as st

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

"""文本隐藏"""
st.link_button('key冲突，详情见页面', 'https://docs.streamlit.io/library/api-reference/widgets/st.text_input')

# 页面分割线 ——————————————————————————
st.divider()

"""数字输入：st.number_input，返回组件当前值"""
import streamlit as st

number = st.number_input('Insert a number')
st.write('The current number is ', number)

"""初始化为空值"""
import streamlit as st

number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write('The current number is ', number)

# 页面分割线 ——————————————————————————
st.divider()

"""多行文本框：st.text_area，返回组件当前值"""
import streamlit as st

txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)

st.write(f'You wrote {len(txt)} characters.')

# 页面分割线 ——————————————————————————
st.divider()

"""日历选择组件： st.date_input，返回组件当前值"""
import datetime
import streamlit as st

# value是'today'则是今天，如果是两个值的元组则可以选择范围，如果是日期则是+10年可选择。
d = st.date_input("When's your birthday", value='today')  # datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

"""例2：范围选择"""
import datetime
import streamlit as st

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)
d
"""例3：初始化为空日期"""
import streamlit as st

d = st.date_input("When's your birthday？", value=None)
st.write('Your birthday is:', d)

# 页面分割线 ——————————————————————————
st.divider()

"""分时组件 st.time_input，返回组件当前值"""
# 步长默认15分钟，参数可选

import datetime
import streamlit as st

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)
"""例2：初始化为空"""
import datetime
import streamlit as st

t = st.time_input('Set an alarm for', value=None)
st.write('Alarm is set for', t)

# 页面分割线 ——————————————————————————
st.divider()

"""文件上传组件：st.file_uploader，返回上传文件列表list，文件为UploadedFile对象"""
# 默认上传不超过200MB，可设置
import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

# 页面分割线 ——————————————————————————
st.divider()
"""用户摄像头组件：st.camera_input，返回照片UploadedFile文件对象或None"""
import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

"""读取图像缓冲"""
import streamlit as st

img_file_buffer = st.camera_input("Take a picture2")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
"""图像处理示例"""
st.link_button("Image processing examples","https://docs.streamlit.io/library/api-reference/widgets/st.camera_input")


# 页面分割线 ——————————————————————————
st.divider()

"""颜色选择组件"""
import streamlit as st

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)