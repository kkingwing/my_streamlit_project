import streamlit as st
from datetime import datetime

import pandas as pd

# st.set_page_config(layout="wide")  # 必须在开头，且第一个调用

CON = st.connection("mydb", type="sql", autocommit=True)
print(CON)
TODAY = datetime.now().strftime("%Y-%m-%d")

st.subheader(' 📰**热榜聚合** ' + TODAY)

st.divider()

# === 读取sql数据作为「预置数据」以备使用 , 下面的写法是st专用方法===
sql = 'SELECT * FROM `aggregate_hot_list`'
# df = pd.read_sql(sql=sql, con=CON)  #st不这么调用，注释掉
df = CON.query(sql)

# 1. 读取sql的「知乎」热榜数据
df_zhihu = df[(df['平台'] == '知乎') & (df['记录日期'] == TODAY)][:]
zh_titles = list(df_zhihu['标题'])
zh_urls = list(df_zhihu['url'])
zh_hots = list(df_zhihu['热度'])

# 2.读取sql的「微博」热榜数据
df_weibo = df[(df['平台'] == '微博') & (df['记录日期'] == TODAY)][:]
wb_titles = list(df_weibo['标题'])
wb_urls = list(df_weibo['url'])
wb_hots = list(df_weibo['热度'])

# 3.读取sql的「百度」热榜数据
df_baidu = df[(df['平台'] == '百度') & (df['记录日期'] == TODAY)][:]
baidu_titles = list(df_baidu['标题'])
baidu_urls = list(df_baidu['url'])
baidu_hots = list(df_baidu['热度'])

# 4.读取sql的「IT之家」热榜数据
df_ithome = df[(df['平台'] == 'IT之家') & (df['记录日期'] == TODAY)][:]
ithome_titles = list(df_ithome['标题'])
ithome_urls = list(df_ithome['url'])
ithome_hots = list(df_ithome['热度'])


def to_wan_hot(hot):
    """
    将微博的数字转换为万的单位并加上文本 "万热度"

    Args:
        hot: 数字型文本

    Returns:
        str: 转换后的文本
    """
    if not hot:
        return ""
    try:
        hot_num = float(hot)
        if hot_num >= 10000:
            return f"{hot_num / 10000:.1f} 万热度"
        else:
            return f"{hot:.0f}"
    except ValueError:
        return hot


# === 以下为「页面布局」及「读取预置数据」。
# st.tabs() # 标签布局
tab_hotlist, tab3 = st.tabs(["热搜榜单", "Owl"])

# 布局： tab标签
with tab_hotlist:
    col1, col2, col3, col4 = st.columns([0.35, 0.35, 0.35, 0.35])  # 分组栏
    # === 分组栏 ===
    with col1:
        # === 容器 ===
        with st.container(border=True, height=520):
            st.caption('知乎')
            for i, (title, url, hot) in enumerate(zip(zh_titles, zh_urls, zh_hots)):
                md_zhihu = f"{i + 1}. [{title}]({url})  :red[{to_wan_hot(hot)}]\n"
                st.write(md_zhihu)
            st.divider()

    with col2:
        with st.container(border=True, height=520):
            st.caption('微博')
            # st.divider()
            for i, (title, url, hot) in enumerate(zip(wb_titles, wb_urls, wb_hots)):
                md_zhihu = f"{i + 1}. [{title.strip('#')}]({url})  :red[{to_wan_hot(hot)}]\n"
                st.write(md_zhihu)
            st.divider()

    with col3:
        with st.container(border=True, height=520):
            st.caption('百度')
            # st.divider()
            for i, (title, url, hot) in enumerate(zip(baidu_titles, baidu_urls, baidu_hots)):
                md_zhihu = f"{i + 1}. [{title}]({url})  :red[{to_wan_hot(hot)}]\n"
                st.write(md_zhihu)
            st.divider()

    with col4:
        with st.container(border=True, height=520):
            st.caption('IT之家')
            # st.divider()
            for i, (title, url, hot) in enumerate(zip(ithome_titles, ithome_urls, ithome_hots)):
                md_zhihu = f"{i + 1}. [{title}]({url})  :red[{to_wan_hot(hot)}]\n"
                st.write(md_zhihu)
            st.divider()

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# with tab_test:
#     # 1. 读取sql的「知乎」热榜数据
#     df_zhihu = df[(df['平台'] == '知乎') & (df['记录日期'] == TODAY)][:10]
#     zh_titles = list(df_zhihu['标题'])
#     zh_urls = list(df_zhihu['url'])
#     zh_hots = list(df_zhihu['热度'])
#     with st.container(border=True):
#         st.markdown('<h3>知乎</h3>', unsafe_allow_html=True)
#         st.dataframe(data=df_zhihu,  # 呈现的df
#                      column_order=('标题',  '热度','url',),  # df要显示的列
#                      use_container_width=True,  # 使用父容器宽度
#                      hide_index=True,  # 隐藏索引
#                      height=500,  # 整体高度 ，热榜呈现队所有50条内容，但在这里限制可度时可用。
#                      # width=400,  # 宽度
#                      column_config={  # 配置具体列的呈现样式
#                          "url": st.column_config.LinkColumn('url',
#                                                             # display_text="Open profile"
#                                                             display_text='跳转',
#                                                             ),
#                      },
#                      )
