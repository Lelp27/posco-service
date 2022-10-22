import streamlit as st
import json
import time
import datetime
from math import floor


def write_db(n):
    if st.session_state[f'user_key{n}'] == '':
        st.error("경고! 사용자 이름을 적어주세요 (새로고침 하면 다시 가능합니다)")
        st.stop()

    db[f'num{n}'] = {"Number": n, "Current": time.time(), \
                "User": st.session_state[f"user_key{n}"], \
                "Use": st.session_state[f"time_key{n}"]}
    with open(db_path, 'w') as data:
        json.dump(db, data, indent=2)

def get_min(time_data):
    return (str(round(floor(time_data)/60, 2)).replace('.', ':'))

def timer_form(n):
    with st.form(f'form{n}'):
        
        st.metric(db[f"num{n}"]['User'], eval(f"check{n}")[2])

        if st.session_state[f'overwrite{n}']:
            Washing_form(n=n, off_button=False)
            if st.form_submit_button("Accept"):
                write_db(n=n)
                st.session_state[f'overwrite{n}'] = False
                st.experimental_rerun()           
        else:
            if st.form_submit_button("OverWrite"):
                st.session_state[f'overwrite{n}'] = True
                st.experimental_rerun()

def Washing_form(n, off_button=True, default_time = 38):
    st.number_input("세탁 시간", max_value=60, value=default_time, key=f"time_key{n}")
    st.text_input("사용자", placeholder="A2 홍길동", key=f"user_key{n}")

    if off_button:
        if st.button("사용", key=f'button{n}'):
            db[f'num{n}'] = {"Number": n, "Current": time.time(), \
                            "User": st.session_state[f"user_key{n}"], \
                            "Use": st.session_state[f"time_key{n}"]}
            with open(db_path, 'w') as data:
                json.dump(db, data, indent=2)
            st.experimental_rerun()
    else:
        pass

def check_used(n):
    with open(db_path, 'r') as data:
        db = json.load(data)[f'num{n}']
    
    user = db['User']
    left_time = (db['Current'] + (db['Use']*60)) - time.time()

    if left_time > -600:
        return ([True, user, get_min(left_time)])
    else:
        return ([False])


# Session State
for i in range(1, 6):
    if f'overwrite{i}' not in st.session_state:
        st.session_state[f'overwrite{i}'] = False

#st.select_slider("Displayed values:", ["Normalized", "Absolute"])

# db read
db_path = './db.json'

with open(db_path, 'r') as data:
    db = json.load(data)


# Web Start
st.set_page_config(page_title="Booking", layout="centered", \
    menu_items={
        'Get help': 'https://github.com/Lelp27/posco-service',
        'About': 'Laundry Service for Posco Edu'})

st.header("Posco Edu 20th")
t_col1, t_col2 = st.columns([3,2])
with t_col1:
    st.warning("* 오류 발생 시 페이지 새로고침 해주세요 \\\n * 실수로 등록 시 OverWrite 클릭 후 -10분으로 등록해주세요")
with t_col2:
    st.success("시간은 -10분 까지 저장 됩니다.")

st.markdown("---")
if st.button("⌛ Time Update", key='update'):
    # with st.spinner("Text = Progressing"):
        # time.sleep(5)
    st.experimental_rerun()


# Session state
# The count should be in session state
col1, col2, col3 = st.columns([1, 1, 1], gap="Large")

with col1:
    st.subheader("세탁기 1")
    check1 = check_used(1)
    if check1[0]:
        timer_form(1)
    else:
        Washing_form(n = 1)
    
with col2:
    st.subheader("세탁기 2")
    check2 = check_used(2)
    if check2[0]:
        timer_form(2)
    else:
        Washing_form(n = 2)

with col3:
    st.subheader("세탁기 3")
    check3 = check_used(3)
    if check3[0]:
        timer_form(3)
    else:
        Washing_form(n = 3)

st.write("")
st.markdown("---")

# Dry
col4, col5 = st.columns([1,1], gap="Large")
with col4:
    st.subheader("건조기 1")
    check4 = check_used(4)
    if check4[0]:
        timer_form(4)
    else:
        Washing_form(n = 4, default_time=20)

with col5:
    st.subheader("건조기 2")
    check5 = check_used(5)
    if check5[0]:
        timer_form(5)
    else:
        Washing_form(n = 5, default_time=20)


#ph = st.empty()
#N = 30*60
#for secs in range(N,0,-1):
#            mm, ss = secs//60, secs%60
#            ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
#            time.sleep(1)
