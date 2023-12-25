## 本目录下的模块用于存放各执行肢本

import streamlit as st
import subprocess
import os

# 定义执行脚本 - 调度爬虫

def run_0():
    script_path = r'D:\Code\my_streamlit_project\scripts\main_schedule_test.py'
    subprocess.run(['python', script_path], check=False, capture_output=True)




def run_1():
    script_path = r'D:\Code\My_project\AutoWork\运营排行榜\main.py'
    result = subprocess.run(['python', script_path], check=False, capture_output=True)
    if result.returncode != 0:
        try:
            error_message = result.stderr.decode('utf-8')
        except UnicodeDecodeError:
            error_message = result.stderr.decode('gbk')
        st.error(f"脚本执行错误：{error_message}")
        st.error(f"返回代码：{result.returncode}")
    else:
        st.success("脚本成功执行！")
