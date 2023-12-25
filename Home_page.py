import streamlit as st

st.set_page_config(
    page_title='Center control',  # 浏览器的标签标题，
    page_icon='🔥',  # 标签图标，支持emoji
    layout='wide',  # 主区域布局，默认为「居中的centered「，也可以选为「布满的wide」
    initial_sidebar_state='auto',
    menu_items={  # 右上角文字链接，键为固定字符串
        'Get Help': 'https://www.extremelycoolapp.com/help',
    }

)

st.title('调度中心')

with st.sidebar:
    st.success("选择上方一个页面")

st.markdown(
    """
    这是一个总控页面，作用是「**调度控制**」以及「**数据分析**」展示。
    选择「**左侧页面**」进入详情查看。
    ### 更多的信息：
    - 需要协助：[先查询吧](https://www.google.com)
    - 有不懂的：查看[streamlit文档](https://docs.streamlit.io)
    """
)
