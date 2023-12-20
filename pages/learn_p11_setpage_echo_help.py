import streamlit as st

""" 多功能工具"""

"""页面设置 st.set_page_config"""
st.write('**见主程序第一个命令。**')
# 「必须有」且「只有一个」在app的「首行」运行的命令。'
#
# st.set_page_config(
#     page_title=None,  # 浏览器的标签标题，如果为None，标签会是一个「app.py」的「app • Streamlit 」
#     page_icon=None,  # 标签图标，支持emoji
#     layout="centered",  # 主区域布局，默认为「居中的centered「，也可以选为「布满的wide」
#     initial_sidebar_state="auto",  # 侧边栏是否展开，一般为auto，其它不管是expanded或是collapsed在手机上显示都不太好
#     menu_items=None
# )

# 分割线————————————
st.divider()

"""显示执行结果的代码  st.echo"""
"""例1 简单作用"""
import streamlit as st

with st.echo():
    st.write('This code will be printed')

"""例2 起作用的代码示例"""
import streamlit as st

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

# 分割线————————————
st.divider()

"""帮助文档 st.help"""

import streamlit as st

st.help(st.container)


