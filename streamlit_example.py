import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import json

# 전체화면 설정
st.set_page_config(layout="wide")
st.title("정신병원 위치 지도 비교")

# 지도 선택 옵션
options = {
    '경상남도 (김해시)': {
        'center': [35.2285, 128.8890],
        'geojson': 'data/hangjeongdong_경상남도.geojson',
        'excel': 'data/gimhae_juso.xlsx',
        'target_regions': ['김해시']
    },
    '전라남도 (순천시, 담양군, 곡성군, 구례군, 고흥군, 보성군, 화순군)': {
        'center': [34.8706, 126.8872],
        'geojson': 'data/hangjeongdong_전라남도.geojson',
        'excel': 'data/jeonnam_juso.xlsx',
        'target_regions': ['순천시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군']
    },
    '강원도 (원주시, 횡성군, 홍천군, 평창군, 영월군)': {
        'center': [37.5, 127.9],  
        'geojson': 'data/hangjeongdong_강원도.geojson', 
        'excel': 'data/gangwon_juso.xlsx',  
        'target_regions': ['원주시', '횡성군', '홍천군', '평창군', '영월군']
    }
}


# 화면을 좌우 분할
col1, col2 = st.columns(2)

def render_map(selection, col):
    config = options[selection]
    center = config['center']
    geojson_path = config['geojson']
    excel_path = config['excel']
    target_regions = config['target_regions']

    # 지도 생성
    m = folium.Map(location=center, zoom_start=10, tiles='CartoDB dark_matter')

    # GeoJSON 로드
    with open(geojson_path, encoding='utf-8') as f:
        geo_data = json.load(f)

    # 전체 테두리
    folium.GeoJson(
        geo_data,
        name="전체 테두리",
        style_function=lambda feature: {
            'fillOpacity': 0,
            'color': '#444444',
            'weight': 1
        }
    ).add_to(m)

    # 강조 지역 필터링
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

    # 엑셀에서 마커 읽기
    df = pd.read_excel(excel_path)
    required_cols = ['주소', '위도', '경도']
    for col_name in required_cols:
        if col_name not in df.columns:
            col.error(f"엑셀 파일에 '{col_name}' 컬럼이 없습니다.")
            return

    for _, row in df.iterrows():
        if pd.notna(row['위도']) and pd.notna(row['경도']):
            popup_html = f"""<div style="white-space: nowrap; font-size:14px;">{row['주소']}</div>"""
            folium.Marker(
                location=[row['위도'], row['경도']],
                popup=folium.Popup(popup_html, max_width=300),
                icon=folium.Icon(color='lightblue', icon='plus-sign')
            ).add_to(m)

    # 지도 출력
    with col:
        st_folium(m, width=700, height=500)

# 왼쪽/오른쪽 선택박스 + 지도 출력
with col1:
    selected_left = st.selectbox("🗺️ 왼쪽 지도 지역 선택", list(options.keys()), key='left')
    render_map(selected_left, col1)

with col2:
    selected_right = st.selectbox("🗺️ 오른쪽 지도 지역 선택", list(options.keys()), key='right')
    render_map(selected_right, col2)

