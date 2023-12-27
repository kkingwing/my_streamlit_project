import streamlit as st

"""性能优化 —— 缓存： st.cache_data  st.cache_resource"""

"""例1 ： st.cache_data 检查「输入参数」与「函数构造」，若都不变，则使用缓存"""

data = None
DATA_URL_1 = '1'
DATA_URL_2 = '2'


@st.cache_data
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up.
    return data


d1 = fetch_and_clean_data(DATA_URL_1)
# 第一次执行，一个实际执行的函数

d2 = fetch_and_clean_data(DATA_URL_1)
# url与d1相同，使用缓存，不会重复执行

d3 = fetch_and_clean_data(DATA_URL_2)
# 这是不同的url，会执行函数


"""缓存到本地：persist="disk" """
import streamlit as st


@st.cache_data(persist="disk")
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up.
    return data


"""清除缓存： .clear()"""
import streamlit as st


@st.cache_data
def fetch_and_clean_data(_db_connection, num_rows):
    # Fetch data from _db_connection here, and then clean it up.
    return data


fetch_and_clean_data.clear()
# Clear all cached entries for this function.

"""清除所有缓存：st.cache_data.clear"""

import streamlit as st


@st.cache_data
def square(x):
    return x ** 2


@st.cache_data
def cube(x):
    return x ** 3


if st.button("Clear All"):
    # Clear values from *all* all in-memory and on-disk data caches:
    # i.e. clear values from both square and cube
    st.cache_data.clear()

"""在缓存中使用组件："""
api = ''


@st.cache_data
def get_api_data():
    data = api.get(...)
    st.success("Fetched data from API!")  # 👈 Show a success message
    return data


@st.cache_data
def show_data():
    st.header("Data analysis")
    data = api.get(...)
    st.success("Fetched data from API!")
    st.write("Here is a plot of the data:")
    st.line_chart(data)
    st.write("And here is the raw data:")
    st.dataframe(data)


"""全局缓存 st.cache_resource"""
"""例1 普通用法"""
import streamlit as st

session = None
SESSION_URL_1 = '1'
SESSION_URL_2 = '2'


@st.cache_resource
def get_database_session(url):
    # Create a database session object that points to the URL.
    return session


s1 = get_database_session(SESSION_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

s2 = get_database_session(SESSION_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value. This means that now the connection object in s1 is the same as in s2.

s3 = get_database_session(SESSION_URL_2)
# This is a different URL, so the function executes.

"""清除缓存： .clear()"""
"""全局清除： st.cache_resource.clear()"""
