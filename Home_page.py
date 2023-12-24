import streamlit as st

st.set_page_config(
    page_title='Center control',
    page_icon='🔥',
    layout='wide',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
    }

)

st.title('调度中心')

# st.set_page_config(
#     page_title=None,  # 浏览器的标签标题，如果为None，标签会是一个「app.py」的「app • Streamlit 」
#     page_icon=None,  # 标签图标，支持emoji
#     layout="centered",  # 主区域布局，默认为「居中的centered「，也可以选为「布满的wide」
#     initial_sidebar_state="auto",  # 侧边栏是否展开，一般为auto，其它不管是expanded或是collapsed在手机上显示都不太好
#     menu_items=None
# )

with st.sidebar:
    st.success("选择一个页面")


st.markdown(
    """
    这是一个总控页面，作用是「**调度控制**」以及「**数据分析**」展示。
    选择「**左侧页面**」进入详情查看。
    ### 更多的信息：
    - 需要协助：[先查询吧](https://www.google.com)
    - 有不懂的：查看[streamlit文档](https://docs.streamlit.io)
    """
)