import streamlit as st
#from multiapp import MultiApp
import utils


def app():
    st.set_page_config(
        page_title="유아용품 고객 분석과 프로모션 전략을 통한 고객 확보 및 매출 증진",
        page_icon="👋",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Get help": "https://github.com/Lelp27/posco-service/bigdata",
            "Report a Bug": None,
            "About": "Posco 청년 AI·Big Data 20기 A2조",
        },
    )

    st.title("Posco Edu 20th A2")
    from PIL import Image
    image = Image.open('/home/piai/workspace/posco-service/bigdata/data/posco-logo.png')
    st.image(image)
    """
    > 안녕하세요 With Posco A2조   
    > 장동언, 박성군, 전하영, 김민지, 전예찬, 이경로 입니다.
    
    ---
    
    Page 1 `View PDF`를 통해서 발표 슬라이드를 보실 수 있습니다.  
    """
    st.sidebar.title("Posco Edu 20th A2")
    st.sidebar.write(
    """
    ### Source Code
    [Github](Lelp27/github.com) : Lelp27/github.com/posco-service  
    ![asdf]('/home/piai/workspace/posco-service/bigdata/data/posco-logo.png')

    """
    )
    # st.sidebar.subheader("Seong-Kun Bak *Lelp27/github.com*")
    # st.sidebar.markdown("---")
    # st.sidebar.text("")

    st.download_button('Presentation PDF', '/home/piai/workspace/posco-service/bigdata/data/presentation.pdf')
    
    with st.expander('View PDF'):
        pdf_display = utils.show_pdf("/home/piai/workspace/posco-service/bigdata/data/presentation.pdf")
        st.markdown(pdf_display, unsafe_allow_html=True)
# app = MultiApp()

# # Add all your application here
# app.add_app("Introduce", page_1.app)
# app.add_app("Improvement Plan", page_2.app)
# app.add_app("Model Demo", model_demo.app)

# The main app
if __name__ == "__main__":
    app()