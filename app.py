import streamlit as st
import random

st.write("Streamlit app loaded")
# ====== 설정 ======
WINDOW_SIZE = 10
# ==================

data = '''
1 - che -  자동차
1 - chuang hu - 창문@
1 - dong tian - 겨울@
1 - gao -  높다
1 - guan zhe - 닫혀있다@
1 - jia - 집
1 - kai zhe - 열려있다@
1 - qian - 천, 1000
1 - qiu tian - 가을@
1 - shu - 책
1 - ting - 듣다
1 - xiang zi - 상자@
1 - xin - 새롭다 참신하다
1 - yi fu - 옷
1 - zher - 여기에서@
11 - can ting - 식당
11 - chou yan - 담배피다@
11 - chu zu che(1) - 택시@
11 - chun tian - 봄@
11 - ge ge(경) - 형/오빠
11 - gong jiao che(1) - 버스@
11 - gong si - 회사
11 - gua feng - 바람이 분다@
11 - jian shi - 시간
11 - jin tian - 오늘
11 - ka fei - 커피
11 - kai che - 운전하다
11 - qiu tian - 가을@
11 - sha fa - 쇼파
11 - shu bao - 책가방
11 - tian tian - 매일매일
11 - xi gua - 수박
11 - xiang jiao - 바나나@
11 - xing qi - 요일
11 - yi sheng - 의사
11 - zhong jian  - 중간
12 - fei chang - 매우
12 - gong yuan - 공원
12 - hua ping - 꽃병@
12 - xiu xi - 휴식하다
12 - zhong wen - 중국어
13 - Zhou zi - 책상
13 - ji chang - 공항
13 - qian bi - 연필
13 - shen ti - 신체
14 - chao shi - 슈퍼마켓
14 - chi fan - 먹다
14 - gong zuo - 일하다
14 - hua dian - 꽃집@
14 - ji dan - 계란@
14 - kai hui - 회의하다@
14 - pai zhao - 사진찍다@
14 - sheng bing - 병이나다
14 - shu dian - 서점@
14 - yi yuan - 병원
14 - yin yue - 음악
14 - zhu rou - 돼지고기@
2 - cha - 차
2 - chang - 길다
2 - chuan - 배
2 - chuang - 침대
2 - du - 읽다
2 - hai - 여전히, 아직도
2 - hong - 붉다, 벌겋다
2 - ju zi - 귤@
2 - juede - ~라고 생각하다
2 - ku zi - 바지@
2 - mang - 바쁘다
2 - men - 문
2 - pu tao - 포도@
2 - qian mian - 앞@
2 - shen me - 무엇을
2 - shen me shi(2)hou - 언제
2 - xie zi - 신발@
21 - fang jian - 방
21 - pa shan - 등산하다
21 - pang bian - 옆, 측면
21 - tu shu gua(3)n - 도서관
21 - yuan zhu bi(3) - 볼펜@
22 - hui da - 대답하다
22 - li mi - 센티미터
22 - ming tian - 내일
22 - nan ren - 남자
22 - pian yi - 싸다
22 - tong xue - 학우
22 - xue xi - 공부하다
22 - yin hang - 은행
22 - you ju - 우체국
23 - haizi - 아이
23 - hua xue - 스키타다
23 - niu nai - 우유
23 - ping guo - 사과
23 - you young -  수영하다@
24 - fu wu yua(2)n - 종업원@
24 - ming zi - 이름
24 - xue xiao - 학교
3 - ben zi - 공책
3 - gei - 주다
3 - gou - 개
3 - ji - 몇
3 - kao - 시험을 보다
3 - leng - 춥다 차다
3 - nar - 어디(의문사)
3 - shui - 물
3 - xie - 쓰다@
3 - yizi - 의자
3 - yuan - 멀다
31 - Bei jing - 북경
31 - dian xin - 간식
31 - guo zhi - 쥬스@
31 - hao chi - 맛있다
31 - hen duo - 매우 많다
31 - hou che zha(4)n - 기차역
31 - lao shi - 선생님
31 - shou ji - 휴대폰
31 - tian tian - 매일
31 - xi huan(경) - 좋아하다
31 - xiao mao - 고양이
31 - zou bian - 왼쪽
32 - cao mei - 딸기@
32 - da lei - 천둥치다@
32 - jian fei - 다이어트@
32 - ke neng - 가능한
32 - lu xing - 여행하다
32 - qi chuang - 일어나다
32 - yi qian - 이전@
32 - you ming - 유명하다
33 - hen yuan - 매우 멀다
33 - ji zhong - 몇 종류
33 - ke yi - 할수 있다
33 - li jie - 이해하다
33 - shou biao - 손목시계@
33 - shui guo - 과일
33 - xi lian - 세수하다@
33 - xi shou - 손을씻다@
33 - xiao gou - 강아지
33 - yu san - 우산@
34 - bai huo sha(1)ng dia(4)n - 백화점@
34 - bi jiao - 비교적
34 - da dian hua(4) - 전화하다
34 - hao kan - 보기 좋다
34 - jiu dian - 호텔@
34 - ke le - 콜라@
34 - li fa dia(4)n - 미용실@
34 - man yi - 만족하다
34 - wan shang(경) - 저녁
34 - yan jing - 안경@
4 - da - 크다
4 - gan - ~하다@ = zou
4 - geng(끄엉) - 더
4 - gui - 비싸다
4 - hou mian(bian) - 뒤@
4 - hua - 그리다
4 - huan - 바꾸다
4 - kan - 보다
4 - mao zi(경) - 모자
4 - re - 덥다, 뜨겁다
4 - shang - 위
4 - shang mian(bian) - 위@
4 - sui - 살, 나이
4 - wai mian(bian) - 바깥@
4 - wen - 질문
4 - xia - 아래
4 - you bian(경) - 오른쪽
4 - zai - ~에 있다, ~에서
4 - zhang fu(경) - 남편
4 - zou - ~ 하다
41 - ban gong shi(4) - 사무실@
41 - chang ge - 노래하다@
41 - guang jie - 쇼핑하다@
41 - mian bao dian(4) - 빵집@
41 - pa chu sou(3) - 파출소@
41 - shang ban - 출근하다
41 - xia ban - 퇴근하다@
41 - xia tian - 여름@
42 - wen ti - 문제, 질문
42 - zi xing che(1) - 자전거
43 - bao zhi - 신문
43 - di tie - 지하철@
43 - dian ying - 영화
43 - dian ying yuan(4) - 영화관
43 - tiao wu - 춤을 추다@
43 - xia xue - 눈이 온다@
43 - xia yu - 비가온다@
44 - ba ba - 아빠
44 - dan shi - 그러나, 하지만
44 - dian hua - 전화기@
44 - dian shi - 텔레비전
44 - dui bu  qi(3) - 미안하다
44 - dui mian - 맞은편
44 - han zi - 한자
44 - hua huar - 그림그리다@
44 - jiao shi - 교실
44 - jie shao - 소개하다
44 - jie shao - 소개하다@
44 - piao liang - 예쁘다
44 - shang ke - 수업을 듣다@
44 - shui jiao - 자다
44 - xia ke - 수업이 끝나다@
44 - xian zai - 지금
44 - yao dian - 약국
44 - zai jian - 안녕
44 - zhao pian - 사진
44 - zhao xing ji(1) - 사진기@
44 - zheng zai - 진행형 표현
44 - zou cai - 요리하다
'''

