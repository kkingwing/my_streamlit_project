import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide")

today = '今日：' + datetime.now().strftime("%Y-%m-%d")

st.subheader(today)
st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    with st.container(border=True):
        st.write('广告')
        st.divider()
        st.write(f"""
                    1. :red[“**硬广、软文、营销活动**”]（“曝光、心智、转化”）三步骤同步进行的特征明显，协同模式成为主流。
                    2. 从数据上看，:blue[「**节点营销、新品营销、线下营销、联名/跨界营销、明星营销**」]成为核心关键词，数量分布分别达到31.1%、27.6%、20.9%、20.3%、18.7%。  
                    这当中，:red[「**联名、流量代言、多元节点、主题情绪化、AI营销**」]“五大模式”异军突起。
                    """
                 )
        st.divider()
        st.write("""
        思考：  
        1.将「商品广告」打包给第三方做方案的做法已经成熟，:red[软硬广同时做+卖货]的套路。  
        2.广告文案：借流量（联名IP、请明星/KOL/KOC），节日节点做广告，文案场景化，借助AI。
        """)

with col2:
    with st.container(border=True):
        st.write('羊毛')
        st.divider()
        st.write(f"""
                    1.  12.27： 百度地图搜 「打车预言家」，分享一下然后答题，答案是 :red[星空]，**有30打车券**

                    """
                 )
with col3:
    with st.container(border=True):
        st.write('暂无')
        st.divider()
        # st.write(f"""
        #             1. :red[“**硬广、软文、营销活动**”]（“曝光、心智、转化”）三步骤同步进行的特征明显，协同模式成为主流。
        #             2. 从数据上看，:blue[「**节点营销、新品营销、线下营销、联名/跨界营销、明星营销**」]成为核心关键词，数量分布分别达到31.1%、27.6%、20.9%、20.3%、18.7%。这当中，
        #             :red[「**联名、流量代言、多元节点、主题情绪化、AI营销**」]“五大模式”异军突起。
        #             """
        #          )
with col4:
    with st.container(border=True):
        st.write('暂无')
        st.divider()
        # st.write(f"""
        #             1. :red[“**硬广、软文、营销活动**”]（“曝光、心智、转化”）三步骤同步进行的特征明显，协同模式成为主流。
        #             2. 从数据上看，:blue[「**节点营销、新品营销、线下营销、联名/跨界营销、明星营销**」]成为核心关键词，数量分布分别达到31.1%、27.6%、20.9%、20.3%、18.7%。这当中，
        #             :red[「**联名、流量代言、多元节点、主题情绪化、AI营销**」]“五大模式”异军突起。
        #             """
        #          )