import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from setup import setup_environment

merged_df = setup_environment()
#---------------------------------------------------------------------------------------前處理
merged_df['受傷人數'] = pd.to_numeric(merged_df['受傷人數'],errors ='coerce')
injury_counts_by_place = merged_df.groupby('地址類型名稱')['受傷人數'].sum()
av = injury_counts_by_place.mean()
#---------------------------------------------------------------------------------------以地址為類別進行受傷人數的加總
plt.figure(figsize = (10, 6))
#---------------------------------------------------------------------------------------建立圖表
color = {
    '一般地址': (0.73, 1.0, 1.0, 1.0),   # 浅蓝色
    '交叉路口': (0.68, 0.93, 0.93, 1.0),  # 天蓝色
    '其他': (0.59, 0.80, 0.80, 1.0),  # 青色
    '無': (0.565, 0.933, 0.565),  #深綠色
}
#---------------------------------------------------------------------------------------給予顏色(<1)
bars = plt.bar(injury_counts_by_place.index, injury_counts_by_place.values, color=[tuple(color.get(name, (128, 128, 128))) for name in injury_counts_by_place.index]) # type: ignore
#---------------------------------------------------------------------------------------繪製長條圖
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height()))
             ,ha = 'center',va ='bottom',fontsize = 10)
#---------------------------------------------------------------------------------------貼上標籤
plt.axhline(y=av, color='red', linestyle='--', label='平均值')
plt.text(len(injury_counts_by_place.index)-2, av +1000,f'平均值:{av:.0f}',fontsize =10, ha ='center',va = 'bottom',color ='red')
#---------------------------------------------------------------------------------------標上平均值
plt.xticks(fontsize=10,rotation=45 ,ha ='right')
plt.yticks(fontsize=10)
plt.xlabel('地理類型名稱')
plt.ylabel('受傷人數')
plt.title('地理類型名稱與受傷人數關聯長條圖')
#---------------------------------------------------------------------------------------補上軸標籤
plt.legend()
plt.savefig('地理類型名稱與受傷人數關聯長條圖.png')
plt.show()

