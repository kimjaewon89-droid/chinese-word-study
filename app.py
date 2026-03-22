import streamlit as st
import os

# --- 1. 페이지 기본 설정 ---
st.set_page_config(page_title="정원이 성장 대시보드", page_icon="👶", layout="wide")

st.title("👶 정원이의 성장 갤러리")
st.write("---")

# --- 2. 누구나 볼 수 있는 갤러리 영역 ---
IMAGE_DIR = "images"
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
PROFILE_KEYWORD = "main_profile"

# 사진을 띄우는 로직
if os.path.exists(IMAGE_DIR):
    all_files = os.listdir(IMAGE_DIR)
    image_files = [f for f in all_files if f.lower().endswith(VALID_EXTENSIONS)]

    if not image_files:
        st.info("📷 아직 사진이 없습니다. 정원이 사진을 올려주세요!")
    else:
        profile_file = None
        other_files = []

        # 프로필 사진과 일반 사진 분류
        for f in image_files:
            if PROFILE_KEYWORD in os.path.splitext(f)[0]:
                profile_file = f
            else:
                other_files.append(f)

        other_files.sort() # 일반 사진은 이름순 정렬
        final_ordered_files = []
        if profile_file:
            final_ordered_files.append(profile_file)
        final_ordered_files.extend(other_files)

        # 3열로 사진 예쁘게 배치
        cols = st.columns(3) 
        for idx, img_file in enumerate(final_ordered_files):
            with cols[idx % 3]:
                img_path = os.path.join(IMAGE_DIR, img_file)
                caption_text = os.path.splitext(img_file)[0]
                
                if PROFILE_KEYWORD in caption_text:
                    caption_text = "💖 우리 집 주인공 💖"
                
                st.image(img_path, caption=caption_text, use_column_width=True)
                st.write("")

# --- 3. 가족 전용 사진 업로드 영역 (비밀번호 보호) ---
st.write("---")
st.subheader("📸 사진 추가하기 (가족 전용)")

SECRET_PASSWORD = "0509" # 원하는 비밀번호로 바꿔주세요

# 비밀번호 입력창 (입력 시 *** 로 가려짐)
upload_pwd = st.text_input("업로드 비밀번호를 입력하세요:", type="password")

# 비밀번호가 맞을 때만 업로드 기능이 화면에 나타남
if upload_pwd == SECRET_PASSWORD:
    uploaded_file = st.file_uploader("정원이 사진 선택 (jpg, png)", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        if st.button("갤러리에 올리기"):
            if not os.path.exists(IMAGE_DIR):
                os.makedirs(IMAGE_DIR)
                
            save_path = os.path.join(IMAGE_DIR, uploaded_file.name)
            
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.success("사진이 성공적으로 올라갔습니다! 키보드의 'F5'를 누르거나 화면을 새로고침 해주세요.")
            
elif upload_pwd != "":
    st.error("비밀번호가 틀렸습니다. 다시 확인해주세요.")
