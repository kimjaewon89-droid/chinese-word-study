import streamlit as st

WINDOW_SIZE = 10

data = '''
11 - gua feng - 바람이 불다
11 - xie - 쓰다
11 - kan - 보다
'''

# ===== 데이터 파싱 =====
words = []
for line in data.strip().splitlines():
    num, pinyin, meaning = line.split(" - ")
    words.append({
        "number": num,
        "pinyin": pinyin,
        "meaning": meaning
    })

TOTAL_WORDS = len(words)
TOTAL_WINDOWS = (TOTAL_WORDS - 1) // WINDOW_SIZE + 1

# ===== 세션 상태 =====
if "window_index" not in st.session_state:
    st.session_state.window_index = 0
    st.session_state.unknown = []
    st.session_state.show_answer = False

start = st.session_state.window_index * WINDOW_SIZE
end = start + WINDOW_SIZE
current_window = words[start:end]

if not st.session_state.unknown:
    st.session_state.unknown = current_window.copy()

current_word = st.session_state.unknown[0]

# ===== 진행률 =====
learned = start + (len(current_window) - len(st.session_state.unknown))
progress = learned / TOTAL_WORDS if TOTAL_WORDS else 1.0

st.progress(progress)
st.markdown(
    f"""
    **윈도우:** {st.session_state.window_index + 1} / {TOTAL_WINDOWS}  
    **현재 윈도우 남은 단어:** {len(st.session_state.unknown)}개  
    **전체 진행률:** {progress * 100:.1f}%
    """
)

st.divider()

# ===== 단어 =====
st.markdown(
    f"<h1 style='text-align:center'>{current_word['pinyin']}</h1>",
    unsafe_allow_html=True
)

if st.session_state.show_answer:
    st.markdown(
        f"<h3 style='text-align:center'>{current_word['number']} - {current_word['meaning']}</h3>",
        unsafe_allow_html=True
    )

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("정답 보기"):
        st.session_state.show_answer = True

with col2:
    if st.button("알아요"):
        st.session_state.show_answer = False
        st.session_state.unknown.pop(0)

        if not st.session_state.unknown:
            st.session_state.window_index += 1
            if st.session_state.window_index * WINDOW_SIZE >= TOTAL_WORDS:
                st.success("🎉 모든 단어 학습 완료!")
                st.stop()

            st.session_state.unknown = words[
                st.session_state.window_index * WINDOW_SIZE:
                (st.session_state.window_index + 1) * WINDOW_SIZE
            ].copy()

        st.rerun()

with col3:
    if st.button("몰라요"):
        st.session_state.show_answer = False
        st.session_state.unknown.append(st.session_state.unknown.pop(0))
        st.rerun()
