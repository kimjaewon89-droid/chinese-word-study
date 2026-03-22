import streamlit as st
import os

# --- 페이지 설정 ---
# 레이아웃을 'wide'로 설정하여 갤러리처럼 넓게 보이게 합니다.
st.set_page_config(page_title="정원이 성장 대시보드", page_icon="👶", layout="wide")

# --- 메인 타이틀 ---
st.title("👶 정원이의 성장 갤러리")
st.write("---") # 구분선

# --- 설정값 ---
IMAGE_DIR = "images" # 이미지 폴더 이름
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.webp') # 지원하는 확장자
PROFILE_KEYWORD = "main_profile" # 가장 먼저 보여줄 프로필 사진의 키워드

# 이미지 폴더가 존재하는지 확인
if os.path.exists(IMAGE_DIR):
    # 1. 폴더 안의 모든 파일 목록 가져오기
    all_files = os.listdir(IMAGE_DIR)
    
    # 2. 지원하는 이미지 확장자만 필터링 (대소문자 구분 안 함)
    image_files = [f for f in all_files if f.lower().endswith(VALID_EXTENSIONS)]

    if not image_files:
        st.info("📷 아직 'images' 폴더에 사진이 없습니다. 정원이 사진을 올려주세요!")
    else:
        # --- 🧩 마법의 정렬 로직 (Captain의 지시사항) ---
        
        # 메인 프로필 사진과 나머지 사진을 분리할 리스트 준비
        profile_file = None
        other_files = []

        for f in image_files:
            # 파일 이름에 'main_profile'이 포함되어 있는지 확인 (확장자 제외한 이름만 확인)
            filename_no_ext = os.path.splitext(f)[0]
            
            if PROFILE_KEYWORD in filename_no_ext:
                profile_file = f # 프로필 사진으로 간주
            else:
                other_files.append(f) # 나머지 사진들

        # 3. 나머지 사진들은 가나다순(알파벳순)으로 정렬
        other_files.sort()

        # 4. 최종 리스트 구성: 프로필 사진을 맨 앞에 넣고, 나머지를 붙임
        final_ordered_files = []
        
        # 프로필 사진이 존재할 때만 맨 앞에 추가
        if profile_file:
            final_ordered_files.append(profile_file)
            
        final_ordered_files.extend(other_files)


        # --- 🖼️ 갤러리 화면 표시 ---
        
        # 사진을 3열(Column)로 예쁘게 배치
        cols = st.columns(3) 
        
        for idx, img_file in enumerate(final_ordered_files):
            # idx % 3을 통해 0, 1, 2번 열에 차례대로 배정
            with cols[idx % 3]:
                img_path = os.path.join(IMAGE_DIR, img_file)
                
                # 사진 이름(확장자 제외)을 아래 캡션으로 사용
                # 단, 프로필 사진은 특별한 캡션을 달아줌
                caption_text = os.path.splitext(img_file)[0]
                if PROFILE_KEYWORD in caption_text:
                    caption_text = "💖 우리 집 주인공 💖"
                
                # 최종 이미지 표시
                st.image(img_path, caption=caption_text, use_column_width=True)
                st.write("") # 사진 간 간격 만들기

else:
    st.error(f"⚠️ 깃허브 최상위에 '{IMAGE_DIR}' 폴더를 찾을 수 없습니다. 폴더를 만들어주세요.")
