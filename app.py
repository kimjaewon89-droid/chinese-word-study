import streamlit as st
import os

# --- 페이지 설정 ---
st.set_page_config(page_title="정원이 성장 대시보드", page_icon="👶")

# --- 메인 타이틀 ---
st.title("👶 정원이의 성장 일기")

# --- 방법 A: 고정 프로필 사진 표시 ---
# 이미지가 저장된 폴더 경로
IMAGE_DIR = "images"
# 표시할 특정 이미지 파일명
PROFILE_IMAGE_NAME = "main_profile.jpg" # 💡 깃허브 images 폴더에 이 이름의 파일이 있어야 합니다.

# 이미지 파일의 전체 경로 생성
profile_path = os.path.join(IMAGE_DIR, PROFILE_IMAGE_NAME)

# 이미지 파일이 실제로 존재하는지 확인 후 표시
if os.path.exists(profile_path):
    # 💡 st.image 사용법
    # caption: 사진 아래 설명, use_column_width: 화면 너비에 맞춤
    st.image(profile_path, caption="우리 집 공주님, 정원이 💖", use_column_width=True)
else:
    st.warning(f"⚠️ '{profile_path}' 파일을 찾을 수 없습니다. 깃허브 이미지를 확인해주세요.")
