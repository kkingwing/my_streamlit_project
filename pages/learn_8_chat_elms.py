import streamlit as st

"""扩展：可以考虑设置一个LLM聊天程序"""
"""聊天消息容器 st.chat_message"""
"""例1 with 标识："""
import numpy as np

with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

"""例2 直接调用"""
import streamlit as st
import numpy as np

message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))


st.divider()


"""聊天输入组件 st.chat_input，返回：最后一次输入的文本值"""
import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
