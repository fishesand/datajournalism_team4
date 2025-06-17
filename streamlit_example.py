import streamlit as st
st.set_page_config(layout="wide")
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

# 간단한 Streamlit 마크다운 제목으로 먼저 확인
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 1. 폰트 경로 설정
font_path = "data/강원교육튼튼.ttf"
font_prop = font_manager.FontProperties(fname=font_path)

# 2. 그래프 영역 설정 (배경 없음)
fig, ax = plt.subplots(figsize=(8, 3))

# 3. 텍스트 추가
ax.text(0.5, 0.6, '정신건강', fontproperties=font_prop,
        fontsize=36, color='#FF6F00', ha='center', va='center')

ax.text(0.5, 0.3, '수도권만의 권리인가요?', fontproperties=font_prop,
        fontsize=20, color='black', ha='center', va='center')

# 4. 축/테두리 제거
ax.axis('off')

# 5. Streamlit에 출력
st.pyplot(fig)





# HTML 렌더링은 줄이거나 검증된 구조만 사용
st.markdown("""
<div style="color: #1e1e1e; font-family: 'Segoe UI', sans-serif; padding: 10px 20px; text-align: center;">

  <div style="font-size: 28px; font-weight: bold; color: #FF5722; margin-bottom: 10px;">
    우리나라 국민의 1/3은
  </div>

  <div style="font-size: 22px; margin-bottom: 30px;">
    ‘중간 수준 이상의 우울감’을 경험하고 있습니다.
  </div>

  <div style="font-size: 13px; color: #888888; margin-bottom: 40px;">
    출처: ‘정신건강 증진과 위기 대비를 위한 일반인 조사’<br>
    (서울대 보건대학원 BK21 건강재난 통합대응을 위한 교육연구단, 2025-05-07)
  </div>

  <div style="font-size: 20px; margin-bottom: 20px;">
    <strong style="color: #FF5722;">그럼에도</strong>, 우리 사회에서 <strong>정신건강</strong>은 늘 뒷전입니다.
  </div>

  <div style="font-size: 20px; margin-bottom: 30px;">
    <strong style="color: #FF5722;">지방, 농어촌 지역</strong>의 정신건강은 더더욱 방치되어 있습니다.
  </div>

  <div style="font-size: 28px; font-weight: bold; color: #FF5722;">
    본 프로젝트의 목표는<br>
    <span style="color: #1e1e1e;">정신건강증진시설의 지역 격차</span>를 시각화하는 것입니다.
  </div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<!-- 공백과 세로선 영역 -->
<div style="position: relative; height: 80px; margin: 60px 0;">

  <!-- 세로선: 가운데 정렬 -->
  <div style="
    position: absolute;
    left: 50%;
    top: 10px;
    transform: translateX(-50%);
    width: 2px;
    height: 150px;
    background-color: #FF5722;
    opacity: 0.7;
  "></div>

</div>
""", unsafe_allow_html=True)


import streamlit as st
import json
import pandas as pd
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time


# 데이터 불러오기
gangnam_df = pd.read_excel("data/gangnam_juso.xlsx").dropna(subset=['위도', '경도'])
seolleung_df = pd.read_excel("data/seoulleung_juso.xlsx").dropna(subset=['위도', '경도'])
seolleung_hospitals = gangnam_df[gangnam_df['주소'].str.contains("선릉로", na=False)]

import pandas as pd

boseong_df = pd.DataFrame({
    '기관명': ['벌교삼호병원', '보성제일병원'],
    '주소': ['전남 보성군 남하로 12', '전남 보성군 송재로 59-2'],
    '위도': [34.8337591, 34.763154],
    '경도': [127.3459238, 127.073384]
})

# 1단계: 인물 소개
import base64

