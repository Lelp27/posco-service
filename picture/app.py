import streamlit as st
from glob import glob
import random
from PIL import Image
import json
# FUnctions
# Image REsize Function.. 필요 (일정크기 이하로)

# Web Start
st.set_page_config(page_title="Photo", layout="wide", \
    menu_items={
        'Get help': 'https://github.com/Lelp27/posco-service',
        'About': 'Photo Contest'})

st.header("20th Photo Contest")
# Random SLider


# Load Json
db_path = './photodb.json'
with open(db_path, 'r') as data:
    db = json.load(data)

captions = ['A', 'B', 'C', 'D', 'E', 'F', '']

# Get Image
image_path = glob("*.png")
images = [Image.open(i) for i in image_path]



tab1, tab2 = st.tabs(["Gallery", "Upload Photo"])

## Gallery Page, Column을 나눠서 COlumn 사이 Margin 결정하기
with tab1:
    # if 랜덤:
    random.shuffle(image_path)

    st.image(images, width=300, caption=captions)
    # 랜덤 먼저 작성
    # A1, 2, 3, 4 > A
    

# UPload System
with tab2:
    with st.form("Upload", clear_on_submit=True):
        name = st.text_input("Name", placeholder="A2 홍길동")
        photo = st.file_uploader("Photo Uploader", type=['png', 'jpg', 'jpeg'])
        if st.form_submit_button("Submit"):
            if (name == None) | (photo == None):
                st.error("이름과 사진을 채워주세요")
                st.stop()
            # Photo Save
            with open(f'./photos/{name}.png', 'wb') as f:
                f.write(photo.getbuffer())
            # DB save
            name = name.replace(' ', '_')
            db[f'{name}'] = {'Caption': 'a', 'Photo':f"./photos/{name}.png"}
            with open(db_path, 'w') as data:
                json.dump(db, data, indent=2)
            st.success("등록되었습니다 !")






def app():
    pass

if __name__ == "__main__":
    app()