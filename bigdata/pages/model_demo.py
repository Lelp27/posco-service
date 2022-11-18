import streamlit as st
import joblib
import pandas as pd

def load_model(model):
    if model == 'churn':
        return (joblib.load('/home/piai/workspace/posco-service/bigdata/data/churn_model_final.pkl'))
    
    if model == 'kmeans':
        return (joblib.load('/home/piai/workspace/posco-service/bigdata/data/kmeans_model.pkl'))

params1 = ['여', '충남', '네이버블로그', 28, '미혼', 'No',
           '수유용품', 40, 5, 'baby1']
params2 = ['남', '서울', '인스타그램', 28, '기혼', 'No',
           '수유용품', 90, 52, 'baby1']

def churn_sample(sample):
    if sample == 'None':
        return (False)
    if sample == 'Sample 1':
        return(params1)
    if sample == 'Sample 2':
        return(params2)

def churn_test_x(params):
    if params[4]:
        params[4] = '기혼'
    else:
        params[4] = '미혼'
    if params[5]:
        params[5] = 'Yes'
    else:
        params[5] = 'No'
    params[-2] = params[-2]*1000
    params[-1] = 'baby1'
    return (params)
    
def params_to_df(params):
    return (pd.DataFrame(params, 
                         index=['성별', '거주지역', '유입경로', '연령', '결혼유무', '자녀여부',
                                        '첫구매물품', '첫주문까지일', '첫결제금액', '첫구매월령']).T)
    
def app():
    #st.subheader('Model demonstration')
    tab1, tab2 = st.tabs(['Churn', 'KMeans'])

    with tab1:

        with st.expander('Model description'):
            
            """
            ### Churn Classification
            이탈여부 분류 모델은 **첫 물품을 구매한 고객**의 이탈율 예측을 위해 만들었습니다.  
            예측한 이탈율은 복귀 가능성이 높은 잠재 고객을 선별하는데 사용됐습니다.
            
            2019년 가입한 81,310명의 데이터를 아래와 같이 분류하여 사용했습니다.
            ```
            - 설명변수(x) = [성별, 연령, 거주지역, 유입경로, 첫 구매 물품군] 
            - 목표변수(y) = 이탈률(0, 1)
            ```
            
            |이탈여부|Value|  
            |---|---|  
            |이탈|0|  
            |재구매, 복귀|1|
            
            모델 선택을 위해 `DecisionTree`, `RandomForest`, `Neural Network`, `SVM`등  
            다수의 모델 확인 결과 가장 높은 Score의 `GradientBoosting`을 활용했습니다.  
            
            Hyper parameter 탐색은 `RandomSearchCV`를 활용했습니다.
            
            ---
            
            """
            {
                'Model Type' : 'Gradient Boosting',
                'n_estimators' : '500',
                'max_depth' : '19',
                'min_sample_leaf' : '145',
                'min_sample_split' : '105',
                'Learning Rate' : '0.1',
                'Scoreing' : 'f1',
                'Test score' : '0.65'
            }
        

        st.subheader('이탈율 예측모델')
        st.success('신규 고객정보를 이용하여 \n 3개월 후 이탈율을 예측 합니다.')

        with st.form('model1'):
            st.markdown('**개인정보**')
            col1, col2, col3, col4 = st.columns([1,1,1,1])
            성별 = col1.selectbox('성별', ['여', '남'])
            거주지역 = col2.selectbox('거주지역', ['서울', '경기', '충남'])
            유입경로 = col3.selectbox('유입경로', ['인스타그램', '네이버블로그'])
            연령 = col4.number_input('연령', min_value=20, max_value=40)
            결혼유무 = col1.checkbox('기혼')
            자녀여부 = col2.checkbox('자녀여부')
            st.markdown('**구매정보**')
            col2_1, col2_2, col2_3, col2_4 = st.columns([1,1,1,1])
            첫구매물품 = col2_1.selectbox('첫 구매 물품', ['수유용품', '이벤트', '3단계'])
            첫주문까지일 = col2_2.number_input('첫 구매 (일)', min_value=0, max_value=40)
            첫결제금액 = col2_3.number_input('결제금액(천원)', min_value=0, max_value=40)
            첫구매월령 = col2_4.text_input('자녀월령', disabled=True, help='Web 에서 구현이안돼있습니다.')
            churn1 = st.selectbox('Use Sample parameter', ['None', 'Sample 1','Sample 2'],
                                help = '등록된 파라미터 사용 [Sample 1, Sample 2] 사용 시 위 모든 파라미터가 덮어쓰기 됩니다.')
            

            if st.form_submit_button('Save Parameter'):
                if churn1 != 'None':
                    st.session_state.loaded_params = churn_sample(churn1)
                    st.session_state.loaded_model = load_model('churn')
                else:
                    st.session_state.loaded_model = load_model('churn')
                    st.session_state.loaded_params = [성별, 거주지역, 유입경로, 연령, 결혼유무, 자녀여부,
                                    첫구매물품, 첫주문까지일, 첫결제금액, 첫구매월령]

        # Load Model
        if 'loaded_model' not in st.session_state:
            st.warning("The model is not loaded fill parameter and Click 'Save'")
        else:
            st.success("Model is Ready")
        
        # Show Predict Value        
        if st.button('Learn Model'):
            if 'loaded_params' not in st.session_state:
                st.warning("Warning ! \nPlease Fill Parameter Well")
            score = pd.DataFrame(st.session_state.loaded_model.predict_proba(params_to_df(churn_test_x(st.session_state.loaded_params))))
            score = score.rename(columns = {0:'이탈확률', 1:'재구매확률'})
            st.table(score)
            if score['이탈확률'].values < 0.5:
                st.success('환영합니다 고객님!')
            else:
                st.warning('떠나지 마세요..')

    # Tab 2
    with tab2:
        with st.expander('Model description'):
            """
            ### KMeans clustering
            KMeans 군집 분석은 고객 정보 중 **구매와 관계 없는 정보**만 활용해 군집화 한 후  
            각 군집별 맞춤 제품군을 추천하기 위해 활용했습니다.
            
            Shiluote 계수가 가장 높은 군집 수를 선택해 6개 군집으로 분류했습니다.
            """
            {
                'Model Type' : 'KMeans',
                'Fittest number of cluster' : '6',
                'Silhouette score' : '0.262'
            }

if __name__ == '__main__':
    app()
