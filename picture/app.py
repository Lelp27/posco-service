import streamlit as st
import random
from PIL import Image
import json
import os
# FUnctions
# Image REsize Function.. 필요 (일정크기 이하로)

# Web Start
st.set_page_config(page_title="Photo", layout="wide", \
    menu_items={
        'Get help': 'https://github.com/Lelp27/posco-service',
        'About': 'Photo Gallery'})

st.header("20th Photo Gallery")
# Random SLider


# Load Json
db_path = './photodb.json'
with open(db_path, 'r') as data:
    db = json.load(data)

name = list(db.keys())
caption = [db[i]['Caption'] for i in name]
images = [Image.open(db[i]['Photo']) for i in name]

# Get Image
#images = [Image.open(f'./photos/{i}.png') for i in name]

## Body
tab1, tab2 = st.tabs(["Gallery", "Upload Photo"])

### Gallery
with tab1:
    n = 0
    col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1], gap='medium') 
    for i in range(len(images)):
        if i >= 6:
            i = i % 6
        eval(f'col{i+1}').markdown(f'<center><b>{name[i]}</b></center>', unsafe_allow_html=True)
        eval(f'col{i+1}').image(images[i], use_column_width='auto')
        eval(f'col{i+1}').text_area(f"area{n}", caption[i], key=f'area{n}', disabled=True, label_visibility='collapsed')
        n += 1
    

# UPload System
with tab2:
    with st.form("Upload", clear_on_submit=True):
        name = st.text_input("Name", placeholder="A2 홍길동")
        name = name.replace(' ', '_')
        user_caption = st.text_input("Caption", placeholder="25자 이내")
        photo = st.file_uploader("Photo Uploader", type=['png', 'jpg', 'jpeg'], accept_multiple_files=False)
        if st.form_submit_button("Submit"):
            if (name == None) | (photo == None):
                st.error("이름과 사진을 채워주세요")
                st.stop()
            prefix = os.path.splitext(photo.name)[-1]
            # Photo Save
            with open(f'./photos/{name}.{prefix}', 'wb') as f:
                f.write(photo.getbuffer())
            # DB save
            name = name.replace(' ', '_')
            db[f'{name}'] = {'Caption': f'{user_caption}', 'Photo':f"./photos/{name}.{prefix}"}
            with open(db_path, 'w', encoding='UTF-8') as data:
                json.dump(db, data, indent=2, ensure_ascii=False)
            st.success("등록되었습니다 !")

def app():
    pass

if __name__ == "__main__":
    app()