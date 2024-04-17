
import streamlit as st
import numpy as np
import random
import time

## name ("user", "assistant", "ai", "human", or str)
# with st.chat_message("user"):  # 显示一个消息框，图标是"user"
#     st.write("Hello 👋")  # 写一条消息

## ————————————————
# with st.chat_message('assistant'):
#     st.write('Hello human')
#     st.bar_chart(np.random.randn(30, 3))

# # with写法理解，等价于：
# msg = st.chat_message('assistant')
# msg.write('Hello human')
# msg.bar_chart(np.random.randn(30, 3))
## with作用可理解为归纳看着方便————————————————


# prompt = st.chat_input("输入一些东西……")
# if prompt:
#     st.write(f'用户的输入：{prompt}')

st.title('Echo Bot')
# 标准「回调函数」的写法
if "messages" not in st.session_state:  # 初始化 键： messages
    st.session_state.messages = []  # 初始化聊天消息列表 ， messages是一个列表，后面用来存消息

## 在应用程序重新运行时显示聊天记录
for message in st.session_state.messages:
    # 这里写with是为了确保回答与角色图标成对出现
    # message['role']是要引用一个字典，role键的值写了user/assistant，用于
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 响应用户输入
prompt = st.chat_input("what's up?")
if prompt:  # 这两行等价于>>> if prompt := st.chat_input("What is up?"):
    # 增加历史消息显示
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 显示用户消息
    with st.chat_message("user"):
        st.markdown(prompt)

    # response = f"Echo: {prompt}"  # 测试回应，这里用不到了
    # 显示回答消息 （with模块的回答消息容器）
    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )

        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            msg_placeholder.markdown(full_response+"|")

        msg_placeholder.markdown(full_response)

    # 增加回答历史记录
    st.session_state.messages.append({'role': 'assistant', 'content': response})
