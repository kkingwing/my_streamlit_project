import streamlit as st

"""嵌入图片：st.image，无返回"""
st.image('images/flower.png',
         caption='sun shines follow you heart.',
         width=120,  # 指定宽度
         )


"""嵌入音频：st.autio，无返回"""
import streamlit as st
import numpy as np

audio_file = open('images/测试音频.oga', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)


"""嵌入视频：st.video，无返回"""
import streamlit as st

video_file = open('iamges/myvideo.mp4', 'rb') # 该文件不存在，若存在改相应地址即可
video_bytes = video_file.read()

st.video(video_bytes)