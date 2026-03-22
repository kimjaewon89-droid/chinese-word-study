import streamlit as st
import os

# --- (기존 페이지 설정 및 타이틀 코드는 그대로 유지) ---

# --- 🔒 비밀번호 및 업로드 영역 ---
st.write("---")
st.subheader("📸 정원이 사진 올리기 (가족 전용)")

# 1. 미리 설정해 둘 비밀번호 (원하는 비밀번호로 변경하세요)
SECRET_PASSWORD = "정원이천사" 

# 2. 비밀번호 입력창 (글자가 가려지도록 type="password" 설정)
upload_pwd = st.text_input("0509", type="password")

# 3. 비밀번호가 맞을 때만 업로드 창 띄우기
if upload_pwd == SECRET_PASSWORD:
    st.success("인증 완료! 사진을 업로드할 수 있습니다.")
    
    # 파일 업로더 활성화
    uploaded_file = st.file_uploader("정원이 사진 선택 (jpg, png)", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        # 업로드 버튼 만들기
        if st.button("갤러리에 사진 추가하기"):
            # 저장할 폴더가 없으면 에러가 나지 않게 확인
            if not os.path.exists("images"):
                os.makedirs("images")
                
            # 사진이 저장될 최종 경로 생성 (예: images/baby_photo.jpg)
            save_path = os.path.join("images", uploaded_file.name)
            
            # 파이썬으로 파일 저장하기
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.success(f"'{uploaded_file.name}' 사진이 성공적으로 저장되었습니다! 화면을 새로고침 해주세요.")
            
elif upload_pwd != "":
    st.error("비밀번호가 일치하지 않습니다.")

# --- (이 아래부터는 기존의 갤러리 화면 표시 코드를 배치하시면 됩니다) ---
