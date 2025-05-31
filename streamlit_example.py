import streamlit as st
import folium
from streamlit_folium import st_folium
import json

# 전체화면 모드
st.set_page_config(layout="wide")

# 🔹 제목/설명
st.markdown("<h1 style='text-align: center;'>정신건강, 수도권만의 권리인가요?</h1>", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: #1e1e1e; padding: 30px; border-radius: 12px; text-align: center; font-size: 20px; line-height: 2; color: white;">
    <strong>우리나라 국민의 1/3은</strong> ‘중간 수준 이상의 우울감’을 경험하고 있습니다.  
    <br><br>
    그럼에도, 우리 사회에서 정신건강은 늘 뒷전입니다.  
    <br><br>
    <strong>지방, 농어촌 지역의 정신건강은</strong> 더더욱 방치되어 있습니다.  
    <br><br>
    <strong>본 프로젝트의 목표는</strong> 정신건강증진시설의 지역 격차를 시각화하는 것입니다.
</div>
""", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>I. 정신건강증진시설의 개념과 기본 통계</h2>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>II. 정신건강증진시설의 지역격차 지도</h2>", unsafe_allow_html=True)

# 🔹 GeoJSON 불러오기
with open("data/sgg_merged.geojson", encoding="utf-8") as f:
    sgg_geojson = json.load(f)

# 🔹 folium 지도 생성
m = folium.Map(
    location=[36.5, 127.8],
    zoom_start=7,
    tiles=None,
    scrollWheelZoom=False,
    dragging=False
)

# 라벨 없는 dark 배경 타일 추가
folium.TileLayer(
    tiles='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
    attr='CartoDB dark_nolabels',
    name='Dark no-labels',
    control=False
).add_to(m)

# 시군구 스타일 지정
def style_function(feature):
    return {
        'fillOpacity': 0.0,
        'weight': 1.5,
        'color': 'white'
    }

def highlight_function(feature):
    return {
        'fillColor': 'white',
        'color': 'orange',
        'weight': 2,
        'fillOpacity': 0.3
    }

# GeoJson 레이어
geo_layer = folium.GeoJson(
    sgg_geojson,
    name="시군구",
    style_function=style_function,
    highlight_function=highlight_function,
    tooltip=folium.GeoJsonTooltip(
        fields=["sidonm", "sggnm"],
        aliases=["시도명:", "시군구명:"],
        sticky=True
    ),
    popup=folium.GeoJsonPopup(
        fields=["sidonm", "sggnm", "sgg"],
        aliases=["시도명:", "시군구명:", "시군구코드:"],
    )
)

geo_layer.add_to(m)
m.fit_bounds(geo_layer.get_bounds())

# 🔹 지도 전체 화면 채우기 (최대 비율로 설정)
st_folium(m, width=1600, height=1400)

st.markdown("<h2 style='text-align: center;'>III. 보건복지부 의료개혁 실행방안을 '정신병원' 중심으로 분석</h2>", unsafe_allow_html=True)