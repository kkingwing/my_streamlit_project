import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')  # 主标题（一级标题）

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


# cache_data的本质是「检查输入函数以及函数的内部结构」如果这两者没变，就直接使用结果值。
# 如果代码需要长时间运行，考虑重构，使用@st.cache_data。
@st.cache_data  # 缓存数据，如果数据不变，则不再重复计算。
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# 1.1 读取数据（使用@st.cache_data）缓存加快每次读取的加载速度
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

# 1.2.1 原始数据查看（确认数据无误）
# st.subheader('Raw data')  # 子标题（二级标题）
# st.write(data)
# 1.2.2 使用复选框查看
if st.checkbox('show raw data'):
    st.subheader('Raw data')
    st.write(data)

# 2. 添加「直方图」（即「柱状图」）查看。（可视化，以小时查看，分析最繁忙的时间）
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)
# （找到最繁忙的时间是下午是17点）


# 3. 地图绘制
# st.subheader('Map of all pickups')
# st.map(data)
# # 3.2 分析集中在17点在地图特点
# st.subheader('Map of 17')
# hour_to_filter = 17
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# st.map(filtered_data)
# # 复制的地图绘制查看（st.pydeck_chart）

# 3.3 使用小组件实时更新小时（将固定的变量，使用「组件」来互动输入）
st.subheader('Map of slider')
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
# 复制的地图绘制查看（st.pydeck_chart）

# 用到知识点： 一级标题 ，二级标题 ，复选框，表格，直方图， 滑块，地图，
# （更多小组件查看api，要把所有的小组件都用一遍。）
