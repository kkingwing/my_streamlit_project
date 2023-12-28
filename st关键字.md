

# strealmit关键字：
```
import streamlit as st

常用命令：
1.万能输入
   st .write()

2.文本输入
   st.title()
   st.subheader()
   st.write()
   st.markdown
   st.code()
   st.caption
   st.divider

3.数据表格框输入
   st.dataframe(help' :'','format':'', 'url': st.column_config.……)'
   st.data_editor()
      字段字典参数：st.column_config.
         .Column()
         .TextColumn()
         .NumberColumn()
         .CheckboxColumn()
         .SelectboxColumn()
         .DatatimeColumn()
         .DateColumn()
         .TimeColumn()
         .ListColumn()
         .LinkColumn()
         .ImageColumn()
         .LineChartColumn()
         .BarChartColumn()
         .ProgressColumn()


4.常用图表
   st.area_chart
   st.bar_chart
   st.line_chart
   st.scatter_chart
   st.pyplot
   st.altair_chart
   st.map

   st.plotly_chart  # python库，交互式图表库 √ （使用这个）
   st.bokeh_chart # python库，交互式图表库
   （应用场景区别：重点是构建交互式Web应用程序，Bokeh 可能更适合。若主要关注数据科学和分析，Plotly 可能是更好的选择。）
   （图不是重要，表达的「分析点」是重点。）


5.组件
   st.button
   st.download_button
   st.link_button
   st.checkbox
   st.toggle
   st.radio

   st.selectbox
   st.multiselect

   st.slider
   st.select_slider

   st.text_input
   st.number_input
   st.text_area

   st.date_input
   st.time_input

   st.file_uploader
   st.camera_input
   st.color_picker

   st.echo # 显示当下代码
   st.spinner # 加载等待

6.嵌入多媒体（图像、音频、视频）
   st.image
   st.audio
   st.vedio

7.布局、容器   以下皆可以「通过with xxx: 调用」或「通过容器对象调用」（通过with将一系列具有前后关系的组件组在一起。）

   st.siderbar.selectbox
   st.columns
   st.tabs
   st.expander
   st.container
   st.empty

8.聊天元素
   st.chat_message
   st.chat_input

9.状态显示
   st.progress
   st.spinner
   st.status
   st.toast
   st.balloons
   st.snow
   st.error
   st.warning
   st.info
   st.success
   st.excption

10.控制流
   st.stop
   st.rerun
   st.form
   st.form_submit_button
   

11.工具
   st.set_page_config
   st.echo
   se.help


12.st会话管理（「键值」与「回调（diao）函数」）
   st.session_state.key = 'value'   # 添加， 或写为 st.session_state['key'] = 'value' 也可以。
   del st.session_state['key']  # 删除

   for key in st.session_state.keys(): # 清空
      del st.session_state[key]


13.性能优化 - 缓存
   @st.cache_data
   @st.cache_resource
   xx.clear()
   st.cache_data.clear()
   st.cache_resource.clear()


14.数据库连接- 调取数据
   st.connection
   .streamlit/secrets.toml  （新建.文件夹，文件，配置见详情文档）



15.云布署
1.数据库安全，需要隐藏设置；
2.app依赖：需要下载的库要放在「requirements.txt」，可以不写版本号，也可以指定。
3.安全管理：敏感信息可以放在一个文件中，并当作环境变量传入。
   - 云部署中，在「Settings - Secrets」中添加「.toml」格式的设置代码即可。
   - 「.gitignore」要忽略掉该文件。

   > 解决bug：
      > # .streamlit/secrets.toml
      [connections.mydb] #定义「mydb」为连接的模块名
      dialect = "mysql" # 类型
      driver = "pymysql" # 解决streamlit安装mysqlclient报错的问题，同时要requirement要安装为pymysql
      username = "root" # 账号
      password = "huanqlu0123" # 密码
      host = "39.98.120.220" # 地址
      database = "spider" # 数据库
      port = "3306" #端口
      type = "sql" # 有些会用到，这里指定不变即可

   > 云布署已解决数据库设置为环境变量的安全问题。
   * 7天没有流量访问的app陷入休眠，平时注意访问即可。
   * 访客匿名。
4.分享
   1.「公开/私人」应用的更改，直接改「设置-分享」即可。
   2.私有app的分享可以通过创建链接的方式邀请查看。也可以添加一些邮箱的方式。（若对方无邮件，可考虑创建一些邮箱来提供访问）
（详见文档https://docs.streamlit.io/streamlit-community-cloud/share-your-app）
5.SEO网格搜索：应用是公开的，写子域名，写程序元标题，


*以上皆为招式，心法为用法。


*可扩展 ：
LLM聊天程序  
   -  GPT的api调用超时，测出结果为：无api免费额度，测试注册，api可用。 
   - 后若程序不可行，需要另再注册一个账号，另建一个api即可。目前gpt注册不需要验证，但创建api需要验证，方法与之前相差不大。） 
   - 要成功访问，仍然需要开「全局的vpn」，否则访问失败。 —— 测试部署到st是否可不用梯子 —— 是的，可以。
第三方插件
案例 - App Gallery (案例库作用不大，需要先手动设计)
测试（文档 - 暂略）
自定义组件（文档 - 暂略）
30天教程
```