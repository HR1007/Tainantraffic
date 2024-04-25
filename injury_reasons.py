import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from setup import setup_environment

merged_df = setup_environment()
#-------------------------------------------------------------------------導入環境
cause_count = merged_df['肇因研判子類別名稱-主要'].value_counts()
cause_count_filtered = cause_count[cause_count >= 2000]#定義條件
pd.to_numeric(cause_count_filtered,errors ='coerce')
#-------------------------------------------------------------------------資料前處理
plt.figure(figsize=(10, 6))#圖形大小
#-------------------------------------------------------------------------設置圖形
color_mapping = {
    '未依規定讓車': (0.73, 1.0, 1.0, 1.0),   # 浅蓝色
    '未注意車前狀態': (0.68, 0.93, 0.93, 1.0),  # 天蓝色
    '違反號誌管制或指揮': (0.59, 0.80, 0.80, 1.0),  # 青色
    '其他引起事故之違規或不當行為': (0.565, 0.933, 0.565),  #深綠色
    '未保持行車安全距離': (0.463, 0.933, 0.776),  # 薄荷色
    '左轉彎未依規定': (0.745, 0.745, 0.745)  # 灰色
}
#-------------------------------------------------------------------------給予顏色
bars = plt.bar(cause_count_filtered.index, cause_count_filtered.to_numpy(),color=[tuple(color_mapping.get(name,(128,128,128))) for name in cause_count_filtered.index])#圖形樣式
#-------------------------------------------------------------------------建立圖形
for bar in bars:
    plt.text(bar.get_x()+ bar.get_width() / 2, bar.get_height() , str(int(bar.get_height())), fontsize = 10,
         ha ='center', va ='bottom',  color ='black' )
#-------------------------------------------------------------------------給予標籤
av = cause_count_filtered.mean()
plt.axhline(y = av, color='red', linestyle='--', label='平均值')
plt.text(len(cause_count_filtered)-2,av + 500 ,f'平均值:{av:.2f}',ha='center',va='bottom',fontsize=10 ,color ='red') #x,y,對齊,格式
#-------------------------------------------------------------------------計算平均值
plt.xticks(fontsize=10, rotation=45, ha='right')
plt.yticks(fontsize=10)
plt.xlabel('肇因研判子類別名稱-主要')
plt.ylabel('計數')
plt.title('案件類別統計')
#-------------------------------------------------------------------------補上標籤
plt.legend()
plt.savefig('案件類別統計.png')
plt.show()