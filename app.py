import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="자기소개 앱",
    page_icon="😊",
    layout="centered"
)

# 제목
st.title("👋 자기소개 앱")
st.subheader("안녕하세요! 저는 Streamlit으로 만든 웹앱입니다.")

# 사이드바
st.sidebar.title("메뉴")
menu = st.sidebar.radio(
    "이동하기",
    ["홈", "프로필", "취미", "연락처"]
)

# 홈 화면
if menu == "홈":
    st.header("🏠 홈")
    st.write("환영합니다! 이 앱은 자기소개를 위한 간단한 Streamlit 웹앱입니다.")

    name = st.text_input("이름을 입력하세요")

    if name:
        st.success(f"{name}님 반갑습니다! 😊")

# 프로필 화면
elif menu == "프로필":
    st.header("🙋 프로필")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
            width=200
        )

    with col2:
        st.write("### 이름: 홍길동")
        st.write("### 나이: 25")
        st.write("### 직업: 개발자")
        st.write("### 소개:")
        st.write("Python과 웹 개발을 좋아합니다!")

# 취미 화면
elif menu == "취미":
    st.header("🎯 취미")

    hobbies = ["💻 코딩", "🎵 음악 듣기", "📚 독서", "🏃 운동"]

    for hobby in hobbies:
        st.write(hobby)

    favorite = st.selectbox(
        "가장 좋아하는 취미는?",
        hobbies
    )

    st.info(f"선택한 취미: {favorite}")

# 연락처 화면
elif menu == "연락처":
    st.header("📞 연락처")

    email = st.text_input("이메일")
    message = st.text_area("메시지")

    if st.button("보내기"):
        if email and message:
            st.success("메시지가 전송되었습니다! 🚀")
        else:
            st.warning("모든 내용을 입력해주세요.")

# 하단
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
