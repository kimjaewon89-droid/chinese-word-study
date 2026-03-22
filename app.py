import streamlit as st
import os
# app.py 최상단에 위치해야 합니다.
st.set_page_config(
    page_title="정원이 성장 대시보드",
    page_icon="images/main_profile.jpg", # 혹은 저장된 이미지 경로 "images/favicon.png"
    layout="wide"
)

st.title("👶 정원이의 성장 갤러리")
st.write("---")

# --- 2. 누구나 볼 수 있는 갤러리 영역 ---
IMAGE_DIR = "images"
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
PROFILE_KEYWORD = "main_profile"

# 폴더가 없으면 미리 생성
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

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

    other_files.sort() # 일반 사진 정렬
    
    final_ordered_files = []
    if profile_file:
        final_ordered_files.append(profile_file)
    final_ordered_files.extend(other_files)

    # 3열로 사진 예쁘게 배치
    cols = st.columns(3) 
    for idx, img_file in enumerate(final_ordered_files):
        with cols[idx % 3]:
            img_path = os.path.join(IMAGE_DIR, img_file)
            base_name = os.path.splitext(img_file)[0]
            txt_path = os.path.join(IMAGE_DIR, base_name + ".txt") # 짝꿍 텍스트 파일 경로
            
            # --- 💡 캡션 달기 로직 ---
            if PROFILE_KEYWORD in base_name:
                caption_text = "💖 우리 집 주인공 💖"
            elif os.path.exists(txt_path):
                # 텍스트 파일이 있으면 읽어서 캡션으로 사용
                with open(txt_path, "r", encoding="utf-8") as f:
                    caption_text = f.read()
            else:
                # 텍스트 파일이 없는 예전 사진들은 파일명 대신 기본 예쁜 문구 출력
                caption_text = "사랑스러운 정원이 ✨"
            
            st.image(img_path, caption=caption_text, use_column_width=True)
            st.write("")

# --- 3. 가족 전용 사진 업로드 영역 (설명 입력 추가) ---
st.write("---")
st.subheader("📸 사진 추가하기 (엄빠)")

SECRET_PASSWORD = "0509" # 원하는 비밀번호로 유지

upload_pwd = st.text_input("업로드 비밀번호를 입력하세요:", type="password")

if upload_pwd == SECRET_PASSWORD:
    # 💡 사진 아래 들어갈 아빠의 멘트 입력창
    photo_caption = st.text_input("📝 사진 아래에 보여줄 짧은 설명을 적어주세요 (선택):", placeholder="예: 생후 11일, 아빠 심장 녹인 배냇짓!")
    
    uploaded_file = st.file_uploader("정원이 사진 선택 (jpg, png)", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        if st.button("갤러리에 올리기"):
            # 1. 사진 파일 저장
            save_img_path = os.path.join(IMAGE_DIR, uploaded_file.name)
            with open(save_img_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
                
            # 2. 설명란에 글을 적었다면, 동일한 이름의 텍스트(.txt) 파일로 저장
            if photo_caption.strip(): 
                base_name = os.path.splitext(uploaded_file.name)[0]
                save_txt_path = os.path.join(IMAGE_DIR, base_name + ".txt")
                with open(save_txt_path, "w", encoding="utf-8") as f:
                    f.write(photo_caption)
            
            st.success("사진과 설명이 성공적으로 올라갔습니다! 화면을 새로고침(F5) 해주세요.")
            
elif upload_pwd != "":
    st.error("비밀번호가 틀렸습니다. 다시 확인해주세요.")
