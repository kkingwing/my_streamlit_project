import pandas as pd

path = r'D:\Code\my_streamlit_project\scripts\测试样表.xlsx'
df = pd.read_excel(path,sheet_name='环比')
df.to_excel('./scripts/生成表.xlsx')
print('已运行.')