import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from setup import setup_environment

merged_df = setup_environment()
#-------------------------------------------------------------------------導入環境
merged_df['受傷人數'] = pd.to_numeric(merged_df['受傷人數'], errors='coerce')#清除空值
merged_df['發生日期'] = pd.to_datetime(merged_df['發生日期'])#定義時間格式
merged_df.set_index('發生日期', inplace=True)
#-------------------------------------------------------------------------資料前處理
injury_counts_by_month = merged_df.resample('M')['受傷人數'].sum()
injury = injury_counts_by_month
#-------------------------------------------------------------------------以月為類別統計受傷人數
plt.figure(figsize=(15, 10))
#-------------------------------------------------------------------------製作圖表
injury.plot(kind='line', color='blue', marker='o', label='受傷人數')
plt.fill_between(injury.index, injury, color='lightblue', alpha=0.3)##添加陰影
#-------------------------------------------------------------------------建立曲線
for i, value in enumerate(injury):
    plt.text(injury.index[i], value, '{:.0f}'.format(value), ha='center', va='bottom', color='black', fontsize=10)
#-------------------------------------------------------------------------放上標籤
plt.xticks(fontsize=10, rotation=45, ha='right')
plt.yticks(fontsize=10)
plt.xlabel('發生月份')
plt.ylabel('計數')
plt.title('受傷人數趨勢')
#-------------------------------------------------------------------------補上軸標籤
plt.legend()
plt.savefig('111年台南市交通事故受傷人數趨勢(月份)')
plt.show()