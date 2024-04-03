import streamlit as st
import pandas as pd

# st.write() 可以显示任何东西

# 1. 文本
st.write('Hello, *Sunshine*!  :sunglasses:')

# 2. 数字
st.write(12345)

# 3. 表格
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# * 可以传多个参数
st.write('1+1=', 2)
st.write('Below is a DataFrame:', df, 'Above is a DataFrame.')

# 4. 图表
import numpy as np
import altair as alt

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)
c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.write(c)



# Magic特性几乎可以显示任何东西，而不用输入显式的命令，只要他出现在代码行中。
# st.write()可以显示任何东西。（magic极简用法暂不支持非主程序，暂不用Magic用法）

import streamlit as st

# 绘写文本，写在import下方的文本将被识别为Magic识别为显示代码，在库上方的将忽略
'''
# This is the document title

This is some _markdown_.
'''

import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4]})
df

x = 10
'x', x  # 字符，变量

import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
fig  # 画图

"""
关于是否使用magic，我觉得这就跟下雨天，
你到一个商店里，说：拿把伞，或是拿一把可以挡住一个人的黑色伞。
一个出现了就知道是什么意思，一个是指定确认的东西。
这两者的目的相同。 
若要极简，则使用极简的变量出现，是趋势。
使用Magic理念，是合适的。
而jupyter notebook，也是这种原理。
而目前，由于streamlit「只支持在主运行.py文件」中使用，而不支持在其它页面中使用，
写法仍暂以具体写法为注，即，使用 st.write() ，则不直接写命令。
"""
