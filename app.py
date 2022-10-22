from math import ceil
import streamlit as st
import json
import time
import math

st.header("Posco Edu 20th")
st.subheader("Conditioner")
st.markdown("---")

def Washing_form():
    pass

def make_counter():
    pass

# db read
db_path = './db.json'

def get_min():
    return math.ceil(time.time()/60)

with open(db_path, 'r') as data:
    db = json.load(data)

# Session state

# The count should be in session state
col1, col2, col3 = st.columns([1, 1, 1], gap="Large")
with col1:
    st.subheader("세탁기 1")
    time1 = st.number_input("세탁 시간", value=38)
    user1 = st.text_input("사용자", placeholder="A2 홍길동")


    if st.button("사용"):
        db['num1'] = {"Number": 1, "Current": get_min(), "User": user1, "Use":time1}
        with open(db_path, 'w') as data:
            json.dump(db, data, indent=2)
        st.experimental_rerun()

with col2:
    with st.form("form2"):
        time1 = st.number_input("세탁 시간", value=38)
        user1 = st.text_input("사용자", placeholder="A2 홍길동")

        st.form_submit_button("Submit")

with col3:
    with st.form("form3"):
        time1 = st.number_input("세탁 시간", value=38)
        user1 = st.text_input("사용자", placeholder="A2 홍길동")

        st.form_submit_button("Submit")


#ph = st.empty()
#N = 30*60
#for secs in range(N,0,-1):
#            mm, ss = secs//60, secs%60
#            ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
#            time.sleep(1)