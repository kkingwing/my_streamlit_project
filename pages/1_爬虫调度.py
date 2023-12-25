import streamlit as st
from scripts.app_schedules import run_1, run_0

# url页面标签的标题
st.set_page_config(page_title="调度运维", page_icon="📈")
st.title('程序调度')

# 初始化按钮状态
if 'toggle_1_state' not in st.session_state:
    st.session_state['toggle_1_state'] = False


# 子标题
with st.container():
    st.divider()
    col1, col2, col3 = st.columns([15, 35, 50], gap='medium')
    col1.subheader('序号')
    col2.subheader('调度名称')
    col3.subheader('开关：')

# 1.测试 - 复制表格
with st.container():
    st.divider()
    col1, col2, col3 = st.columns([15, 35, 50], gap='medium')
    col1.write('1')
    col2.write('复制目标表格')
    on_1 = col3.button('启动', key='button_1')  # 办公自动化不适合用「toggle」，会使bool切换混乱。
    if on_1:
        col3.write(on_1)
        run_0()
        st.success('运行完成')

# 2.排行榜
with st.container():
    col1, col2, col3 = st.columns([15, 35, 50], gap='medium')
    col1.write('2')
    col2.write('排行榜')
    on_1 = col3.button('启动', key='button_2')  # 办公自动化不适合用「toggle」，会使bool切换混乱。
    if on_1:
        col3.write(on_1)
        run_1()
        st.success('运行完成')

# 暂放，未用。
st.sidebar.selectbox('选择调度', ['复制目标表格', '排行榜'])