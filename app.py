import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(
    page_title="취향 탐험가",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 취향 탐험가")
st.markdown("간단한 질문에 답하고 당신의 취향 유형을 알아보세요!")

st.divider()

with st.form("preference_form"):

    food = st.radio(
        "🍕 어떤 음식을 더 좋아하나요?",
        ["한식", "양식", "둘 다 비슷"]
    )

    travel = st.radio(
        "✈️ 여행을 간다면?",
        ["관광 명소", "자연 휴양", "맛집 탐방"]
    )

    weekend = st.radio(
        "🏠 주말에 가장 하고 싶은 것은?",
        ["집에서 휴식", "외출", "새로운 경험"]
    )

    planning = st.radio(
        "📅 당신은?",
        ["계획형", "즉흥형", "상황에 따라"]
    )

    social = st.radio(
        "👥 사람들과의 관계는?",
        ["소수와 깊게", "많이 사귀기", "둘 다"]
    )

    spending = st.radio(
        "💰 소비 스타일은?",
        ["절약형", "가치 소비형", "경험 우선형"]
    )

    submit = st.form_submit_button("결과 보기")

if submit:

    explorer_score = 0
    comfort_score = 0

    # 여행
    if travel == "맛집 탐방":
        explorer_score += 2
    elif travel == "관광 명소":
        explorer_score += 1
    else:
        comfort_score += 2

    # 주말
    if weekend == "새로운 경험":
        explorer_score += 2
    elif weekend == "외출":
        explorer_score += 1
    else:
        comfort_score += 2

    # 계획성
    if planning == "즉흥형":
        explorer_score += 2
    elif planning == "계획형":
        comfort_score += 2

    # 소비
    if spending == "경험 우선형":
        explorer_score += 2
    elif spending == "절약형":
        comfort_score += 2

    st.divider()

    st.subheader("📊 분석 결과")

    if explorer_score >= comfort_score + 2:
        result_type = "모험가형"
        description = """
새로운 경험을 좋아하고 다양한 활동에 적극적입니다.
여행, 체험, 도전을 즐기는 성향이 강합니다.
"""
        recommendations = [
            "혼자 여행 도전",
            "새로운 취미 시작",
            "체험 클래스 참여",
            "즉흥 드라이브"
        ]

    elif comfort_score >= explorer_score + 2:
        result_type = "안정추구형"
        description = """
편안함과 익숙함을 선호합니다.
신중하게 선택하고 안정적인 환경에서 만족감을 느낍니다.
"""
        recommendations = [
            "독서",
            "카페 투어",
            "산책",
            "집콕 취미"
        ]

    else:
        result_type = "균형형"
        description = """
새로운 경험과 안정감을 균형 있게 추구합니다.
상황에 따라 유연하게 행동하는 편입니다.
"""
        recommendations = [
            "주말 근교 여행",
            "가벼운 운동",
            "문화생활",
            "맛집 탐방"
        ]

    st.success(f"당신의 취향 유형은 **{result_type}** 입니다!")

    st.write(description)

    st.subheader("⭐ 추천 활동")

    for item in recommendations:
        st.write(f"• {item}")

    st.subheader("📈 점수")

    score_df = pd.DataFrame({
        "항목": ["모험 성향", "안정 성향"],
        "점수": [explorer_score, comfort_score]
    })

    st.bar_chart(
        score_df.set_index("항목")
    )

    st.subheader("📥 결과 다운로드")

    result_df = pd.DataFrame({
        "항목": [
            "음식 취향",
            "여행 취향",
            "주말 스타일",
            "계획 성향",
            "관계 스타일",
            "소비 스타일",
            "최종 유형"
        ],
        "결과": [
            food,
            travel,
            weekend,
            planning,
            social,
            spending,
            result_type
        ]
    })

    csv = result_df.to_csv(index=False)

    st.download_button(
        label="CSV 다운로드",
        data=csv,
        file_name="preference_result.csv",
        mime="text/csv"
    )

st.divider()

st.caption("취향 탐험가 v1.0")
