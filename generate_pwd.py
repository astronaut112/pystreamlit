import streamlit as st
import random
import string

def generate_password():
    # 8자리 암호 생성
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return password

# Streamlit 앱 설정
st.title("암호 생성 앱")

# "암호 생성" 버튼 생성
if st.button("암호 생성"):
    # 암호 생성 함수 호출
    password = generate_password()
    # 생성된 암호 출력
    st.success(f"생성된 암호: {password}")