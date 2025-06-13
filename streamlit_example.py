import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import pandas as pd
import math
import os
from branca.element import Template, MacroElement
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from io import BytesIO

# set_page_config는 항상 가장 먼저
st.set_page_config(layout="wide")

# 간단한 Streamlit 마크다운 제목으로 먼저 확인
st.markdown("""
<h1 style='
    text-align: center;
    font-size: 64px;
    font-weight: 900;
    margin-top: 30px;
    margin-bottom: 40px;
    color: #1e1e1e;
    letter-spacing: -1px;
    text-shadow: 2px 2px 0px #ffffff, 4px 4px 0px #cccccc;
'>
    정신건강, 수도권만의 권리인가요?
</h1>
""", unsafe_allow_html=True)


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
# I. 정신건강증진시설의 개념과 기본 통계
st.markdown("""
<h1 style='text-align: center; font-size: 40px; margin-top: 60px;'>
    I. 정신건강증진시설의 개념과 기본 통계
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h2 style='text-align: center; margin-top: 40px;'>정신건강증진시설이란?</h2>

<div style="background-color: #e3f2fd; padding: 20px; border-left: 6px solid #1976d2; border-radius: 8px; margin-bottom: 25px; font-size: 16px;">
    「정신건강증진 및 정신질환자 복지서비스 지원에 관한 법률」 제3조 제4호에 따르면,  
    <strong>‘정신건강증진시설’이란 정신의료기관, 정신요양시설 및 정신재활시설</strong>을 말합니다.  
    이들 시설을 중심으로 <strong>국가와 지방자치단체는 정신건강의 예방부터 조기발견, 치료, 재활, 사회복귀까지 전 과정을 포괄하는 서비스를 계획·시행</strong>하고 있습니다.
</div>

<div style="background-color: #f9f9f9; padding: 25px; border-radius: 12px; line-height: 1.8; font-size: 17px;">
    <ul>
        <li><strong>정신건강복지센터:</strong> 지역주민 및 정신장애인과 그 가족에게 포괄적인 정신건강 서비스를 제공합니다.</li>
        <li><strong>아동·청소년 정신건강복지센터:</strong> 조기 발견, 상담·치료를 통해 아동·청소년의 건강한 성장을 지원합니다.</li>
        <li><strong>노인정신건강복지센터:</strong> 노인 대상 정신건강 서비스 제공으로 건강한 노년을 지원합니다.</li>
        <li><strong>자살예방센터:</strong> 자살 고위험군 및 유가족에 대한 지원과 생명존중 문화 확산을 위한 서비스를 제공합니다.</li>
        <li><strong>중독관리통합지원센터:</strong> 알코올, 약물, 도박 등 중독자 조기발견부터 치료·재활까지 통합적 지원을 합니다.</li>
        <li><strong>트라우마센터:</strong> 재난이나 사고로 인한 심리적 충격에 대응해 심리 안정과 사회 적응을 돕습니다.</li>
        <li><strong>정신재활시설:</strong> 정신질환자의 사회복귀를 위한 생활지원, 직업재활, 주거제공 등을 수행합니다.</li>
        <li><strong>정신요양시설:</strong> 보호가 필요한 만성 정신질환자의 요양·보호를 통해 삶의 질 향상을 지원합니다.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

import matplotlib.font_manager as fm

# 폰트 경로 설정
font_path = "data/NanumGothic.ttf"  # 파일 경로가 다르면 수정
font_prop = fm.FontProperties(fname=font_path)

# 📊 2018~2023 전국 정신건강증진 시설 수 변화 선그래프 표시
st.markdown("""
<h2 style='text-align: center; margin-top: 40px;'>2018~2023 전국 정신건강증진 시설 수 변화</h2>
""", unsafe_allow_html=True)

# 그래프 데이터 로드 및 전처리
df_year = pd.read_excel("data/2018_2023_정신건강시설.xlsx")
df_cleaned = df_year.iloc[1:4].copy()
df_cleaned.columns = ['종류', 2018, 2019, 2020, 2021, 2022, 2023]
df_cleaned.set_index('종류', inplace=True)
df_cleaned = df_cleaned.astype(int).T
df_cleaned.index = df_cleaned.index.astype(int)

# 그래프 생성 및 크기 조절
fig, ax = plt.subplots(figsize=(6, 3.5))
for col in df_cleaned.columns:
    ax.plot(df_cleaned.index, df_cleaned[col], marker='o', label=col)

# ✅ 폰트 적용
ax.set_title("2018~2023 전국 정신건강증진 시설 수 변화", fontsize=40, fontproperties=font_prop)
ax.set_xlabel("연도", fontsize=10, fontproperties=font_prop)
ax.set_ylabel("시설 수", fontsize=10, fontproperties=font_prop)
ax.set_xticks(df_cleaned.index)
ax.set_xticklabels(df_cleaned.index, fontproperties=font_prop)
ax.legend(prop=font_prop, fontsize=9)
ax.grid(True)

st.pyplot(fig)

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import streamlit as st
import os

import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import pandas as pd
import math
import os
from branca.element import Template, MacroElement
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from io import BytesIO


# II. 정신건강증진시설의 지역격차 지도
st.markdown("""
<h1 style='text-align: center; font-size: 40px; margin-top: 80px;'>
    II. 정신건강증진시설의 지역격차 지도
</h1>
""", unsafe_allow_html=True)

# ✅ 수동 면적 정보 (㎢ 기준)
manual_area_map = {
    '서울특별시 (강남구)': 39.55,
    '경상남도 (김해시)': 463.3,
    '전라남도 (순천시, 담양군, 곡성군, 구례군, 고흥군, 보성군, 화순군)': 5369,
    '강원도 (원주시, 횡성군, 홍천군, 평창군, 영월군)': 5997
}

# ✅ 면적 기반 줌 계산 (강남구는 더 작게 보이도록)
def zoom_from_manual_area(area_km2):
    max_zoom = 16
    min_zoom = 7
    max_area = 6000
    min_area = 40
    norm = (math.log(max_area) - math.log(area_km2)) / (math.log(max_area) - math.log(min_area))
    return round(min_zoom + norm * (max_zoom - min_zoom), 1)

# ✅ 확대 상태 저장
if "zoom_enabled" not in st.session_state:
    st.session_state.zoom_enabled = False

# ✅ 지도 설정 정보
options = {
    '서울특별시 (강남구)': {
        'geojson': 'data/hangjeongdong_강남구.geojson',
        'excel': 'data/gangnam_juso.xlsx',
        'target_regions': ['강남구']
    },
    '경상남도 (김해시)': {
        'geojson': 'data/hangjeongdong_경상남도.geojson',
        'excel': 'data/gimhae_juso.xlsx',
        'target_regions': ['김해시']
    },
    '전라남도 (순천시, 담양군, 곡성군, 구례군, 고흥군, 보성군, 화순군)': {
        'geojson': 'data/hangjeongdong_전라남도.geojson',
        'excel': 'data/jeonnam_juso.xlsx',
        'target_regions': ['순천시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군']
    },
    '강원도 (원주시, 횡성군, 홍천군, 평창군, 영월군)': {
        'geojson': 'data/hangjeongdong_강원도.geojson',
        'excel': 'data/gangwon_juso.xlsx',
        'target_regions': ['원주시', '횡성군', '홍천군', '평창군', '영월군']
    }
}

# ✅ 범례 HTML
legend_html = """
{% macro html(this, kwargs) %}
<div style='
    position: fixed;
    bottom: 50px;
    left: 50px;
    z-index: 9999;
    background-color: rgba(255,255,255,0.85);
    padding: 10px;
    border-radius: 5px;
    font-size: 14px;
'>
    <b>🗂 범례</b><br>
    <i class="fa fa-plus-square" style="color: lightblue"></i> 정신병원<br>
    <i class="fa fa-heart" style="color: orange"></i> 정신재활시설
</div>
{% endmacro %}
"""
legend = MacroElement()
legend._template = Template(legend_html)

# ✅ 지도 렌더링 함수
def render_map(selection, col):
    config = options[selection]
    geojson_path = config['geojson']
    excel_path = config['excel']
    target_regions = config['target_regions']

    with open(geojson_path, encoding='utf-8') as f:
        geo_data = json.load(f)

    features = [
        f for f in geo_data['features']
        if any(region in f['properties'].get('adm_nm', '') for region in target_regions)
        or f['properties'].get('sggnm') in target_regions
    ]
    target_geojson = {"type": "FeatureCollection", "features": features}

    # 중심 계산
    bounds = []
    for f in features:
        coords = f['geometry']['coordinates']
        if f['geometry']['type'] == 'Polygon':
            for ring in coords:
                bounds.extend(ring)
        elif f['geometry']['type'] == 'MultiPolygon':
            for poly in coords:
                for ring in poly:
                    bounds.extend(ring)

    lats = [pt[1] for pt in bounds]
    lons = [pt[0] for pt in bounds]
    min_lat, max_lat = min(lats), max(lats)
    min_lon, max_lon = min(lons), max(lons)
    center_lat = (min_lat + max_lat) / 2
    center_lon = (min_lon + max_lon) / 2

    # ✅ 면적 기반 줌
    area_km2 = manual_area_map.get(selection, 500)
    zoom_start = zoom_from_manual_area(area_km2)

    # 지도 생성
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=zoom_start,
        scrollWheelZoom=st.session_state.zoom_enabled,
        dragging=st.session_state.zoom_enabled,
        zoom_control=st.session_state.zoom_enabled,
        tiles='CartoDB dark_matter',
        control_scale=True
    )

    folium.GeoJson(
        geo_data,
        style_function=lambda _: {'fillOpacity': 0, 'color': '#444444', 'weight': 1}
    ).add_to(m)

    folium.GeoJson(
        target_geojson,
        style_function=lambda _: {'fillOpacity': 0, 'color': 'white', 'weight': 3},
        tooltip=folium.GeoJsonTooltip(fields=['sidonm', 'sggnm'], aliases=['시도명:', '시군구명:'])
    ).add_to(m)

    df = pd.read_excel(excel_path)
    for _, row in df.iterrows():
        if pd.notna(row['위도']) and pd.notna(row['경도']):
            folium.Marker(
                location=[row['위도'], row['경도']],
                popup=folium.Popup(f"<div style='font-size:14px'>{row['주소']}</div>", max_width=300),
                icon=folium.Icon(color='lightblue', icon='plus-sign')
            ).add_to(m)

    if '전라남도' in selection:
        try:
            rehab_df = pd.read_excel('data/jeonnam_juso 2.xlsx')
            for _, row in rehab_df.iterrows():
                if pd.notna(row['위도']) and pd.notna(row['경도']):
                    folium.Marker(
                        location=[row['위도'], row['경도']],
                        popup=folium.Popup(f"<div style='font-size:14px'>{row['주소']}</div>", max_width=300),
                        icon=folium.Icon(color='orange', icon='heart')
                    ).add_to(m)
        except Exception as e:
            col.error(f"정신재활시설 파일 로딩 오류: {e}")
    elif '강원도' in selection:
        try:
            # 정신재활시설 한 곳만 수동으로 추가
            folium.Marker(
                location=[37.43953, 127.9878],  # 위도, 경도
                popup=folium.Popup(
                    "<div style='font-size:14px'>강원특별자치도 원주시 소초면 둔둔로 217-19</div>",
                    max_width=300
                ),
                icon=folium.Icon(color='orange', icon='heart')
            ).add_to(m)
        except Exception as e:
            col.error(f"정신재활시설 표시 오류: {e}")
    elif '강남구' in selection:
        try:
            # 정신재활시설 한 곳만 수동으로 추가
            folium.Marker(
                location=[37.4855441, 127.0758442],  # 위도, 경도
                popup=folium.Popup(
                    "<div style='font-size:14px'>서울특별시 강남구 광평로 185</div>",
                    max_width=300
                ),
                icon=folium.Icon(color='orange', icon='heart')
            ).add_to(m)
        except Exception as e:
            col.error(f"정신재활시설 표시 오류: {e}")
    elif '김해시' in selection or '경상남도' in selection:
        try:
        # 정신재활시설 한 곳 수동 추가 (김해시)
            folium.Marker(
                location=[35.2396888, 128.8558248],  # 김해시 평전로93번길 10-19
                popup=folium.Popup(
                    "<div style='font-size:14px'>경상남도 김해시 평전로93번길 10-19</div>",
                    max_width=300
                ),
                icon=folium.Icon(color='orange', icon='heart')
            ).add_to(m)
        except Exception as e:
            col.error(f"정신재활시설 표시 오류: {e}")


    m.get_root().add_child(legend)
    m.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])

    with col:
        st_folium(m, width=700, height=500)

    font_path = os.path.abspath('data/NanumGothic.ttf')
    font_prop = fm.FontProperties(fname=font_path)

    # ✅ 전라남도 설명 및 그래프 표시
    if '전라남도' in selection:
        with col:
            st.markdown("""
            **대상 지역:** 전라남도 순천시, 담양군, 곡성군, 구례군, 고흥군, 보성군, 화순군  
            **지역 총면적:** 5,432.27 km²  
            **지역 총인구:** 554,371명  
            
            **지역별 정신병원 및 정신재활센터 수:**
            """)

            labels = ['고흥군', '곡성군', '담양군', '보성군', '순천시', '화순군']
            hospital_counts = [1, 1, 3, 2, 12, 4]
            rehab_counts = [0, 0, 0, 0, 1, 0]
            x = range(len(labels))
            width = 0.35

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar([i - width/2 for i in x], hospital_counts, width, label='정신병원', color='lightblue')
            ax.bar([i + width/2 for i in x], rehab_counts, width, label='정신재활센터', color='orange')
            ax.set_xticks(list(x))
            ax.set_xticklabels(labels, fontproperties=font_prop)
            ax.set_ylabel("기관 수", fontproperties=font_prop)
            ax.set_title("전라남도 지역별 정신의료 인프라 분포", fontproperties=font_prop)
            ax.legend(prop=font_prop)
            st.pyplot(fig)

    elif '서울특별시' in selection:
        with col:
            st.markdown("""
            **대상 지역:** 서울특별시 강남구       
            **지역 총면적:** 39.55km²      
            **지역 총인구:** 556,822명
                        
            **지역별 정신병원 및 정신재활센터 수:** 102개/1개
            """)

        # ✅ 김해시 설명 및 그래프 표시
    elif '김해시' in selection:
        with col:
            st.markdown("""
            **대상 지역:** 경상남도 김해시  
            **지역 총면적:** 463.3 km²  
            **지역 총인구:** 532,792명  
            
            **지역별 정신병원 및 정신재활센터 수:**
            """)

            labels = ['김해시']  # 예시 구분
            hospital_counts = [11]  # 예시 데이터
            rehab_counts = [1]     # 예시 데이터
            x = [2]
            width = 0.3

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar([i - width/2 for i in x], hospital_counts, width, label='정신병원', color='lightblue')
            ax.bar([i + width/2 for i in x], rehab_counts, width, label='정신재활센터', color='orange')
            ax.set_xlim(0,4)
            ax.set_xticks(list(x))
            ax.set_xticklabels(labels, fontproperties=font_prop)
            ax.set_ylabel("기관 수", fontproperties=font_prop)
            ax.set_title("김해시 지역별 정신의료 인프라 분포", fontproperties=font_prop)
            ax.legend(prop=font_prop)
            st.pyplot(fig)

    elif '강원도' in selection:
     with col:
        st.markdown("""
        **대상 지역:** 강원도 원주시, 횡성군, 홍천군, 평창군, 영월군  
        **지역 총면적:**  6272.74 km²  
        **지역 총인구:** 550028명  
        
        **지역별 정신병원 및 정신재활센터 수:**
        """)

        labels = ['원주시', '횡성군', '홍천군', '평창군', '영월군']
        hospital_counts = [13, 0, 1, 0, 1]  # 실제 숫자 넣기
        rehab_counts =  [1, 0, 0, 0, 0]   # 실제 숫자 넣기
        x = range(len(labels))
        width = 0.35

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar([i - width/2 for i in x], hospital_counts, width, label='정신병원', color='lightblue')
        ax.bar([i + width/2 for i in x], rehab_counts, width, label='정신재활센터', color='orange')
        ax.set_xticks(list(x))
        ax.set_xticklabels(labels, fontproperties=font_prop)
        ax.set_ylabel("기관 수", fontproperties=font_prop)
        ax.set_title("강원도 지역별 정신의료 인프라 분포", fontproperties=font_prop)
        ax.legend(prop=font_prop)
        st.pyplot(fig)




col1, col2 = st.columns(2)

# 왼쪽 지도 선택
with col1:
    selected_left = st.selectbox("🗺️ 왼쪽 지도 지역 선택", list(options.keys()), key='left_map')
    render_map(selected_left, col1)

# 오른쪽 지도 선택 - 왼쪽과 다른 옵션만 제공
with col2:
    right_options = [opt for opt in options.keys() if opt != selected_left]

    # 현재 세션에 selected_right가 존재하고, 그것이 새로운 옵션에 없다면 초기화
    if "selected_right" not in st.session_state or st.session_state.selected_right not in right_options:
        st.session_state.selected_right = right_options[0] if right_options else None

    if right_options:
        selected_right = st.selectbox("🗺️ 오른쪽 지도 지역 선택", right_options, index=right_options.index(st.session_state.selected_right), key='right_map')
        render_map(selected_right, col2)
    else:
        st.warning("⚠️ 왼쪽과 다른 지역을 선택해 주세요.")


# ✅ 확대 기능 버튼
st.markdown("---")
if not st.session_state.zoom_enabled:
    if st.button("🔍 확대 기능 켜기"):
        st.session_state.zoom_enabled = True
        st.rerun()
else:
    colz1, colz2 = st.columns([3, 1])
    colz1.success("🖱️ 이제 지도를 자유롭게 확대·이동할 수 있습니다.")
    if colz2.button("🔒 확대 기능 끄기"):
        st.session_state.zoom_enabled = False
        st.rerun()

# ✅ 수동 면적 정보 (㎢ 기준)
manual_area_map = {
    '서울특별시 (강남구)': 39.55,
    '경상남도 (김해시)': 463.3,
    '전라남도 (순천시, 담양군, 곡성군, 구례군, 고흥군, 보성군, 화순군)': 5369,
    '강원도 (원주시, 횡성군, 홍천군, 평창군, 영월군)': 5997
}

# ✅ 면적 기반 줌 계산 (강남구는 더 작게 보이도록)
def zoom_from_manual_area(area_km2):
    max_zoom = 16
    min_zoom = 7
    max_area = 6000
    min_area = 40
    norm = (math.log(max_area) - math.log(area_km2)) / (math.log(max_area) - math.log(min_area))
    return round(min_zoom + norm * (max_zoom - min_zoom), 1)

# ✅ 확대 상태 저장
if "zoom_enabled" not in st.session_state:
    st.session_state.zoom_enabled = False

# ✅ 지도 설정 정보
options = {
    '서울특별시 (강남구)': {
        'geojson': 'data/hangjeongdong_강남구.geojson',
        'excel': 'data/gangnam_juso.xlsx',
        'target_regions': ['강남구']
    },
    '경상남도 (김해시)': {
        'geojson': 'data/hangjeongdong_경상남도.geojson',
        'excel': 'data/gimhae_juso.xlsx',
        'target_regions': ['김해시']
    },
    '전라남도 (순천시, 담양군, 곡성군, 구례군, 고흥군, 보성군, 화순군)': {
        'geojson': 'data/hangjeongdong_전라남도.geojson',
        'excel': 'data/jeonnam_juso.xlsx',
        'target_regions': ['순천시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군']
    },
    '강원도 (원주시, 횡성군, 홍천군, 평창군, 영월군)': {
        'geojson': 'data/hangjeongdong_강원도.geojson',
        'excel': 'data/gangwon_juso.xlsx',
        'target_regions': ['원주시', '횡성군', '홍천군', '평창군', '영월군']
    }
}

# ✅ 범례 HTML
legend_html = """
{% macro html(this, kwargs) %}
<div style='
    position: fixed;
    bottom: 50px;
    left: 50px;
    z-index: 9999;
    background-color: rgba(255,255,255,0.85);
    padding: 10px;
    border-radius: 5px;
    font-size: 14px;
'>
    <b>🗂 범례</b><br>
    <i class="fa fa-plus-square" style="color: lightblue"></i> 정신병원<br>
    <i class="fa fa-heart" style="color: orange"></i> 정신재활시설
</div>
{% endmacro %}
"""
legend = MacroElement()
legend._template = Template(legend_html)

# ✅ 지도 렌더링 함수
def render_map(selection, col):
    config = options[selection]
    geojson_path = config['geojson']
    excel_path = config['excel']
    target_regions = config['target_regions']

    with open(geojson_path, encoding='utf-8') as f:
        geo_data = json.load(f)

    features = [
        f for f in geo_data['features']
        if any(region in f['properties'].get('adm_nm', '') for region in target_regions)
        or f['properties'].get('sggnm') in target_regions
    ]
    target_geojson = {"type": "FeatureCollection", "features": features}

    # 중심 계산
    bounds = []
    for f in features:
        coords = f['geometry']['coordinates']
        if f['geometry']['type'] == 'Polygon':
            for ring in coords:
                bounds.extend(ring)
        elif f['geometry']['type'] == 'MultiPolygon':
            for poly in coords:
                for ring in poly:
                    bounds.extend(ring)

    lats = [pt[1] for pt in bounds]
    lons = [pt[0] for pt in bounds]
    min_lat, max_lat = min(lats), max(lats)
    min_lon, max_lon = min(lons), max(lons)
    center_lat = (min_lat + max_lat) / 2
    center_lon = (min_lon + max_lon) / 2

    # ✅ 면적 기반 줌
    area_km2 = manual_area_map.get(selection, 500)
    zoom_start = zoom_from_manual_area(area_km2)

    # 지도 생성
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=zoom_start,
        scrollWheelZoom=st.session_state.zoom_enabled,
        dragging=st.session_state.zoom_enabled,
        zoom_control=st.session_state.zoom_enabled,
        tiles='CartoDB dark_matter'
    )

    folium.GeoJson(
        geo_data,
        style_function=lambda _: {'fillOpacity': 0, 'color': '#444444', 'weight': 1}
    ).add_to(m)

    folium.GeoJson(
        target_geojson,
        style_function=lambda _: {'fillOpacity': 0, 'color': 'white', 'weight': 3},
        tooltip=folium.GeoJsonTooltip(fields=['sidonm', 'sggnm'], aliases=['시도명:', '시군구명:'])
    ).add_to(m)

    df = pd.read_excel(excel_path)
    for _, row in df.iterrows():
        if pd.notna(row['위도']) and pd.notna(row['경도']):
            folium.Marker(
                location=[row['위도'], row['경도']],
                popup=folium.Popup(f"<div style='font-size:14px'>{row['주소']}</div>", max_width=300),
                icon=folium.Icon(color='lightblue', icon='plus-sign')
            ).add_to(m)

    if '전라남도' in selection:
        try:
            rehab_df = pd.read_excel('data/jeonnam_juso 2.xlsx')
            for _, row in rehab_df.iterrows():
                if pd.notna(row['위도']) and pd.notna(row['경도']):
                    folium.Marker(
                        location=[row['위도'], row['경도']],
                        popup=folium.Popup(f"<div style='font-size:14px'>{row['주소']}</div>", max_width=300),
                        icon=folium.Icon(color='orange', icon='heart')
                    ).add_to(m)
        except Exception as e:
            col.error(f"정신재활시설 표시 오류: {e}")
    elif '강원도' in selection:
        try:
            # 정신재활시설 한 곳만 수동으로 추가
            folium.Marker(
                location=[37.43953, 127.9878],  # 위도, 경도
                popup=folium.Popup(
                    "<div style='font-size:14px'>강원특별자치도 원주시 소초면 둔둔로 217-19</div>",
                    max_width=300
                ),
                icon=folium.Icon(color='orange', icon='heart')
            ).add_to(m)
        except Exception as e:
            col.error(f"정신재활시설 표시 오류: {e}")
    elif '강남구' in selection:
        try:
            # 정신재활시설 한 곳만 수동으로 추가
            folium.Marker(
                location=[37.4855441, 127.0758442],  # 위도, 경도
                popup=folium.Popup(
                    "<div style='font-size:14px'>서울특별시 강남구 광평로 185</div>",
                    max_width=300
                ),
                icon=folium.Icon(color='orange', icon='heart')
            ).add_to(m)
        except Exception as e:
            col.error(f"정신재활시설 표시 오류: {e}")

    m.get_root().add_child(legend)
    m.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])

    with col:
        st_folium(m, width=700, height=500)

    font_path = os.path.abspath('data/NanumGothic.ttf')
    font_prop = fm.FontProperties(fname=font_path)

# [중략: 기존 코드 동일, 생략 없이 이어짐]
     # ✅ 강원도 설명 및 그래프 표시
    if '강원도' in selection:
     with col:
        st.markdown("""
        **대상 지역:** 강원도 원주시, 횡성군, 홍천군, 평창군, 영월군  
        **지역 총면적:**  6272.74 km²  
        **지역 총인구:** 550028명  
        
        **지역별 정신병원 및 정신재활센터 수:**
        """)

        labels = ['원주시', '횡성군', '홍천군', '평창군', '영월군']
        hospital_counts = [13, 0, 1, 0, 1]  # 실제 숫자 넣기
        rehab_counts =  [1, 0, 0, 0, 0]   # 실제 숫자 넣기
        x = range(len(labels))
        width = 0.35

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar([i - width/2 for i in x], hospital_counts, width, label='정신병원', color='lightblue')
        ax.bar([i + width/2 for i in x], rehab_counts, width, label='정신재활센터', color='orange')
        ax.set_xticks(list(x))
        ax.set_xticklabels(labels, fontproperties=font_prop)
        ax.set_ylabel("기관 수", fontproperties=font_prop)
        ax.set_title("강원도 지역별 정신의료 인프라 분포", fontproperties=font_prop)
        ax.legend(prop=font_prop)
        st.pyplot(fig)

    # ✅ 전라남도 설명 및 그래프 표시
    elif '전라남도' in selection:
        with col:
            st.markdown("""
            **대상 지역:** 전라남도 순천시, 담양군, 곡성군, 구례군, 고흥군, 보성군, 화순군  
            **지역 총면적:** 5,432.27 km²  
            **지역 총인구:** 554,371명  
            
            **지역별 정신병원 및 정신재활센터 수:**
            """)

            labels = ['고흥군', '곡성군', '담양군', '보성군', '순천시', '화순군']
            hospital_counts = [1, 1, 3, 2, 12, 4]
            rehab_counts = [0, 0, 0, 0, 1, 0]
            x = range(len(labels))
            width = 0.35

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar([i - width/2 for i in x], hospital_counts, width, label='정신병원', color='lightblue')
            ax.bar([i + width/2 for i in x], rehab_counts, width, label='정신재활센터', color='orange')
            ax.set_xticks(list(x))
            ax.set_xticklabels(labels, fontproperties=font_prop)
            ax.set_ylabel("기관 수", fontproperties=font_prop)
            ax.set_title("전라남도 지역별 정신의료 인프라 분포", fontproperties=font_prop)
            ax.legend(prop=font_prop)
            st.pyplot(fig)

    # ✅ 김해시 설명 및 그래프 표시
    elif '김해시' in selection:
        with col:
            st.markdown("""
            **대상 지역:** 경상남도 김해시  
            **지역 총면적:** 463.3 km²  
            **지역 총인구:** 556,505명  
            
            **지역별 정신병원 및 정신재활센터 수:**
            """)

            labels = ['김해시 동부', '김해시 서부']  # 예시 구분
            hospital_counts = [6, 3]  # 예시 데이터
            rehab_counts = [1, 0]     # 예시 데이터
            x = range(len(labels))
            width = 0.35

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar([i - width/2 for i in x], hospital_counts, width, label='정신병원', color='lightblue')
            ax.bar([i + width/2 for i in x], rehab_counts, width, label='정신재활센터', color='orange')
            ax.set_xticks(list(x))
            ax.set_xticklabels(labels, fontproperties=font_prop)
            ax.set_ylabel("기관 수", fontproperties=font_prop)
            ax.set_title("김해시 지역별 정신의료 인프라 분포", fontproperties=font_prop)
            ax.legend(prop=font_prop)
            st.pyplot(fig)

    elif '서울특별시' in selection:
        with col:
            st.markdown("""
            **대상 지역:** 서울특별시 강남구       
            **지역 총면적:** 39.55km²      
            **지역 총인구:** 556,822명
                        
            **지역별 정신병원 및 정신재활센터 수:** 102개/1개
            """)


import streamlit as st
import json
import pandas as pd
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

# 상태 변수 초기화
if "story_stage" not in st.session_state:
    st.session_state.story_stage = 1

def next_stage():
    st.session_state.story_stage += 1

def prev_stage():
    st.session_state.story_stage -= 1

# 데이터 불러오기
gangnam_df = pd.read_excel("data/gangnam_juso.xlsx").dropna(subset=['위도', '경도'])
seolleung_df = pd.read_excel("data/seoulleung_juso.xlsx").dropna(subset=['위도', '경도'])
seolleung_hospitals = gangnam_df[gangnam_df['주소'].str.contains("선릉로", na=False)]

# 타이틀
st.markdown("<h1 style='text-align:center; font-size:40px;'>III. A씨와 B씨의 이야기</h1>", unsafe_allow_html=True)

# 1단계: 인물 소개
if st.session_state.story_stage == 1:
    st.markdown("<h2 style='text-align: center; font-size:40px; margin-top:100px;'>강남구에 사는 A씨가 있습니다.</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("data/A씨.png", width=240)

# 2단계: 전체 강남구 지도
elif st.session_state.story_stage == 2:
    st.markdown("<h2 style='text-align:center; font-size:40px; margin-bottom:20px;'>강남구에는 정신병원이 102곳, 정신재활센터는 1곳 있습니다.</h2>", unsafe_allow_html=True)

    m = folium.Map(location=[37.4979, 127.0276], zoom_start=13, tiles=None,
                   zoom_control=False, dragging=False, scrollWheelZoom=False)

    with open("data/gangnam_only.geojson", encoding="utf-8") as f:
        gangnam_geo = json.load(f)

    folium.GeoJson(gangnam_geo, style_function=lambda x: {
        'fillColor': 'none', 'color': 'black', 'weight': 3, 'fillOpacity': 0
    }).add_to(m)

    for _, row in gangnam_df.iterrows():
        folium.CircleMarker(
            location=[row['위도'], row['경도']],
            radius=5, color='red', fill=True, fill_color='red', fill_opacity=0.9
        ).add_to(m)

    st_folium(m, width=1200, height=700)

# 3단계: 선릉로 강조 지도
elif st.session_state.story_stage == 3:
    st.markdown("<h2 style='text-align:center; font-size:40px; margin-bottom:20px;'>A씨가 거주하는 선릉로에만 정신병원이 12곳 있습니다.</h2>", unsafe_allow_html=True)

    m = folium.Map(location=[37.5045, 127.0497], zoom_start=14, tiles=None,
                   zoom_control=False, dragging=False, scrollWheelZoom=False)

    m.get_root().html.add_child(folium.Element("""
        <style>.leaflet-container {background-color: #007f00 !important;}</style>
    """))

    # 선릉로 라인
    points = list(zip(seolleung_df['위도'], seolleung_df['경도']))
    folium.PolyLine(points, color='orange', weight=8, opacity=1).add_to(m)

    # 병원 마커
    for _, row in seolleung_hospitals.iterrows():
        folium.CircleMarker(
            location=[row['위도'], row['경도']],
            radius=7,
            color='red',
            weight=2,
            fill=True,
            fill_color = 'red',
            fill_opacity=0.9
        ).add_to(m)

    st_folium(m, width=1200, height=700)

elif st.session_state.story_stage == 4:
    st.markdown("<h2 style='text-align:center; font-size:40px;'>A씨의 거주지로부터 정신병원까지 가는 데는 얼마나 걸릴까요?</h2>", unsafe_allow_html=True)

    # 지도 설정
    m = folium.Map(location=[37.4979, 127.0276], zoom_start=13, tiles=None,
                   zoom_control=False, dragging=False, scrollWheelZoom=False)

    m.get_root().html.add_child(folium.Element("""
        <style>.leaflet-container {background-color: #007f00 !important;}</style>
    """))

    # GeoJSON 로드
    with open("data/gangnam_only.geojson", encoding="utf-8") as f:
        gangnam_geo = json.load(f)

    # 스타일 함수 정의: 역삼2동만 노란색, 나머지는 투명
    def style_function(feature):
        adm_nm = feature['properties'].get('adm_nm', '')
        if adm_nm == "서울특별시 강남구 역삼2동":
            return {
                'fillColor': '#ffd700',
                'color': 'black',
                'weight': 3,
                'fillOpacity': 0.8
            }
        else:
            return {
                'fillColor': 'none',
                'color': 'black',
                'weight': 3,
                'fillOpacity': 0
            }

    # GeoJSON 지도 추가
    folium.GeoJson(
        gangnam_geo,
        name="강남구 행정동",
        style_function=style_function
    ).add_to(m)

    # 병원 위치에 CircleMarker 추가
    for _, row in gangnam_df.iterrows():
        folium.CircleMarker(
            location=[row['위도'], row['경도']],
            radius=5,
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.9
        ).add_to(m)

    # 지도 렌더링
    st_folium(m, width=1200, height=700)

elif st.session_state.story_stage == 5:
    st.markdown("""
        <h2 style='text-align:center; font-size:28px; margin-bottom:10px;'>
            집 근처, 정신병원들이 모여있는 반경까지 이동하는 데 걸어서 12분이 채 걸리지 않습니다.
        </h2>
        <h3 style='text-align:center; font-size:28px; color: black;'>
            많은 병원들이 분포되어 있기 때문에, 선택지의 폭도 넓습니다.
        </h3>
    """, unsafe_allow_html=True)

    if "path_step" not in st.session_state:
        st.session_state.path_step = 1

    path = [
        [37.5005851, 127.0444115],
        [37.502807, 127.044328],
        [37.503531, 127.0470524],
        [37.5049872, 127.0491562]
    ]

    m = folium.Map(location=[37.5025, 127.0465], zoom_start=16, tiles=None,
                   zoom_control=False, dragging=False, scrollWheelZoom=False)

    m.get_root().html.add_child(folium.Element("""
        <style>.leaflet-container {background-color: #007f00 !important;}</style>
    """))

    with open("data/gangnam_only.geojson", encoding="utf-8") as f:
        gangnam_geo = json.load(f)

    def style_function(feature):
        adm_nm = feature['properties'].get('adm_nm', '')
        if adm_nm == "서울특별시 강남구 역삼2동":
            return {
                'fillColor': '#ffd700',
                'color': 'black',
                'weight': 3,
                'fillOpacity': 0.8
            }
        else:
            return {
                'fillColor': 'none',
                'color': 'black',
                'weight': 3,
                'fillOpacity': 0
            }

    folium.GeoJson(
        gangnam_geo,
        name="강남구 행정동",
        style_function=style_function
    ).add_to(m)

    for _, row in gangnam_df.iterrows():
        folium.CircleMarker(
            location=[row['위도'], row['경도']],
            radius=5,
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.9
        ).add_to(m)

    folium.CircleMarker(
        location=[37.5005851, 127.0444115],
        radius=7,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.9
    ).add_to(m)

    folium.PolyLine(
        path[:st.session_state.path_step],
        color='lightblue',
        weight=5,
        opacity=0.9
    ).add_to(m)

    folium.Circle(
        location=[37.5049600, 127.0481000],
        radius=300,
        color='lightblue',
        fill=True,
        fill_color='lightblue',
        fill_opacity=0.3
    ).add_to(m)

    st_folium(m, width=1200, height=700)

    if st.session_state.path_step < len(path):
        time.sleep(0.5)
        st.session_state.path_step += 1
        st.rerun()

# 🔽 하단 버튼
if 1 <= st.session_state.story_stage <= 5:
    col1, col2, col3 = st.columns([1, 8, 1])
    with col1:
        if st.session_state.story_stage > 1:
            st.button("⬅ BACK", on_click=prev_stage)
    with col3:
        if st.session_state.story_stage < 5:
            st.button("NEXT ➡", on_click=next_stage)