import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import json

st.set_page_config(layout="wide")
st.title("김해시 정신병원 지도")

# 김해시 중심 좌표
gimhae_center = [35.2285, 128.8890]

# 1. 지도 생성
m = folium.Map(location=gimhae_center, zoom_start=11, tiles='CartoDB dark_matter')

# 2. GeoJSON 로드 및 경계 그리기
geojson_path = "data/hangjeongdong_경상남도.geojson"
with open(geojson_path, encoding='utf-8') as f:
    geo_data = json.load(f)

# 경상남도 전체 테두리
folium.GeoJson(
    geo_data,
    name="경상남도 전체",
    style_function=lambda feature: {
        'fillOpacity': 0,
        'color': '#444444',
        'weight': 1
    }
).add_to(m)

# 김해시만 강조
gimhae_features = [f for f in geo_data['features'] if f['properties']['sggnm'] == '김해시']
gimhae_geojson = {
    "type": "FeatureCollection",
    "features": gimhae_features
}
folium.GeoJson(
    gimhae_geojson,
    name="김해시 강조",
    style_function=lambda feature: {
        'fillOpacity': 0,
        'color': 'white',
        'weight': 3
    },
    tooltip=folium.GeoJsonTooltip(
        fields=['sidonm', 'sggnm'],
        aliases=['시도명:', '시군구명:']
    )
).add_to(m)

# 3. gimhae_juso 엑셀 데이터 불러오기 (위도, 경도 포함)
file_path = "data/gimhae_juso.xlsx"
df = pd.read_excel(file_path)

# 좌표 컬럼명 확인
required_cols = ['주소', '위도', '경도']
for col in required_cols:
    if col not in df.columns:
        st.error(f"엑셀 파일에 '{col}' 컬럼명이 없습니다. 실제 컬럼명을 확인해 주세요.")
        st.stop()

# 4. 지도에 마커 추가 (필터링 없이 전체 사용)
for _, row in df.iterrows():
    if pd.notna(row['위도']) and pd.notna(row['경도']):
        # 팝업에 가로로 길게 표시하려고 스타일 넣음 (한 줄 길게)
        popup_html = f"""<div style="white-space: nowrap; font-size:14px;">{row['주소']}</div>"""
        folium.Marker(
            location=[row['위도'], row['경도']],
            popup=folium.Popup(popup_html, max_width=300),
            icon=folium.Icon(color='lightblue', icon='plus-sign')
        ).add_to(m)

# 5. 지도 출력
st_folium(m, width=700, height=500)

