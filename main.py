
import folium as g
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc

font_path="korean.ttf" #그래프에서 한글 오류가 안나게 하는 폰트 설치
font_name=font_manager.FontProperties(fname=font_path).get_name() #폰트 한글 오류 안나게함
rc('font',family=font_name)
plt.figure(figsize=(8,8)) # 그래프의 사이즈 조절
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


by_accident_graph = pd.read_csv("by_accident_graph.csv",encoding='cp949') # 그래프를 위해 새로 정리해서 만든 csv
by_accident_graph.plot(kind='bar', x='사고유형',y='발생건수',color ='blue')
plt.show()

by_violation_graph = pd.read_csv("by_violation_graph.csv",encoding='cp949') # 그래프를 위해 새로 정리해서 만든 csv
by_violation_graph.plot(kind='bar', x='위반유형',y='발생건수',color ='green')
plt.show()

by_road_graph = pd.read_csv("by_road_graph.csv",encoding='cp949') # 그래프를 위해 새로 정리해서 만든 csv
by_road_graph.plot(kind='line', x='도로형태',y='발생건수',color ='red')
plt.show()
print("----------------------------------------------------------------")

By__type__of__violation = pd.read_csv("By__type__of__violation.csv",encoding='cp949')
By__type__of__violation.dtypes #
print(By__type__of__violation)
print("----------------------------------------------------------------")
print(By__type__of__violation.sort_values(by=['발생건수'],ascending=False).head(1))
      # 내림차순을 이용해서 최댓값을 출력

# 도로 형태별 교통사고 통계
print("----------------------------------------------------------------")
By__road__type= pd.read_csv("By__road__type.csv",encoding='cp949')
By__road__type.dtypes
print("발생 건수가 많은 순서대로") #발생건수가 큰 순서대로
print(By__road__type.sort_values(by=['발생건수'],ascending=False).head(11))

# 사고 유형별 교통사고 통계
print("----------------------------------------------------------------")
By__accident__type = pd.read_csv("By__accident__type.csv",encoding='cp949')
By__accident__type.dtypes
print("발생 건수가 적은 순서대로") #발생건수가 작은 순서대로
print(By__accident__type.sort_values(by=['발생건수'],ascending=True).head(18))

# 위반 유형별 교통사고 통계
print("----------------------------------------------------------------")
data = pd.read_excel('sec.xlsx') #csv파일이 아닌 excel 파일일때 통계를 불러옴
data.columns = ['위반유형','발생건수','대형사고','여객(건)','화물(건)','사망자수','치사율(%)']
data=data.iloc[2:, :]
print(data.head(11))
data_ac = data.sort_values(by=["발생건수"], ascending=False)
plt.figure(figsize=(5,3))
plt.title("발생건수")
sns.barplot(x="대형사고",y="발생건수",data=data_ac)
#위반 유형에 따른 발생 건수    # excel통계를 그래프로 표현
plt.show()


danger_zone_df=pd.read_excel('my map.xlsx')
danger_zone_df.head()

g_map = g.Map(location=[36.631226, 127.458044],tiles='Stamen terrain',zoom_start=12)
for i in range(len(danger_zone_df)):
    marker01=g.Marker([danger_zone_df.loc[i]['x'],danger_zone_df.loc[i]['y']],
               icon = g.Icon(color='red'))
    marker01.add_to(g_map)

print("----------------------------------------------------------------")
danger= pd.read_csv("danger.csv",encoding='cp949')
# 청주 사고 다발 지역 순서 통계
danger.dtypes
print("발생 건수가 많은 순서대로") #발생건수가 큰 순서대로
print(danger.sort_values(by=['발생건수'],ascending=False).head(216))


g_map.save('사고 다발 지역.html') #구글맵에 내 맵을 저장하고 열 수 있는 파일 생성


