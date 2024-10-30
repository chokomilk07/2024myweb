print("hello world!!!!!!!!!!")

import streamlit

import streamlit as st

st.write("Hello World")

st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')

st.text('Hello World. Streamlit text')
name = 'Hong gildong'
st.text('Hi, {}'.format(name))

st.markdown('## This is markdown')


hello = st.button("Hello")
bye=st.button("Bye")

if bye:
    st.write("안녕히가세요")
else:
    st.write("안녕하세요.")