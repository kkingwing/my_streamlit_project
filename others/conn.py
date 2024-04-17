import pandas as pd
from sqlalchemy import create_engine
import streamlit as st

# CON = st.connection("mydb", type="sql", autocommit=True) # 布署云文档时的连接。连接sql
CON = create_engine("mysql://root:huanqlu0123@39.98.120.220:3306/spider?charset=utf8mb4")


# ===  一、 源数据连接，ods/dw ===
@st.cache_data  # 缓存装饰器 （第一次为真正读取，其后使用缓存的df）
def conn_sql_data(table_name_="ods_sample_data"):
    df = pd.read_sql_table(table_name_, CON)
    return df
