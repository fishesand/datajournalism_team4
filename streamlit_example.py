import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(layout="wide")

# Webpage Title
st.title("정신건강, 수도권만의 권리인가요?")

st.info(
"""
우리나라 국민의 1/3은 '중간 수준 이상의 우울감'을 경험하고 있다.
그럼에도, 우리 사회에서 정신건강은 늘 뒷전이다. 지방, 농어촌 지역의 정신건강은 더더욱 뒷전이다. 점점 흔해지는 우울과 불안에 대응할 적절한 인프라가 갖추어져 있는지, 아무도 관심을 갖지 않는다.
본 프로젝트의 목표는 정신건강증진시설의 지역격차를 시각화하는 것이다. 

"""
)

st.header("I. 정신건강증진시설의 지역격차")

st.write("Streamlit은 데이터분석 결과를 가장 빠르게 웹기반 리포트를 작성하고 공유할 수 있는 플랫폼이다.")
st.write("간단한 파이썬 코드를 이용해 데이터기반 홈페이지를 손쉽게 만들 수 있다. 현재 깃허브(github)에서 가장 인기있는 프로젝트중 하나이며 정보시각화(visualization)을 손쉽게 포함시킬 수 있다.")

st.info(
"""
참고자료
* API Document: https://docs.streamlit.io/library/api-reference
* Examples: https://github.com/MarcSkovMadsen/awesome-streamlit
"""
)
import streamlit as st
import pydeck as pdk
import pandas as pd

# Example data: cities in Korea
data = pd.DataFrame({
    "city": ["Seoul", "Busan", "Daegu"],
    "lat": [37.5665, 35.1796, 35.8714],
    "lon": [126.9780, 129.0756, 128.6014]
})

st.title("🗺️ Interactive Map of South Korea (Pydeck)")

# Define Pydeck layer
layer = pdk.Layer(
    "ScatterplotLayer",
    data,
    get_position='[lon, lat]',
    get_radius=50000,
    get_fill_color='[255, 0, 0, 160]',
    pickable=True,
)

# Set the viewport location
view_state = pdk.ViewState(
    longitude=127.7669,
    latitude=35.9078,
    zoom=6,
    pitch=0,
)

# Render map
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{city}"}))

import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

# 페이지 설정
st.title("🗺️ 대한민국 행정동 경계 지도")

# GeoJSON URL
geojson_url = "https://raw.githubusercontent.com/raqoon886/Local_HangJeongDong/main/hangjeongdong.geojson"

# 지도 초기화 (중심은 서울)
m = folium.Map(location=[37.5665, 126.9780], zoom_start=10)

# GeoJSON 데이터 불러오기 및 지도에 추가
geojson_data = requests.get(geojson_url).json()
folium.GeoJson(geojson_data, name="행정동").add_to(m)

# 지도 표시
st_data = st_folium(m, width=1000, height=700)

import requests

geojson_url = "https://raw.githubusercontent.com/raqoon886/Local_HangJeongDong/main/hangjeongdong.geojson"
response = requests.get(geojson_url)

# 응답 내용을 출력해보자
print(response.text[:500])  # 처음 500글자만 미리보기

# 혹시라도 이상한 내용이 있다면 확인 가능




st.subheader("정신건강증진시설의 지역격차 지도")
st.code("pip install streamlit 혹은  \nconda instalel streamlit")

st.subheader("Streamlit 실행")
st.code("streamlit run tutorial.py")

st.header("인터페이스 위젯 만들기")

st.subheader("텍스트 입력")
st.write("텍스트의 입력은 `st.write()` 함수를 사용한다.")

st.subheader("Markdown")
st.markdown(
"""
Markdown 문법으로 텍스트를 입력하려면 `st.markdown()`을 사용한다. Markdown에서 활용가능한 모든 문법을 사용할 수 있다.

예를 들어,
* bullet point1
* bullet point2
    * bullet point2-1
를 입력하거나,
1. 숫자항목 1 
2. 숫자항목 2
를 입력할 수 있다.

## 헤딩 2
### 헤딩 3
과 같이 제목을 입력하거나,
> block quote 
의 입력도 가능하다.

수평선을 만들기 위해서는 `- - -` 혹은  `***` 등을 입력한다.
- - -
***

링크를 만들기 위해서는 다음과 같이.
[Go google] (https://google.com)

테이블의 추가도 가능하다.
|          | male | female |
|----------|------|--------|
| Survived |  0   |     2  |
| Deceased |      |        |

"""
)

st.markdown("***")

st.subheader("버튼 만들기")
if st.button("버튼을 눌러주세요"):
      st.write("데이터가 로딩 중입니다..")
      # 데이터 로딩 함수는 여기에!

st.subheader("체크박스 만들기")
cb1 = st.checkbox('체크박스 1')	
if cb1:
    st.write('체크박스 1을 선택했어요.')
cb2 = st.checkbox('체크박스 2', value=True)
if cb2:
    st.write('체크박스 2는 default로 선택이 되었습니다.')

st.subheader("라디오 버튼 만들기")
selected_item = st.radio("Radio Part", ("A", "B", "C"))	
if selected_item == "A":
    st.write("A가 선택됨")
elif selected_item == "B":
    st.write("B가 선택됨")
elif selected_item == "C":
    st.write("C가 선택됨")

st.subheader("선택 박스 만들기")
option = st.selectbox('Please select in selectbox!',
                     ('Americano', 'Café Latte', 'Café Mocha'))	
st.write('You selected:', option)

st.subheader("다중 선택 박스 만들기")
multi_select = st.multiselect('Please select somethings in multi selectbox!',
                             ['Americano', 'Café Latte', 'Café Mocha', 'Tea'])
st.write('You selected:', multi_select)
st.write('결과를 list 형태로 반환한다.')

st.subheader("슬라이더 만들기")
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


st.markdown("***")

st.header("데이터 입력")

st.subheader("텍스트 데이터의 입력")
title = st.text_input("type anything")
st.write('The current movie title is', title)

st.subheader("날짜 데이터의 입력")
dt = st.date_input("type your date")
st.write('The date is', dt)

st.markdown("***")

st.header("데이터 출력")

st.subheader("")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write("Interactive Table")
st.dataframe(df) # same as df or st.write(df). 이런 데이터프레임: sorting, download 등 할 수 있

st.write("Interactive Table with Highlight")
st.dataframe(df.style.highlight_max(axis=0)) # max값을 하이라이트 해준다.

st.write("Static Table")
st.table(df) # 그냥 table이라는 명령어를 쓴다
# table과 데이터프레임을 적절히 잘 사용하면 수집한 데이터를 효과적으로 보여줄 수 있음.

st.markdown("***")

st.header("시각화 예제")

st.subheader("Vega-Light")

st.info("https://vega.github.io/vega-lite/")

df_vega = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

st.vega_lite_chart(df_vega, {
    'width': 'container',
    'height': 500,
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
         'x': {'field': 'a', 'type': 'quantitative'},
         'y': {'field': 'b', 'type': 'quantitative'},
         'size': {'field': 'c', 'type': 'quantitative'},
         'color': {'field': 'c', 'type': 'quantitative'},
    },
}, use_container_width=True)

st.subheader("Plotly")

st.info("https://plotly.com/python/")

import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)


import plotly.express as px

gm_df = px.data.gapminder()
gm_df
years = gm_df.year.unique()
target_year = st.slider('Select a year:', min_value=int(years.min()), max_value=int(years.max()), step=5)
fig3 = px.scatter(gm_df.query("year=={}".format(target_year)), x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)
st.plotly_chart(fig3, use_container_width=True)
