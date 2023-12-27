import time

"""布局 和 容器"""

"""侧边栏 st.sidebar.[组件] 、 with st.sidebar: """
import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

"""使用st.echo，st.spinner只能用with方法"""
import streamlit as st

with st.sidebar:
    with st.echo():  # 显示当下编写的代码，下方代码将被显示出来。
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):  # 加载等待
        time.sleep(2)
    st.success("Done!")

# 分割线——————————
st.divider()

"""并排列 st.columns，返回容器对象的列表"""
# 1.调用方法: 1 首选with, 2 使用对象方法 col_x.[组件]
# 2.st.columns(spec, *, gap="small")
# spec:
# 用于指定列数及宽度, 如果是一个数字,则宽度相同;
# 如果是几个小数,代列宽度分布如 [0.7,0.3]
# 如果是一个列表,则按倍数拆分如[1,2,3]
# gap:列的间隙, 默认small,可选medium\large
#
"""例1，with调用"""
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

"""例2 对象直接调用"""
import streamlit as st
import numpy as np

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader('A wide column with chart')
col1.line_chart(data)

col2.subheader('a narrow column with data')
col2.write(data)

# 分割线——————————
st.divider()

"""导航标签 st.tabs，返回容器对象的列表"""
import streamlit as st

# st.tabs接受字符串或是列表，每个元素都将被分成独立的标签。
# 可以使用「with的方式」 或是 「对象直接调用」
"""例1 ，with调用"""
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

"""例2 对象直接调用"""
import streamlit as st
import numpy as np

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)

# 分割线——————————
st.divider()

"""插入一个可以展开/折叠的多元素容器 st.expander，无返回"""
# st.expander(label, expanded=False)
# label：提示标签
# expanded：默认为False，折叠状态，即默认只能看到「提示label」

"""例1 with写法"""
import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")

"""例2 调用写法"""
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
expander = st.expander("See explanation")
expander.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
expander.image("https://static.streamlit.io/examples/dice.jpg")

# 分割线——————————
st.divider()

"""插入一个容纳多元素的容器 st.container，无返回"""
"""例1 with写法"""
import streamlit as st

with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

"""例2 容器内的写法不在于先后，在于调用"""
import streamlit as st

container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

# Now insert some more in the container
container.write("This is inside too")

# 分割线——————————
st.divider()

"""单元素容器 st.empty，无返回"""
# 使用单元素方便管理
import streamlit as st
import time

with st.empty():
    for seconds in range(2):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 1 minute over!")

"""例2 便于清除"""
import streamlit as st

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")

# Clear all those elements:
placeholder.empty()