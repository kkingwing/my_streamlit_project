import requests
import time
from datetime import datetime
import streamlit as st


def wxrobot(msg):
    # md_content是markdown的格式

    headers = {'Content-Type': 'application/json'}
    params = {'key': '1d7f2f23-9a6f-4bf9-b81e-79801fa1faf7'}
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    json_data = {
        "msgtype": "markdown",
        "markdown": {"content": (f"\n{'-' * 30}\n"
                                 "\n\n"
                                 f"提醒内容：{msg}\n"
                                 f"{now}"
                                 "\n\n"
                                 f"\n{'-' * 30}\n"
                                 )
                     }
    }
    res = requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send', params=params, headers=headers,
                        json=json_data)
    print("推送情况", res.text)


msg = '测试'
# wxrobot(msg)

with st.container(border=True, height=520):
    st.caption('定时通知')
    col1, col2, = st.columns([0.35, 0.35])
    with col1:
        t_day = st.date_input(label='label', value="default_value_today", min_value=None, max_value=None, key=None,
                              help=None,
                              on_change=None, args=None, kwargs=None, format="YYYY/MM/DD", disabled=False,
                              label_visibility="visible")
    with col2:
        t_time = st.time_input("label", value="now", key=None, help=None, on_change=None, args=None, kwargs=None,
                               disabled=False,
                               label_visibility="visible", step=60)

    if t_day and t_time:
        # label_text = t_day + t_time
        str_day = t_day.strftime('%Y-%m-%d')
        str_time = t_time.strftime('%H:%M')
        str_value = str_day + " " + str_time + ":00"
        # msg = '测试内容'
        msg = st.text_area(str_value, value=None, height=None, max_chars=None, key=None, help=None, on_change=None,
                           args=None,
                           kwargs=None,
                           placeholder=None, disabled=False, label_visibility="visible")
        bool_button_click = st.button("确定", key=None, help=None, on_click=None, args=None, kwargs=None,
                                      type="secondary",
                                      disabled=False, use_container_width=False)

        # 若是点击确定
        if bool_button_click:
            # 显示「定时信息」的文本框
            show_msg = str_value + " " + msg
            show_cron_msg = st.text_area(label='定时内容', value=show_msg, height=None, max_chars=None, key=None,
                                         help=None, on_change=None,
                                         args=None,
                                         kwargs=None,
                                         placeholder=None, disabled=True, label_visibility="visible")

            # 获得选择的时间
            time_value = time.strptime(str_value, "%Y-%m-%d %H:%M:%S")
            # 判断时间，发送内容
            while True:
                now = time.localtime()
                if now > time_value:
                    wxrobot(msg)
                    break

# 要解决异步的问题。
