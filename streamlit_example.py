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
<h2 style='text-align: center; font-size: 40px; margin-top: 60px;'>
    I. 정신건강증진시설의 개념과 기본 통계
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<h2 style='text-align: center; margin-top: 40px;'>정신건강증진시설 소개</h2>

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

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import streamlit as st
import os

# 한글 폰트 설정
font_path = os.path.abspath('data/NanumGothic.ttf')
font_prop = fm.FontProperties(fname=font_path)

# 파일 로딩
facility_df = pd.read_excel('data/facility.xlsx', skiprows=3)  # 앞부분 설명행 3줄 스킵
pop_df = pd.read_excel('data/인구통계.xlsx', header=None)
pop_df.columns = ['지역', '인구']

# 지역명 정리 (인덱스 맞추기용)
regions = ['서울특별시','부산광역시','대구광역시','인천광역시', '광주광역시', '대전광역시','울산광역시','세종특별자치시',
           '경기도','강원특별자치도','충청북도','충청남도','전북특별자치도', '전라남도','경상북도','경상남도','제주특별자치도']

# 필요한 행 필터링
facility_df = facility_df[facility_df.iloc[:, 0].isin(regions)]
facility_df = facility_df.set_index(facility_df.columns[0])
pop_df = pop_df[pop_df['지역'].isin(regions)]
pop_df = pop_df.set_index('지역')

# 정신재활시설 데이터
rehab = facility_df.iloc[:, 5]  # 6번째 컬럼
rehab.name = '정신재활시설'

# 의료기관 전체 (합산)
medical = facility_df.iloc[:, 7:16].sum(axis=1)
medical.name = '의료기관'

# 인구수 추출 (숫자 변환)
population = pop_df['인구'].astype(float)

# 비율 계산 (개수 / 인구)
rehab_ratio = (rehab / population).reindex(regions)
medical_ratio = (medical / population).reindex(regions)

# 데이터프레임 병합
ratio_df = pd.DataFrame({
    '정신재활시설': rehab_ratio,
    '의료기관': medical_ratio
}, index=regions)

# 시각화
fig, ax = plt.subplots(figsize=(12, 6))
ratio_df.plot(kind='bar', ax=ax, color=['#66c2a5', '#fc8d62'])

ax.set_title('시도별 정신재활시설 및 의료기관 비율 (개수/인구)', fontproperties=font_prop)
ax.set_ylabel('시설 수 / 인구 수', fontproperties=font_prop)
ax.set_xlabel('지역', fontproperties=font_prop)
ax.legend(prop=font_prop)
plt.xticks(rotation=45, ha='right', fontproperties=font_prop)

st.pyplot(fig)



# II. 정신건강증진시설의 지역격차 지도
st.markdown("""
<h2 style='text-align: center; font-size: 40px; margin-top: 80px;'>
    II. 정신건강증진시설의 지역격차 지도
</h2>
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
    },
    '서울특별시 (강남구)': {
        'geojson': 'data/hangjeongdong_강남구.geojson',
        'excel': 'data/gangnam_juso.xlsx',
        'target_regions': ['강남구']
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

    


# ✅ 화면 구성
col1, col2 = st.columns(2)
with col1:
    selected_left = st.selectbox("🗺️ 왼쪽 지도 지역 선택", list(options.keys()), key='left')
    render_map(selected_left, col1)

with col2:
    selected_right = st.selectbox("🗺️ 오른쪽 지도 지역 선택", list(options.keys()), key='right')
    render_map(selected_right, col2)

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




