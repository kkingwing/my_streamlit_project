import streamlit as st

# url页面标签的标题
st.set_page_config(page_title="爬虫调度", page_icon="📈")

st.title('爬虫调度页面')
bool_1 = st.toggle('激活爬虫')
st.write('爬虫激活状态：', bool_1)
