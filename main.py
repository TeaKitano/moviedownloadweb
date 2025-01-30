import os

import streamlit as st
from yt_dlp import YoutubeDL

def checkfile(file_name):
    try:
        f=open(file_name)
    except OSError:
        return False
    else:
        f.close()
        return True


def dl_mov(url):
    result=1
    file_num = 0
    while True:
        if checkfile(str(file_num) + ".mp4"):
            file_num += 1
        else:
            break
    ydl_opts = {'format': 'best', 'outtmpl': str(file_num) + ".mp4", "ignoreerrors": True}
    with YoutubeDL(ydl_opts) as ydl:
        result=ydl.download([url])
    if result != 0:
        return -1
    else:
        st.session_state["filename"] = str(file_num) + ".mp4"
        return 0


def dl_sound(url):
    result=1
    file_num = 0
    while True:
        if checkfile(str(file_num) + ".mp3"):
            file_num += 1
        else:
            break
    ydl_opts = {'format': 'best' ,'outtmpl': str(file_num) + ".mp3","ignoreerrors": True}
    with YoutubeDL(ydl_opts) as ydl:
        result=ydl.download([url])
    if result != 0:
        return -1
    else:
        st.session_state["filename"] = str(file_num) + ".mp3"
        return 0

def main():
    data_type = st.selectbox("ダウンロードしたい形式を選択してください", ["mp4", "mp3"])
    url = st.text_input("URLを入力してください", "URL")
    if st.button("URL確定"):
        if data_type == "mp3":
            result = dl_sound(url)
        else:
            result = dl_mov(url)
        try:
            res = st.download_button("ダウンロード", open(st.session_state["filename"], "br"),
                                     "image." + st.session_state["filename"].split(".")[-1])
            if result != 0:
                raise ValueError
        except Exception as e:
            st.text("失敗しました。")
            st.text(e)
    try:
        print(res)
        os.remove(st.session_state["filename"])
    except:
        pass

if __name__ == "__main__":
    main()
