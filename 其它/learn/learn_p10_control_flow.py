import streamlit as st
"""控制执行流程"""

"""改变执行：st.stop()  st.rerun()"""

"""停止执行 st.stop()"""
import streamlit as st

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  # st.stop()
st.success('Thank you for inputting a name.')

# 分割线————————————
st.divider()

"""组件分组，成批传输 st.form"""

import streamlit as st
# 必须有个提交按钮： st.form_submit_button(Submit)，
# 当提交时，所有互动的结果值一并发给st
# （st.button,st_download_button不能添加到st.form）
# form可以出现在slider或是column，但不是嵌入另一个form中。

"""例1 with写法"""
with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

"""例2 对象调用，乱序写法"""
import streamlit as st

form = st.form("my_form2")
form.slider("Inside the form")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")


# 分割线————————————
st.divider()


"""重新运行 st.rerun """
"""例1 更新标题："""
import streamlit as st

if "value" not in st.session_state:
    st.session_state.value = "Title"

##### Option using st.rerun #####
st.header(st.session_state.value)

if st.button("Foo"):
    st.session_state.value = "Foo"
    st.rerun()

"""例2 使用callback"""
##### Option using a callback #####
st.header(st.session_state.value)

def update_value():
    st.session_state.value = "Bar"

st.button("Bar", on_click=update_value)

"""例3 使用container"""
##### Option using a container #####
container = st.container()

if st.button("Baz"):
    st.session_state.value = "Baz"

container.header(st.session_state.value)