# 模块名称：v1a_agg_information_api.py
# 作者：清易
# 版本：v1a  创建日期：2024-04-07  作用：采集各个平台热搜榜信息，进行处理，定时于linux采集
# 热榜信息聚合

import requests
import time
import pandas as pd
import urllib.parse
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()  # 解决报错：no  No module named 'MySQLdb'


def caesar_encrypt(text: str, shift: int,
                   alphabet: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:/?.@=") -> str:
    """加密明文"""
    cipher_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            cipher_text += alphabet[new_index]
        else:
            cipher_text += char
    # print('cipher_text:', cipher_text)
    return cipher_text


# 加密，使用「结果字符串」反编译来使用，隐藏明文。（阿里ECS，这里要写为mb4以支持emoji）
encry_con = caesar_encrypt("wICAveffByyDerEkxAvE:/?.i.dhdch/?:h??:e..:afCzsnoBgmrkBCoDjEDpcwl@", -10)
CON = create_engine(encry_con)


def zhihu_hotlist():
    """知乎热榜 api 接口，记录于数据库"""
    api_url = r'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total'
    plat_name = '知乎'
    res = requests.get(
        url=api_url,
        params={'limit': '50', 'desktop': 'true', },
    )
    items = res.json()['data']
    ls = []
    for top_item in items:
        ds = {}
        ds['平台'] = plat_name
        ds['标题'] = top_item['target']['title']
        ds['url'] = top_item['target']['url'].replace('https://api.zhihu.com/questions/',
                                                      'https://www.zhihu.com/question/')
        ds['热度'] = top_item['detail_text']
        ds['时间'] = time.strftime("%Y-%m-%d", time.localtime(top_item['target']['created']))
        ds['记录日期'] = time.strftime("%Y-%m-%d", time.localtime())
        print(ds)
        ls.append(ds)
    df = pd.DataFrame(ls)
    pd.io.sql.to_sql(df, 'aggregate_hot_list', con=CON, if_exists='append', index=False)
    print(f'{plat_name}写入数据库完成，预览\n{df.head()}')


def weibo_hotlist():
    """知乎热榜 api 接口，记录于数据库"""
    api_url = 'https://weibo.com/ajax/side/hotSearch'
    plat_name = '微博'
    res = requests.get(url=api_url)
    datas = res.json()['data']
    ls = []
    print(datas)
    top_items = datas['hotgovs']
    for top_item in top_items:
        ds = {}
        ds['平台'] = plat_name
        word = top_item['word']
        ds['标题'] = word
        ds['url'] = f'https://s.weibo.com/weibo?q=' + urllib.parse.quote(word)
        ds['热度'] = '置顶'
        ds['时间'] = time.strftime("%Y-%m-%d", time.localtime(top_item['stime']))
        ds['记录日期'] = time.strftime("%Y-%m-%d", time.localtime())
        print(ds)
        ls.append(ds)

    realtime_items = datas['realtime']
    for realtime_item in realtime_items:
        try:
            ds = {}
            ds['平台'] = plat_name
            word = realtime_item['word_scheme']
            ds['标题'] = word
            ds['url'] = f'https://s.weibo.com/weibo?q=' + urllib.parse.quote(word)
            ds['热度'] = realtime_item['num']
            ds['时间'] = time.strftime("%Y-%m-%d", time.localtime(realtime_item['onboard_time']))
            ds['记录日期'] = time.strftime("%Y-%m-%d", time.localtime())
            print(ds)
            ls.append(ds)
        except:
            pass
    df = pd.DataFrame(ls)
    pd.io.sql.to_sql(df, 'aggregate_hot_list', con=CON, if_exists='append', index=False)
    print(f'{plat_name}写入数据库完成，预览\n{len(df)}\n{df.head()}')
    return df


def baidu_hotlist():
    plat_name = '百度'
    api_url = 'https://top.baidu.com/board'
    params = {
        'tab': 'realtime',
    }
    res = requests.get(api_url, params=params)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(res.text, 'lxml')
    items = soup.select('.category-wrap_iQLoo.horizontal_1eKyQ')
    ls = []
    for item in items:
        ds = {}
        ds['平台'] = '百度'
        ds['标题'] = item.select('.c-single-text-ellipsis')[0].text.strip()
        ds['url'] = item.select('.content_1YWBm a')[0]['href']
        ds['热度'] = item.select('.hot-index_1Bl1a')[0].text
        ds['时间'] = time.strftime("%Y-%m-%d", time.localtime())
        ds['记录日期'] = time.strftime("%Y-%m-%d", time.localtime())
        print(ds)
        ls.append(ds)
    df = pd.DataFrame(ls)
    pd.io.sql.to_sql(df, 'aggregate_hot_list', con=CON, if_exists='append', index=False)
    print(f'{plat_name}写入数据库完成，预览\n{df.head()}')


def ithome_hotlist():
    plat_name = 'IT之家'
    api_url = 'https://www.ithome.com/'
    res = requests.get(api_url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    items = soup.select('#rank #d-1 li')
    ls = []
    for item in items:
        ds = {}
        ds['平台'] = 'IT之家'
        ds['标题'] = item.select('a')[0].text.strip()
        ds['url'] = item.select('a')[0]['href']
        ds['热度'] = 2000000  # 网站无公开热度，默认赋值200万热度
        ds['时间'] = time.strftime("%Y-%m-%d", time.localtime())
        ds['记录日期'] = time.strftime("%Y-%m-%d", time.localtime())
        print(ds)
        ls.append(ds)
    df = pd.DataFrame(ls)
    pd.io.sql.to_sql(df, 'aggregate_hot_list', con=CON, if_exists='append', index=False)
    print(f'{plat_name}写入数据库完成，预览\n{df.head()}')


# 去重
def clean_sql():
    # 读取记录于sql今日已处理的头条资讯
    print('读取数据并去重：开始……')
    sql = 'SELECT * FROM `aggregate_hot_list`'
    df = pd.read_sql(sql=sql, con=CON)  # 读取sql，获取内容。
    # ===处理热度为数字，进行排序，因定时抓取，需要进行热度排序
    ## 去「置顶」、「万热度」、将字符串转浮点再转整数
    df['热度'] = df['热度'].apply(lambda x: x.replace('置顶', '99999999') if '置顶' in x else x)
    df['热度'] = df['热度'].apply(lambda x: x.replace(' 万热度', '0000') if '万' in x else x)
    df['热度'] = df['热度'].astype(float).astype(int)
    # ===
    df.sort_values(by=['记录日期', '热度', '平台'], ascending=[False, False, False], inplace=True)
    df.drop_duplicates(subset=['平台', 'url'], keep='first', inplace=True)  # 去重
    df['热度'] = df['热度'].astype(str)  # 需要以文本的格式存诸，新内容是文本。
    pd.io.sql.to_sql(df, 'aggregate_hot_list', con=CON, if_exists='replace', index=False)
    print('数据去重完成。')


def run():
    zhihu_hotlist()
    weibo_hotlist()
    baidu_hotlist()
    ithome_hotlist()
    clean_sql()


run()

# baidu_hotlist()
# do 定时抓取，30min，已定时于linux，每30分钟抓取一次。
