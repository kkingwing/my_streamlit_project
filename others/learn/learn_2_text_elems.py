# 常用：
# 主标题： st.title
# 子标题： st.subheader
# 万能输入: st.write
# md语法： st.markdown
# 代码框：st.code
# 注释：st.caption
# 分隔线：st.divider



# markdown语法：st.markdown
import streamlit as st

st.markdown("**st.markdown：以下这块是markdown语法**")
st.markdown('''着色[中括号内写颜色如red]：
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''结尾写两个空格，就会「软换行」,  


两个或多个换行符会「硬换行」.
'''
st.markdown(multi)

# 文本框:st.text_area
md = st.text_area('md的文本框st.text_area',
                  "Happy Streamlit-ing! :balloon:")
# 代码框
st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")
st.markdown(md)

# 二级标题：st.header
import streamlit as st

# 分隔线：divider这里是彩虹条
st.header('这是st.header的主标题及分隔线', divider='rainbow')
# 着色使用[]，支持普通颜色以及彩虹，rainbow
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

# 子标题：st.subheader
import streamlit as st

st.subheader('这是st.subheader的子标题及分隔线', divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

# 注释：st.caption
import streamlit as st

st.caption('这是st.caption的注释写法：This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# 代码块：st.code
import streamlit as st

code = '''# 代码块st.code，会简单进行代码之间的相对缩进识别
def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')  # 默认的即为python

# 普通文本:st.text
import streamlit as st

st.text('本行是普通文本st.text的显示')

# 数学表达式：st.latex
import streamlit as st

st.latex(r'''数学表达式st.latex：
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# 分隔线 st.divider
import streamlit as st
st.write('下面这行是「分隔线」')

st.divider()
import streamlit as st

st.write("下面是「分隔线」的组合分隔用法")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule