import streamlit as st
import os
from time import sleep

# 设置页面配置
st.set_page_config(page_title="图片流动", page_icon="📸")

tab1, tab2 = st.tabs(['图像变动', '滑动'])

with  tab1:
    # 定义图片文件夹路径
    image_folder = "images"

    # 获取文件夹中的所有PNG图片
    image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]

    # 图片自动流动的间隔时间（秒）
    interval_seconds = 2

    # 创建空白容器
    image_index = st.empty()

    # 无限循环，实现图片自动流动
    while True:
        # 循环显示图片
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            image_index.image(image_path, caption=f"图片: {image_file}", use_column_width=True)
            sleep(interval_seconds)


with tab2:
    pass