print("hello world!!!!!!!!!!")

import streamlit

import streamlit as st

# st.write("Hello World")

# st.title('This is a title')
# st.header('This is a header')
# st.subheader('This is a subheader')

# st.text('Hello World. Streamlit text')
# name = 'Hong gildong'
# st.text('Hi, {}'.format(name))

# st.markdown('## This is markdown')


# hello = st.button("Hello")
# bye=st.button("Bye")

# if bye:
#     st.write("안녕히가세요")
# else:
#     st.write("안녕하세요.")

st.sidebar.selectbox("MENU",["로그인","회원가입"])

db_id="test"
db_pw="123"


st.title("로그인")


id=st.text_input("아이디",placeholder="아이디를 입력하세요")
pw=st.text_input("비밀번호",type="password")
login=st.button("로그인")


if login:
    if db_id==id and db_pw==pw:
        st.success("로그인 성공")
        st.balloons()
    else:
        st.error("로그인 실패")
