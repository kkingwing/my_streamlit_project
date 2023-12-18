# st.metric 标签度量值
import streamlit as st
"""
st.metric(
label,  # 显示的「标签」，即显示的文本
value,   # 显示的「数字」
delta=None,  # 「环比变化」
delta_color="normal",   # 环比升降「红绿色」的设置，默认绿升，要反转将实参改为：inverse
help=None,  # 悬浮帮助提示
label_visibility="visible" # 是否可见
)
"""


import streamlit as st

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

