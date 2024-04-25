import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from setup import setup_environment

merged_df = setup_environment()

injery_weather = merged_df.groupby('天候名稱',as_index= False)['案件編號'].count()
#---------------------------------------------------------------------------------------以天氣為類別進行案件編號的加總
selected_weather = ['晴','陰','雨']
#---------------------------------------------------------------------------------------選擇範圍
selected_data = injery_weather[injery_weather['天候名稱'].isin(selected_weather)].copy() # type: ignore
average_value = selected_data['案件編號'].mean()
#---------------------------------------------------------------------------------------建立副本並計算平均值
plt.figure(figsize=(10,6))
#---------------------------------------------------------------------------------------建立圖表
color_1 = {
    '晴': (0.73, 1.0, 1.0, 1.0),   # 浅蓝色
    '陰': (0.68, 0.93, 0.83, 1.0),  # 天蓝色
    '雨': (0.59, 0.80, 0.80, 1.0),  # 青色
 }

bars = plt.bar(selected_data['天候名稱'],selected_data['案件編號'], color = [tuple(color_1.get(name,(128,128,128)))for name in selected_data['天候名稱']])
#---------------------------------------------------------------------------------------以選完範圍為基礎建立長條圖
for bar in bars:
   plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())),
        ha='center', va='bottom', fontsize=10)
#---------------------------------------------------------------------------------------放上標籤
plt.axhline(y=average_value, color='red', linestyle='--', label='平均值')
plt.text(len(selected_data)-2,average_value +1000 ,f'平均值:{average_value:.0f}',ha='center',va='bottom',fontsize=10 ,color ='red') #x,y,對齊,格式
#---------------------------------------------------------------------------------------建立平均線
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('天候名稱')
plt.ylabel('案件數量')
plt.title('不同天氣下的案件數量')
#---------------------------------------------------------------------------------------補上軸標籤
plt.legend()
plt.savefig('不同天氣下的案件數量.png')
plt.show()