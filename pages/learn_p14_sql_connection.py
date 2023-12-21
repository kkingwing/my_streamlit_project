import streamlit as st

"""连接数据库 st.connection()"""
# sql的连接要用 st.connection("<name>",type="sql")

"""例1 直接写明文的连接"""

# con = create_engine('mysql://root:pass@address:port/db?charset=utf8')

# conn = st.connection(
#     name="阿里云-ECS",  # 可自定义，连接的标识
#     type="sql",  # 固定写法（不可变）
#     url=con_url,  # url固定形参（不可变）
# )
# df = conn.query("select * from crawl_ip")  # .query快速查询，同样使用了cache缓存技术
# st.dataframe(df)

"""例2 连接配置文件.toml"""
# 1. 手动在根目录新建「.streamlit」文件夹，及其下级文件「secrets.toml」
# 2. 配置（见文件）
# 3. 引用：

# streamlit_app.py
conn = st.connection("mydb", type="sql", autocommit=True)
df2 = conn.query("select * from crawl_ip")
st.dataframe(df2)


"""失效重连  .reset"""
# import streamlit as st
#
# conn = st.connection("mydb")
#
# # Reset the connection before using it if it isn't healthy
# st.write("Note: is_healthy() 不是一个真方法，这里只是举例")
# if not conn.is_healthy():
#     conn.reset()