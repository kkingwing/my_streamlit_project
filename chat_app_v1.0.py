# 名称：chat_app_v1.0.py
# 作用：不使用梯子而访问GPT。
# 本模块：1、需要gpt-api有额度，2、需要开全局。 若本地访问不开全局vpn，会访问超时。
# 已布署至「streamlit分享」，可以不使用梯子而进行访问分享链。

import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# 调用配置文件的openai的key # 在toml中需要写一个[openai再调用，否则会识别到另一个前面设置过的[]sql中
client = OpenAI(api_key=st.secrets.openai.OPENAI_API_KEY)

# 设置模型 (标准回调函数写法，如无键，设置键）
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# 标准「回调函数」的写法，初始化历史聊天记录
if "messages" not in st.session_state:  # 初始化 键： messages
    st.session_state.messages = []  # 初始化聊天消息列表 ， messages是一个列表，后面用来存消息

# 显示历史聊天记录
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 接受用户输入
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})  # 增加历史消息显示
    with st.chat_message("user"):
        st.markdown(prompt)

    # 显示回答消息 （with模块的回答消息容器）
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})