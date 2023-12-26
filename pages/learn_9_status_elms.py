# 进程状态的显示
import streamlit as st

st.subheader("""显示进度与状态的「动画」，如「进度条，警告弹框，庆祝气球""")

"""进度条 st.progress"""
import streamlit as st
import time

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(20):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)

my_bar.empty()  # 删除元素，此处的功能是加载完毕时，使进度条消失

st.button("Rerun")

st.divider()

"""加载等待 st.spinner"""
import time
import streamlit as st

with st.spinner('Wait for it...'):
    time.sleep(2)
    time.sleep(2)
st.success('Done!')

st.divider()

"""设置一个长时间运行的加载状态容器： st.status"""
import time
import streamlit as st

with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button('Rerun!')

"""例2 状态列表显示更新，显示过程 .update()更新「显示标签、状态或是扩展」"""
import time
import streamlit as st

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Download complete!", state="complete", expanded=False)

st.button('Rerun3')

st.divider()

"""便浮窗 st.toast，短暂的显示非干扰性消息，于右下角显示4秒"""
"""例1，简单用法"""
import streamlit as st

st.toast('Your edited image was saved!', icon='😍')

"""例2：多个浮窗，点击后排行显示"""
import streamlit as st
import time

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)  # 这里是0.5s
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')

"""例3 同条浮窗提示内容变化。"""
import streamlit as st
import time

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")

if st.button('Cook breakfast'):
    cook_breakfast()

st.divider()

"""庆祝 - 气球动画 st.balloons"""
import streamlit as st

st.balloons()

"""庆祝 - 降雪动画  st.snow"""
import streamlit as st

st.snow()


"""错误提示 st.error"""
import streamlit as st

st.error('This is an error', icon="🚨")

"""警告提示 st.warning"""
import streamlit as st

st.warning('This is a warning', icon="⚠️")

"""信息提示 st.info"""
import streamlit as st

st.info('This is a purely informational message', icon="ℹ️")

"""成功提示 st.success"""
import streamlit as st

st.success('This is a success message!', icon="✅")

"""异常提示 st.exception"""
import streamlit as st

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)