# ====== 데이터 파싱 ======
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


# ====== 세션 상태 초기화 ======
if "window_index" not in st.session_state:
    st.session_state.window_index = 0
    st.session_state.word_index = 0
    st.session_state.unknown = []
    st.session_state.show_answer = False

# 현재 윈도우
start = st.session_state.window_index * WINDOW_SIZE
end = start + WINDOW_SIZE
current_window = words[start:end]

# unknown 초기화
if not st.session_state.unknown:
    st.session_state.unknown = current_window.copy()
    random.shuffle(st.session_state.unknown)

current_word = st.session_state.unknown[st.session_state.word_index]

# ====== 상태 표시 ======
learned = start + (len(current_window) - len(st.session_state.unknown))
progress = learned / TOTAL_WORDS

st.progress(progress)
st.markdown(
    f"""
    **윈도우:** {st.session_state.window_index + 1} / {TOTAL_WINDOWS}  
    **현재 윈도우 남은 단어:** {len(st.session_state.unknown)}개  
    **전체 진행률:** {progress * 100:.1f}%
    """
)

st.divider()

# ====== 단어 표시 ======
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

# ====== 버튼 영역 ======
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("정답 보기"):
        st.session_state.show_answer = True

with col2:
    if st.button("알아요"):
        st.session_state.show_answer = False
        st.session_state.unknown.pop(st.session_state.word_index)

        if not st.session_state.unknown:
            st.session_state.window_index += 1
            if st.session_state.window_index * WINDOW_SIZE >= TOTAL_WORDS:
                st.success("🎉 모든 단어 학습 완료!")
                st.stop()

            st.session_state.unknown = words[
                                       st.session_state.window_index * WINDOW_SIZE:
                                       (st.session_state.window_index + 1) * WINDOW_SIZE
                                       ].copy()
            random.shuffle(st.session_state.unknown)

        st.session_state.word_index = 0
        st.rerun()

with col3:
    if st.button("몰라요"):
        st.session_state.show_answer = False
        st.session_state.word_index = (st.session_state.word_index + 1) % len(st.session_state.unknown)
        st.rerun()
