import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import json

# 전체화면 설정
st.set_page_config(layout="wide")
st.title("정신병원 위치 지도")

# 지역 선택 버튼
region = st.radio("지도를 볼 지역을 선택하세요:", ['김해시', '전라남도'])

# 지도 객체 초기화
m = None

if region == '김해시':
    # 김해시 중심 좌표
    center = [35.2285, 128.8890]
    geojson_path = "data/hangjeongdong_경상남도.geojson"
    excel_path = "data/gimhae_juso.xlsx"
    target_region = '김해시'
    
    # 지도 생성
    m = folium.Map(location=center, zoom_start=11, tiles='CartoDB dark_matter')

    # GeoJSON 로드
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

    # 김해시 강조
    gimhae_features = [f for f in geo_data['features'] if f['properties']['sggnm'] == target_region]
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

elif region == '전라남도':
    # 전라남도 중심 좌표
    center = [34.8706, 126.8872]
    geojson_path = "data/hangjeongdong_전라남도.geojson"
    excel_path = "data/jeonnam_juso.xlsx"
    target_regions = ['순천시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군']
    
    # 지도 생성
    m = folium.Map(location=center, zoom_start=9.3, tiles='CartoDB dark_matter')

    # GeoJSON 로드
    with open(geojson_path, encoding='utf-8') as f:
        geo_data = json.load(f)

    # 전체 테두리
    folium.GeoJson(
        geo_data,
        name="전라남도 전체",
        style_function=lambda feature: {
            'fillOpacity': 0,
            'color': '#444444',
            'weight': 1
        }
    ).add_to(m)

    # 주요 지역 강조
    target_features = [f for f in geo_data['features'] if f['properties']['sggnm'] in target_regions]
    target_geojson = {
        "type": "FeatureCollection",
        "features": target_features
    }
    folium.GeoJson(
        target_geojson,
        name="강조 지역",
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

# 공통: 마커 추가
df = pd.read_excel(excel_path)
required_cols = ['주소', '위도', '경도']
for col in required_cols:
    if col not in df.columns:
        st.error(f"엑셀 파일에 '{col}' 컬럼명이 없습니다.")
        st.stop()

for _, row in df.iterrows():
    if pd.notna(row['위도']) and pd.notna(row['경도']):
        popup_html = f"""<div style="white-space: nowrap; font-size:14px;">{row['주소']}</div>"""
        folium.Marker(
            location=[row['위도'], row['경도']],
            popup=folium.Popup(popup_html, max_width=300),
            icon=folium.Icon(color='lightblue', icon='plus-sign')
        ).add_to(m)

# 지도 출력
st_folium(m, width=700, height=500)

