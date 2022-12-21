import pandas as pd
import matplotlib.pyplot as plt

#한글폰트 깨짐처리
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#데이터 불러오기
file1=pd.read_excel("녹지데이터전처리.xls",sheet_name="Sheet2")
file2=pd.read_excel("미세먼지전처리.xlsx",sheet_name="Sheet2")

green = pd.DataFrame(file1)
fog=pd.DataFrame(file2)


#Plot 변환
green.plot.bar(x='자치구명', y='녹지면적총합', rot=0)
fog.plot.bar(x='자치구명', y='7,8월 평균', rot=0,)

# 생성된 Plot 출력
plt.show()