# 이미지 파일 불러와서 base64 인코딩
with open("data/A씨.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

# HTML 코드 삽입
st.markdown(f"""
<div style="display: flex; justify-content: center; margin-top: 40px;">
    <div style="text-align: center;">
        <img src="data:image/png;base64,{encoded}" style="max-width: 240px; width: 100%;" />
        <div style="margin-top: 20px; font-size: 24px; line-height: 1.6;">
            강남구에 사는 A씨가 있습니다.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)




# 2단계: 전체 강남구 지도
import base64

# 이미지 파일 base64 인코딩
with open("data/1.png", "rb") as image_file:
    encoded_img = base64.b64encode(image_file.read()).decode()

# HTML로 이미지 + 텍스트 중앙 정렬 표시
st.markdown(f"""
<div style="display: flex; justify-content: center; margin-top: 40px;">
    <div style="text-align: center;">
        <img src="data:image/png;base64,{encoded_img}" style="max-width: 1000px; width: 100%;" />
        <div style="margin-top: 30px; font-size: 24px; line-height: 1.6;">
            강남구에는 정신병원이 102곳,<br>
            정신재활센터는 1곳 있습니다.<br><br>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# 3단계: 선릉로 강조 지도
import base64

# 이미지 파일 base64 인코딩
with open("data/2.png", "rb") as image_file:
    encoded_img = base64.b64encode(image_file.read()).decode()

# HTML로 이미지 + 텍스트 중앙 정렬 표시
st.markdown(f"""
<div style="display: flex; justify-content: center; margin-top: 40px;">
    <div style="text-align: center;">
        <img src="data:image/png;base64,{encoded_img}" style="max-width: 1000px; width: 100%;" />
        <div style="margin-top: 30px; font-size: 24px; line-height: 1.6;">
            A씨가 거주하는 선릉로에만 <br>
            정신병원이 12곳 있습니다.<br><br>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


#4단계
import base64

# 이미지 파일 base64 인코딩
with open("data/3.png", "rb") as image_file:
    encoded_img = base64.b64encode(image_file.read()).decode()

# 이미지 + 텍스트 중앙 정렬
st.markdown(f"""
<div style="display: flex; justify-content: center; margin-top: 40px;">
    <div style="text-align: center;">
        <img src="data:image/png;base64,{encoded_img}" style="max-width: 1000px; width: 100%;" />
        <div style="margin-top: 30px; font-size: 24px; line-height: 1.6;">
            A씨의 집에서 정신병원까지 가기 위해서는 얼마나 걸릴까요?<br><br><br>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

##
import base64

# 이미지 파일 base64 인코딩
with open("data/4.png", "rb") as image_file:
    encoded_img = base64.b64encode(image_file.read()).decode()

# 이미지와 텍스트를 HTML로 중앙 정렬
st.markdown(f"""
<div style="display: flex; justify-content: center; margin-top: 40px;">
    <div style="text-align: center;">
        <img src="data:image/png;base64,{encoded_img}" style="max-width: 1000px; width: 100%;" />
        <div style="margin-top: 30px; font-size: 24px; line-height: 1.6;">
            A씨는 집 근처 정신병원들이 모여있는 반경까지 이동하는 데<br>
            걸어서 12분이 채 걸리지 않습니다.<br>
            많은 병원들이 분포되어 있기 때문에,<br>
            선택지의 폭도 넓습니다.<br><br><br>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)



#5단계
import base64

# 이미지 파일 base64 인코딩
with open("data/A씨.png", "rb") as image_file:
    encoded_img = base64.b64encode(image_file.read()).decode()

# 중앙 정렬된 이미지 + 텍스트 표시
st.markdown(f"""
<div style="display: flex; justify-content: center; margin-top: 40px;">
    <div style="text-align: center;">
        <img src="data:image/png;base64,{encoded_img}" style="max-width: 240px; width: 100%;" />
        <div style="margin-top: 30px; font-size: 24px; line-height: 1.6;">
            한편, 전라남도 보성군에 사는 B씨가 있습니다.<br><br>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


##
import base64

# 이미지 파일 base64 인코딩
with open("data/5.png", "rb") as image_file:
    encoded_img = base64.b64encode(image_file.read()).decode()

# 이미지 + 텍스트 중앙 정렬 표시
st.markdown(f"""
<div style="display: flex; justify-content: center; margin-top: 40px;">
    <div style="text-align: center;">
        <img src="data:image/png;base64,{encoded_img}" style="max-width: 1000px; width: 100%;" />
        <div style="margin-top: 30px; font-size: 24px; line-height: 1.6;">
            보성군에는 정신병원이 단 2곳뿐입니다.<br><br>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

##
import base64

# 이미지 base64 인코딩
with open("data/6.png", "rb") as image_file:
    encoded_img = base64.b64encode(image_file.read()).decode()

# HTML로 이미지 + 텍스트 중앙 정렬
st.markdown(f"""
<div style="display: flex; justify-content: center; margin-top: 40px;">
    <div style="text-align: center;">
        <img src="data:image/png;base64,{encoded_img}" style="max-width: 1000px; width: 100%;" />
        <div style="margin-top: 30px; font-size: 24px; line-height: 1.6;">
            B씨가 거주하는 지역에도 병원이 있긴 하지만,<br>
            같은 보성군 안에 있는 병원까지도<br>
            <strong>자동차로는 약 30분,</strong><br>
            <strong>버스로는 무려 1시간 40분이 걸립니다.</strong><br><br>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


##
import base64

# 이미지 base64 인코딩
with open("data/7.png", "rb") as image_file:
    encoded_img = base64.b64encode(image_file.read()).decode()

# HTML로 이미지 + 텍스트 중앙 정렬
st.markdown(f"""
<div style="display: flex; justify-content: center; margin-top: 40px;">
    <div style="text-align: center;">
        <img src="data:image/png;base64,{encoded_img}" style="max-width: 1000px; width: 100%;" />
        <div style="margin-top: 30px; font-size: 24px;">
            보성군 내 병원 접근이 어려운 B씨는<br>
            결국 순천시까지 나가야 할지도 모릅니다.<br>
            차로 약 1시간, 버스로는 2시간 넘게 걸리는 거리입니다.<br><br>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="background-color: #e3f2fd; padding: 20px; border-left: 6px solid #1976d2; border-radius: 8px; margin-bottom: 25px; font-size: 18px; max-width: 100%; text-align: center;">
    이러한 문제는 단지 A씨와 B씨 개인의 문제가 아닙니다. <br>
    현재 우리 사회에서는 정신건강증진시설에 지역 간 격차가 존재하며, 이는 많은 이들의 삶에 영향을 미치고 있습니다. <br>
    이에 따라 정신건강증진시설의 개념과 관련 통계를 살펴보고, <br>
    지역 격차가 실제로 어떻게 나타나는지 지도를 통해 확인한 뒤, <br>
    이를 해소하기 위한 보건복지부의 의료 개혁 방향에 대해 논의하고자 합니다.<br>
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

<div style="background-color: #e3f2fd; padding: 20px; border-left: 6px solid #1976d2; border-radius: 8px; margin-bottom: 25px; font-size: 18px;">
    「정신건강증진 및 정신질환자 복지서비스 지원에 관한 법률」 제3조 제4호에 따르면,  
    <strong>‘정신건강증진시설’이란 정신의료기관, 정신요양시설 및 정신재활시설</strong>을 말합니다.  
    이들 시설을 중심으로 <strong>국가와 지방자치단체는 정신건강의 예방부터 조기발견, 치료, 재활, 사회복귀까지 전 과정을 포괄하는 서비스를 계획 및 시행</strong>하고 있습니다.
</div>

<div style="background-color: #f9f9f9; padding: 25px; border-radius: 12px; line-height: 1.8; font-size: 18px;">
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
            
<div style="background-color: #fff8e1; padding: 20px; border-left: 6px solid #fbc02d; border-radius: 8px; margin-top: 30px; font-size: 18px; line-height: 1.7;">
    본 프로젝트는 전체 정신건강증진시설 중에서 <strong>가장 일반적인 대상층을 가진 정신병원과 정신재활시설</strong>에 주목하여 분석을 진행하였습니다.  
    이는 노인복지시설이나 트라우마센터처럼 특정 계층을 대상으로 한 시설보다,  
    <strong>보다 폭넓은 인구에게 직접적인 영향을 미치는 기반 시설</strong>로 판단했기 때문입니다.
</div>
""", unsafe_allow_html=True)

import matplotlib.font_manager as fm
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import font_manager
from PIL import Image
import base64
from io import BytesIO

# 폰트 설정
font_path = "data/NanumGothic.ttf"
font_prop = font_manager.FontProperties(fname=font_path)

# 데이터 로드 및 전처리
facility_df = pd.read_excel("data/facility.xlsx")
population_df = pd.read_excel("data/population.xlsx")

facility_df.columns = facility_df.iloc[1]
facility_df = facility_df[2:].copy()
facility_df.rename(columns={'시도별(1)': '시도'}, inplace=True)

medical_cols = ['종합병원 정신과', '병원 정신과', '정신병원_국립', '정신병원_공립', '정신병원_사립',
                '요양병원 정신과', '한방병원 정신과', '의원 정신과', '한의원 정신과']
for col in medical_cols:
    facility_df[col] = (
        facility_df[col].astype(str).str.replace('-', '0').str.replace(',', '').astype(float)
    )
facility_df['총의료기관수'] = facility_df[medical_cols].sum(axis=1)

population_df = population_df[['sgg', 'population']].dropna()
population_df.rename(columns={'sgg': '시도'}, inplace=True)

merged_df = pd.merge(facility_df, population_df, on='시도')
merged_df = merged_df[merged_df['시도'] != '전국']
merged_df['인구/의료기관'] = merged_df['population'] / merged_df['총의료기관수']

# 좌우 레이아웃
st.markdown("<h2 style='text-align: center; margin-top: 40px;'>시도별 의료기관 1곳이 담당하는 인구 수</h2>", unsafe_allow_html=True)

import matplotlib.pyplot as plt
import base64
from io import BytesIO

# 그래프 생성
sorted_df = merged_df.sort_values(by='인구/의료기관', ascending=True)
fig, ax = plt.subplots(figsize=(7, 4))
x = sorted_df['시도']
x_idx = range(len(x))
ax.bar(x_idx, sorted_df['인구/의료기관'], width=0.4, color='skyblue')
ax.set_xticks(x_idx)
ax.set_xticklabels(x, rotation=60, ha='right', fontsize=6, fontproperties=font_prop)
ax.set_ylabel("인구 / 의료기관 수", fontproperties=font_prop, fontsize=8)
ax.set_xlabel("시도", fontproperties=font_prop, fontsize=8)
fig.tight_layout()

# base64로 변환
buf = BytesIO()
fig.savefig(buf, format="png", bbox_inches="tight")
buf.seek(0)
encoded_graph = base64.b64encode(buf.read()).decode()

# HTML로 그래프 + 글 정렬
st.markdown(f"""
<div style="display: flex; flex-direction: row; justify-content: center; align-items: center; gap: 50px; margin-top: 40px; flex-wrap: wrap;">
    <div style="flex: 1;">
        <img src="data:image/png;base64,{encoded_graph}" style="max-width: 100%; height: auto;" />
    </div>
    <div style="flex: 1; font-size: 18px; line-height: 1.8;">
        <p><strong>- 본 그래프는 2023년 기준으로, 각 시도별 정신건강의학과 의료기관 한 곳이 평균적으로 담당하는 인구 수를 나타낸 것입니다.</strong></p>
        <p>- 막대의 높이가 클수록 해당 지역의 의료기관 한 곳이 감당해야 하는 인구 수가 많다는 것을 의미하며, 이는 곧 의료 접근성이 낮고 정신건강 관련 인프라가 부족하다는 사실을 시사합니다.</p>
        <p>- 서울특별시의 경우, 의료기관 한 곳당 약 14,000명을 담당하는 반면, 경상북도는 한 곳당 약 37,000명을 담당하고 있어, 지역 간 약 2.5배에 달하는 격차가 존재합니다.</p>
        <p>- 전반적으로 수도권과 광역시에 비해, 충청도, 전라도, 경상도 등 비수도권 지역일수록 인구 대비 의료기관 수가 적은 경향을 보입니다. 이러한 현상은 정신건강 분야에서의 지역 불균형 문제를 드러내며, 보다 균형 잡힌 정책적 개입이 요구된다고 할 수 있습니다.</p>
    </div>
</div>
""", unsafe_allow_html=True)


# 이미지 → base64 변환 함수
# 병원/사람 시각화 함수
def image_to_base64(img, width):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode()
    return f"<img src='data:image/png;base64,{img_b64}' width='{width}' style='margin:2px;'/>"

def render_region(title, num_hospitals, people_per_hospital, people_count_text):
    st.markdown(f"<h4 style='text-align: center;'>{title}</h4>", unsafe_allow_html=True)
    hospital_html = "".join([image_to_base64(hospital_img, width=80) for _ in range(num_hospitals)])
    st.markdown(f"<div style='text-align: center;'>{hospital_html}</div>", unsafe_allow_html=True)
    person_html = "".join([image_to_base64(person_img, width=40) for _ in range(people_per_hospital)])
    st.markdown(f"<div style='text-align: center; margin-top:5px;'>{person_html}</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size:24px; margin-top:5px;'>{people_count_text}</p>", unsafe_allow_html=True)

# 병원/사람 이미지 불러오기
hospital_img = Image.open("data/hospital.png")
person_img = Image.open("data/person.png")

# 제목
st.markdown("<h2 style='text-align: center; margin-top: 40px;'><br><br>서울과 경상북도 비교<br></h2>", unsafe_allow_html=True)

# 좌우 분할
left_col, right_col = st.columns([1, 1])

# 왼쪽: 이미지 시각화
with left_col:
    render_region("서울", num_hospitals=1, people_per_hospital=2, people_count_text="14,437명")
    render_region("경상북도", num_hospitals=1, people_per_hospital=5, people_count_text="36,998명 (약 2.5배)")

# 오른쪽: 설명 줄글
with right_col:
    st.markdown("""
    <div style="background-color: #f4f6f8; padding: 24px; border-left: 6px solid #1976d2;
                border-radius: 8px; margin-top: 50px; font-size: 18px; line-height: 1.9; text-align: left;">
        -대표적으로 서울과 경상북도를 시각화하여 비교해보면 다음과 같습니다. <br>
        -서울은 한 개의 병원 당 약 14,437명을 담당하고 있으나, 경상북도의 병원은 약 36,998명을 담당하고 있습니다.<br>
        -이는 경북의 의료기관 1곳이 서울보다 평균 2.5배 더 많은 인구를 감당하고 있는 셈입니다.<br>
        -앞서 살펴본 그래프와 같이 이러한 수치는 두 지역 간 의료 인프라의 밀도 차이를 드러내며, 정신건강 분야에서의 지역 불균형 문제를 보다 명확히 보여주는 사례로 해석할 수 있습니다.
    </div>
    """, unsafe_allow_html=True)

# 제목
st.markdown("<h2 style='text-align: center; margin-top: 80px;'><br>2018~2023 전국 정신건강증진 시설 수 변화<br></h2>", unsafe_allow_html=True)

# 좌우 분할
left_col, right_col = st.columns([1, 1])

# 왼쪽: 선그래프
with left_col:
    
    df_year = pd.read_excel("data/2018_2023_정신건강시설.xlsx")
    df_cleaned = df_year.iloc[1:4].copy()
    df_cleaned.columns = ['종류', 2018, 2019, 2020, 2021, 2022, 2023]
    df_cleaned.set_index('종류', inplace=True)
    df_cleaned = df_cleaned.astype(int).T
    df_cleaned.index = df_cleaned.index.astype(int)

    fig, ax = plt.subplots(figsize=(6, 3))
    for col in df_cleaned.columns:
        ax.plot(df_cleaned.index, df_cleaned[col], marker='o', label=col)

    ax.set_xlabel("연도", fontsize=9, fontproperties=font_prop)
    ax.set_ylabel("시설 수", fontsize=9, fontproperties=font_prop)
    ax.set_xticks(df_cleaned.index)
    ax.set_xticklabels(df_cleaned.index, fontproperties=font_prop, fontsize=8)
    ax.tick_params(axis='y', labelsize=7)
    ax.legend(
        prop=font_prop, fontsize=4, loc='upper left',
        markerscale=0.5, labelspacing=0.2, handlelength=0.8,
        borderpad=0.2, handletextpad=0.3, borderaxespad=0.2
    )
    ax.grid(True)
    st.pyplot(fig)

# 오른쪽: 설명 줄글
with right_col:
    st.markdown("""
    <div style="background-color: #f4f6f8; padding: 24px; border-left: 6px solid #1976d2;
                border-radius: 8px; margin-top: 15px; font-size: 18px; line-height: 1.9; text-align: left;">
        -본 그래프는 2018년부터 2023년까지 정신건강 관련 의료기관과 정신재활시설 수의 변화를 보여줍니다. <br>
        -의료기관은 꾸준히 증가하고 있으며, 재활시설도 일정 수준 유지되고 있음을 확인할 수 있습니다. <br>
        -그러나 앞서 살펴본 지역별 의료기관 당 인구수 분포를 함께 고려하면, 이러한 인프라의 양적 확대가 곧 지역 간 격차 해소로 이어지지는 않는다는 사실을 알 수 있습니다. <br>
        -즉, 의료기관이나 재활시설이 늘어나는 추세에도 불구하고, 특정 지역에서는 여전히 의료 접근성이 낮고 과도한 부담이 집중되고 있습니다. <br>
        -이는 단순한 시설 수의 증가만으로는 지역 불균형 문제를 해결할 수 없으며, 인프라의 ‘분포’와 ‘배치’ 또한 정책적으로 고려되어야 함을 시사합니다.
    </div>
    """, unsafe_allow_html=True)



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

st.markdown("""
<div style="background-color: #e3f2fd; padding: 20px; border-left: 6px solid #1976d2; border-radius: 8px; margin-top: 30px; font-size: 16px; line-height: 1.7;">
   그렇다면 전국의 정신건강증진시설은 어떻게 분포되어있을까요? 인구수가 유사한 지역 4곳(강남구, 김해시, 강원도, 전라남도)을 지도로 시각화해보았습니다. 
</div>
""", unsafe_allow_html=True)

st.write("")

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

    elif '강남구' in selection:
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
            
            **지역별 정신병원 및 정신재활센터 수:** 11개/1개
            """)

            

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
            **지역 총인구:** 532,792명  
            
            **지역별 정신병원 및 정신재활센터 수:** 11개/1개
            """)


    elif '서울특별시' in selection:
        with col:
            st.markdown("""
            **대상 지역:** 서울특별시 강남구       
            **지역 총면적:** 39.55km²      
            **지역 총인구:** 556,822명
                        
            **지역별 정신병원 및 정신재활센터 수:** 102개/1개
            """)
st.markdown("""
<div style="background-color: #e3f2fd; padding: 20px; border-left: 6px solid #1976d2; border-radius: 8px; margin-top: 30px; font-size: 16px; line-height: 1.7;">
지도에서 볼 수 있듯이, 수도권의 중심지인 강남구에는 정신의료기관과 정신재활시설이 밀집해 있는 반면, 일부 지방 지역 3곳에는 이들 시설이 현저히 부족한 실정입니다. 이는 지역 간 정신보건 서비스 접근성에 뚜렷한 불균형이 존재함을 시사하며, 정신건강 격차 해소를 위한 정책적 개입이 요구되는 지점입니다.

</div>
""", unsafe_allow_html=True)


     
#제목
st.markdown(
    """
    <h1 style='text-align: center; font-size: 40px; margin-top: 60px;'>IV. 보건복지부 의료개혁 실행방안 텍스트 분석</h1>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div style="background-color: #e3f2fd; padding: 20px; border-left: 6px solid #1976d2; border-radius: 8px; margin-top: 30px; font-size: 16px; line-height: 1.7;">
  앞선 논의들을 바탕으로, 현재의 의료 정책 방향을 점검하고자 보건복지부에서 발행한 의료 개혁 1차, 2차 자료집의 텍스트 분석을 진행했습니다. 
</div>
""", unsafe_allow_html=True)

st.markdown("""
<h2 style='text-align: center; margin-top: 40px;'>의료개혁 1차 · 2차 실행방안: 지역 격차 대응 비교</h2>
            """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

# ------------ 의료개혁 1차 ------------
with col1:
    st.header("의료개혁 1차 실행방안")
    st.markdown("### 핵심 내용 요약")
    st.markdown("""
- **지역완결 의료체계 구축**
  - 국립대병원, 지방의료원, 지역 종합병원 중심 기능 강화
- **지역 전공의 배정 확대**
  - 수도권·비수도권 5:5 배정, 지역 친화적 배치 방식
- **지역필수의사제 도입**
  - 일정 기간 지역 근무 시 수당, 주거 지원, 해외 연수 등 인센티브
- **지역의료발전기금 신설**, ‘지역의료지원법’ 제정 추진
- **의료권 기준 개편**
  - 행정구역이 아닌 진료권 기반 체계화
""")

    with st.expander("원문 발췌 보기"):
        st.markdown("""
- “지역완결 의료체계 구축: 국립대병원 등 권역 책임의료기관 육성 및 기능 강화, 지방의료원 역량 강화, 지역 종합병원 집중 지원”  
- “의료협력 네트워크 구축 (의뢰·회송 시스템, EMR 정보 공유 등)”  
- “계약형 지역필수의사제 도입: 일정 기간 지역 병원 근무 시 월 400만원 수당, 정주 여건 지원, 해외 연수 기회 제공”  
- “‘지역의료지원법’ 제정 추진 및 지역의료발전기금 신설”
- “병상 수급 및 진료권 체계화 (행정구역보다 실제 진료권 기준으로 재편)”
        """)

# ------------ 의료개혁 2차 ------------
with col2:
    st.header("의료개혁 2차 실행방안")

    st.markdown("### 핵심 내용 요약")
    st.markdown("""
- **포괄 2차 종합병원** 집중 지원 (3년간 2조 원 투자)
- **지방의료원 인프라 현대화**, 진료 포괄성 강화
- **‘지역수가’ 도입**: 의료취약지에 수가 가산
- **일차의료 혁신 시범사업**: 주치의 중심 예방·관리 체계
- **지역 진료협력 네트워크 확대**
  - 암, 심뇌, 분만, 중환자 등 분야별 협력 시스템 구축
- **지자체 자율 지역의료혁신 시범사업** 추진
""")

    with st.expander("원문 발췌 보기"):
        st.markdown("""
- “포괄 2차 종합병원 지원사업: 상급종합병원과 협력하여 지역 내 의료수요 대부분 대응 가능토록 집중 지원”  
- “지역수가 본격 적용: 의료수요·공급 취약지역에 추가 가산 적용”  
- “일차의료 혁신 시범사업: 통합·지속적 건강관리 위한 의원급 기능 강화”  
- “상급종합병원-2차병원-일차의료 협력 체계 확대, 진료협력 인력 지원, 중환자 네트워크 도입 등”  
- “‘지역의료지도’ 활용 및 지자체 중심 지역문제 해결형 시범사업 추진”
        """)

st.markdown("---")
st.caption("출처: 보건복지부 『의료개혁 1차 실행방안』, 『의료개혁 2차 실행방안』")


st.header("1차 → 2차: 차이점")
            
           


col1, col2 = st.columns(2)

# 왼쪽: 1차 실행방안
with col1:
    st.subheader("1차 실행방안")

    st.markdown("""
**주요 특징**
- 국립대병원, 지방의료원 등 **기본 인프라 확충**
- 지역 전공의 배정 및 **계약형 지역필수의사제** 도입
- **의료지원법 제정**, 진료권 기반 재편 등 **정책 방향 제시**

**의의**
- 지역 필수의료에 대한 **정치적 선언**
- 첫 출발로서의 **의미 있는 재정 투자 계획**

**한계**
- 의료기관의 **역할 분화·기능 정립 부족**
- ‘**구조 개편**’보다는 ‘**지원**’에 머무름
""")

# 오른쪽: 2차 실행방안
with col2:
    st.subheader("2차 실행방안")

    st.markdown("""
**주요 특징**
- **포괄 2차 종합병원** 지정 및 24시간 진료 역량 강화
- **지역수가 도입**: 의료취약지에 수가 가산
- **진료협력 네트워크 구축** (암, 심뇌, 분만, 중환자 등)
- **지자체 중심 지역의료혁신 시범사업** 운영

**의의**
- **‘돈’이 아닌 ‘구조’** 중심의 지역 격차 해소 방식
- 지역 내 **자율 설계 + 성과 기반 보상체계**

**1차와 달라진 개선점**
- 1차의 큰 그림을 **실행 가능한 세부 시스템으로 구체화**
- 병원 간 역할 분담 → **대형병원 쏠림 완화**
""")
    
st.markdown("---")
st.subheader("한계")

st.markdown(
    """
    정신 건강과 관련된 지역 간 의료 격차에 대한 논의는 여전히 충분히 다뤄지지 않고 있습니다.  
    이는 향후 정신건강 증진시설의 지역 간 불균형 문제를 해결하기 위한 구체적인 정책 마련이 필요함을 시사합니다.
    """
)

# 출처
st.caption("출처: 보건복지부 『의료개혁 1차 실행방안』, 『의료개혁 2차 실행방안』")

st.markdown(
    """
    <div style='text-align: center; font-size: 22px; line-height: 1.8; font-weight: 500; margin-top: 40px;'>
        정신건강증진시설의 지역격차는 분명히 존재합니다.<br>
        지방은 수도권에 비해 접근 가능한 시설의 수가 현저하게 적으며,<br>
        시설까지 이동하는 데의 거리 및 시간도 상당합니다.<br>
        그러나, 사회 전반적인 정책적 차원에서 대응이 제대로 이뤄지지 않는 상황입니다.<br>
        매년 정신병원의 수는 증가하였습니다.<br>
        그러나, 아무도 지방의 시설 현황에는 주목하지 않으며,<br>
        적절한 대응을 위해 노력하지 않습니다.<br>
        ‘정신건강’이라는 의료분야의 소외와, 구조적인 지역격차 문제가 혼합되어<br>
        악순환을 만들고 있습니다.<br><br>
        프로젝트를 마무리하며, 이에 대한 한국 대중의 관심과<br>
        정부의 적절한 대응을 촉구합니다.
    </div>
    """, 
    unsafe_allow_html=True
)

