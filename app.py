import streamlit as st
from gtts import gTTS
import tempfile
import os
import pyttsx3

def tts_google(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    return tts

def tts_pyttsx3(text, lang='en'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.save_to_file(text, "output.mp3")
    engine.runAndWait()

def text_to_braille(text):
    braille_dict = {
        'a': '⠁',
        'b': '⠃',
        'c': '⠉',
        'd': '⠙',
        'e': '⠑',
        'f': '⠋',
        'g': '⠛',
        'h': '⠓',
        'i': '⠊',
        'j': '⠚',
        'k': '⠅',
        'l': '⠇',
        'm': '⠍',
        'n': '⠝',
        'o': '⠕',
        'p': '⠏',
        'q': '⠟',
        'r': '⠗',
        's': '⠎',
        't': '⠞',
        'u': '⠥',
        'v': '⠧',
        'w': '⠺',
        'x': '⠭',
        'y': '⠽',
        'z': '⠵',
        ' ': ' '
    }

    braille_text = ''
    for char in text.lower():
        braille_char = braille_dict.get(char, char)
        braille_text += braille_char

    return braille_text

def main():
    st.title("시각장애인을 위한 책 읽기 및 쓰기 앱")

    # 텍스트 입력
    book_text = st.text_area("책 텍스트를 입력하세요", height=400)

    # 선택된 TTS 엔진
    tts_engine = st.selectbox("TTS 엔진 선택", ["Google TTS", "pyttsx3"])

    # 음성 변환 버튼
    if st.button("책 읽어주기"):
        if book_text:
            if tts_engine == "Google TTS":
                tts = tts_google(book_text)
                with tempfile.NamedTemporaryFile(delete=False) as temp_wav:
                    tts.save(temp_wav.name)
                    st.audio(temp_wav.name, format="audio/wav")
                os.remove(temp_wav.name)
            elif tts_engine == "pyttsx3":
                tts_pyttsx3(book_text)
                st.audio("output.mp3", format="audio/mp3")

    # 점자 변환 버튼
    if st.button("책을 점자로 변환하기"):
        if book_text:
            braille_text = text_to_braille(book_text)
            st.write("점자로 변환된 텍스트:")
            st.write(braille_text)

    # 음성 안내 버튼
    if st.button("음성 안내로 점자 이해하기"):
        if book_text:
            tts_pyttsx3(text_to_braille(book_text))
            st.audio("output.mp3", format="audio/mp3")

    # 텍스트 파일 다운로드 링크
    # 텍스트 파일 다운로드 링크
    # 텍스트 파일 다운로드 링크
    if st.button("점자 텍스트 파일 다운로드"):
        if book_text:
            braille_text = text_to_braille(book_text)
            file_path = "braille_text.txt"
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(braille_text)
            st.write("점자로 변환된 텍스트를 다운로드하세요.")
            st.download_button("다운로드", braille_text, key="braille_download", file_name="braille_text.txt")

if __name__ == "__main__":
    main()
