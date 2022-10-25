import streamlit as st
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

name = list(db.keys())
caption = [db[i]['Caption'] for i in name]

# Get Image
images = [Image.open(f'./photos/{i}.png') for i in name]

## Body
tab1, tab2 = st.tabs(["Gallery", "Upload Photo"])

### Gallery
with tab1:

    col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1], gap='medium') 
    for i in range(len(images)):
        eval(f'col{i+1}').markdown(f'<center><b>{name[i]}</b></center>', unsafe_allow_html=True)
        eval(f'col{i+1}').image(images[i], use_column_width='auto')
        eval(f'col{i+1}').code(caption[i])
    
        # if 랜덤:
        #random.shuffle(image_path)
    

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