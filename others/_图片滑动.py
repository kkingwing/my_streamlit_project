import streamlit as st
import os
from PIL import Image
from time import sleep

# 设置页面配置
st.set_page_config(page_title="图片流动", page_icon="📸")

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

        # 打开图片并调整宽度
        image = Image.open(image_path)
        resized_image = image.resize((100, int(100 / image.width * image.height)), Image.LANCZOS)

        # 使用HTML和CSS实现动画效果
        st.markdown(
            f"""
            <style>
                @keyframes slide-up {{
                    from {{
                        transform: translateY(100%);
                    }}
                    to {{
                        transform: translateY(0);
                    }}
                }}
                .custom-container {{
                    animation: slide-up 2s ease-out;
                }}
            </style>
            """,
            unsafe_allow_html=True
        )

        # 在每次图片显示后等待一定时间
        with st.container():
            st.image(
                resized_image,
                caption=f"图片: {image_file}",
                use_column_width=True,
                format='PNG',
                unsafe_allow_html=True,
                key='animated_image'
            )

        sleep(interval_seconds)
