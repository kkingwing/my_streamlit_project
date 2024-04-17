import streamlit as st

"""会话管理 st.session_state"""

"""原理："""
with st.echo():
    """ 初始化"""
    if 'key' not in st.session_state:
        st.session_state['key'] = 'value'

with st.echo():
    """ session state也支持基础语法"""
    if 'key' not in st.session_state:
        st.session_state.key = 'value'

with st.echo():
    """读取（键值）"""
    st.write(st.session_state.key)
    """Outputs: value"""

with st.echo():
    """更新（键值）"""
    st.session_state.key = 'value2'  # Attribute API
    st.session_state['key'] = 'value2'  # Dictionary like API

with st.echo():
    """查看「会话状态」里有什么东西："""
    st.write(st.session_state)

st.divider()
# with st.echo():
#     """如果不存在这个「键」，那么报错：
#     st.write(st.session_state['value']) """
# st.write(st.session_state['value'])
# # Throws an exception!


with st.echo():
    """删除键 del"""
    st.session_state['key'] = 'value'
    # 删除单个键
    del st.session_state['key']

    # 删除所有键值：
    for key in st.session_state.keys():
        del st.session_state[key]
    # （删除所有键值也可以在浏览器右上角使用- 清除缓存，clear cache来达到。）

st.divider()
with st.echo():
    """组件的key会自动加到会话session_state中。"""
    st.text_input("Your name", key="name")
    st.write(st.session_state)


"""回调（diao）,返回调用，Callbacks，特指的是「通过事件触发的函数」将一个函数的触发值传给另一个函数，
主要优点是异步执行，而不是线性等待执行。"""

"""使用Callbacks 回调Session State"""

# 执行顺序:当更新Session状态以响应事件时，首先执行回调函数，然后从上到下执行应用程序。
# 要添加回调，请在小部件声明上方定义一个回调函数，并通过on_change(或on_click)参数将其传递给小部件。
# （用法暂略）

# 分割线 ————————————
st.divider()

"""表单回调: forms and callbacks"""


def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)


with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)


"""回调限制：
1. 只有form的st.form_submit_button有回调键
2. on_change和on_click只需要输入类型的组件回调
3. 实例化组件后，不需要通过会话状态来修改键值
"""