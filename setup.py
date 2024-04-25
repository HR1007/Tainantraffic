import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
from sklearn.linear_model import LinearRegression
from matplotlib.font_manager import fontManager
import requests

def setup_environment():
 url = "https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_"
 response = requests.get(url)

 with open('TaipeiSansTCBeta-Regular.ttf', 'wb') as file:
    file.write(response.content)

 fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
 mpl.rc('font', family='Taipei Sans TC Beta')

 excel_file_0 =r'C:\Users\harry\OneDrive - 國立高雄科技大學\桌面\digi\使用資料\臺南市111年上半年道路交通事故原因傷亡統計.xlsx'
 excel_file_1 =r'C:\Users\harry\OneDrive - 國立高雄科技大學\桌面\digi\使用資料\臺南市111年下半年道路交通事故原因傷亡統計.xlsx'

 df_0 = pd.read_excel(excel_file_0)
 df_1 = pd.read_excel(excel_file_1)

 merged_df = pd.concat([df_0,df_1])
 print(merged_df)
 
 return merged_df

