import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import pandas as pd

# set_page_config는 항상 가장 먼저
st.set_page_config(layout="wide")

# 간단한 Streamlit 마크다운 제목으로 먼저 확인
st.title("정신건강, 수도권만의 권리인가요?")

# HTML 렌더링은 줄이거나 검증된 구조만 사용
st.markdown("""
<div style="background-color: #1e1e1e; padding: 20px; border-radius: 12px; text-align: center; font-size: 18px; line-height: 1.8; color: white;">
    <strong>우리나라 국민의 1/3은</strong> ‘중간 수준 이상의 우울감’을 경험하고 있습니다.  
    <div style="font-size: 12px; color: #bbbbbb; margin-top: 0;">
        출처: ‘정신건강 증진과 위기 대비를 위한 일반인 조사’ (서울대 보건대학원 BK21 건강재난 통합대응을 위한 교육연구단, 2025-05-07)</div>
    <br><br>
    그럼에도, 우리 사회에서 정신건강은 늘 뒷전입니다.  
    <br><br>
    <strong>지방, 농어촌 지역의 정신건강은</strong> 더더욱 방치되어 있습니다.  
    <br><br>
    <strong>본 프로젝트의 목표는</strong> 정신건강증진시설의 지역 격차를 시각화하는 것입니다.
</div>
""", unsafe_allow_html=True)

# 소제목 출력
st.subheader("I. 정신건강증진시설의 개념과 기본 통계")
st.subheader("II. 정신건강증진시설의 지역격차 지도")

# GeoJSON 불러오기
with open("data/sgg_merged.geojson", encoding="utf-8") as f:
    sgg_geojson = json.load(f)

# 인구 데이터 정리
population_data = pd.read_excel("data/population.xlsx")

# 만약 '청주시 흥덕구'처럼 시군구명이 시+구로 되어 있다면, '흥덕구'만 추출
population_data["sgg_name_only"] = population_data["sgg"].str.extract(r'(\S+구|\S+시|\S+군)')

# GeoJSON의 시군구명과 맞춰서 매핑
geo_name_to_code = {f["properties"]["sggnm"]: f["properties"]["sgg"] for f in sgg_geojson["features"]}

# 시군구명을 기준으로 코드 매핑
population_data["sgg_code"] = population_data["sgg_name_only"].map(geo_name_to_code)
population_data = population_data.dropna(subset=["sgg_code"])

# 인구수 병합 (GeoJSON에 int 값과 표시용 문자열 둘 다 삽입)
for feature in sgg_geojson["features"]:
    sgg_code = feature["properties"]["sgg"]
    match = population_data[population_data["sgg_code"] == sgg_code]
    if not match.empty:
        pop_int = int(match["population"].values[0])
        feature["properties"]["population"] = pop_int  # <- 비교용 (int)
        feature["properties"]["population_str"] = f"{pop_int:,}"  # <- 툴팁 표시용
    else:
        feature["properties"]["population"] = 0
        feature["properties"]["population_str"] = "데이터 없음"


# 지도 생성
m = folium.Map(
    location=[36.5, 127.8],
    zoom_start=7,
    tiles=None,
    scrollWheelZoom=True, 
    dragging=True,
    min_zoom=9 ,
    max_bounds=11
)

# 대한민국 경계 설정 (대략)
m.fit_bounds([[33.0, 124.0], [39.5, 132.0]])


# 배경 타일 추가
folium.TileLayer(
    tiles='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
    attr='CartoDB dark_nolabels',
    name='Dark no-labels',
    control=False
).add_to(m)

#인구 최댓값 구하기
max_population = max(
    feature['properties'].get('population', 0)
    for feature in sgg_geojson["features"]
)

#회색 스타일 함수
def style_function(feature):
    pop = feature['properties'].get('population', 0)
    if max_population == 0:
        gray_value = 255
    else:
        norm = pop / max_population  # 0~1 정규화
        gray_value = int(255 * norm)  # 인구 많을수록 밝게

    gray_value = min(max(gray_value, 0), 255)
    hex_color = f"#{gray_value:02x}{gray_value:02x}{gray_value:02x}"
    return {
        'fillOpacity': 0.8,
        'weight': 1,
        'color': 'white',
        'fillColor': hex_color
    }

# 하이라이트 함수
def highlight_function(feature):
    return {
        'fillColor': 'white',
        'color': 'orange',
        'weight': 2,
        'fillOpacity': 0.3
    }

tooltip = folium.GeoJsonTooltip(
    fields=["sidonm", "sggnm", "population_str"],
    aliases=["시도명:", "시군구명:", "인구 수:"],
    localize=True,
    sticky=True
)

popup = folium.GeoJsonPopup(
    fields=["sidonm", "sggnm", "sgg", "population_str"],
    aliases=["시도명:", "시군구명:", "시군구코드:", "인구 수:"]
)

# GeoJSON 레이어 추가 (한 번만)
geo_layer = folium.GeoJson(
    sgg_geojson,
    name="시군구",
    style_function=style_function,
    highlight_function=highlight_function,
    tooltip=tooltip,
    popup=popup
)

geo_layer.add_to(m)
m.fit_bounds(geo_layer.get_bounds())

# 한 번만 지도 출력
st_folium(m, width=1600, height=1400)

st.subheader("III. 보건복지부 의료개혁 실행방안을 '정신병원' 중심으로 분석")