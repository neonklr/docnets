# Main App for Web App

"""

File : app.py
File_Info : This file contains python streamlit code for Main app
Author : Hospitalized Trio

"""

# Dependencies

import streamlit as st

# ================================ SETTING STREAMLIT PAGE CONFIGURATIONS ================================ #

st.set_page_config(
    page_title="appoitment manager",
    layout="wide",
    page_icon=None, # DEPRECATED : constants.PAGE_ICON,
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help" : None,
        "Report A Bug" : None,
        "About" : None,
    }
)


# ================================ Main Functions ================================ #
def remove_streamlit_marks(st):
    st.markdown(
        '''
            <style>
                footer { visibility: hidden; }
                /* #MainMenu { visibility: hidden; } */
                /* [data-testid=stHeader] { backdrop-filter: blur(1px); background: none; } */
            </style>
        '''
    , unsafe_allow_html=True)



def doctor_details(st):
    import datetime
    import json

    st.header("Enter time slot you are free in")
    st.subheader("from :")
    t = st.time_input('Set an alarm for', datetime.time(8, 45))
    st.write('Alarm is set for')

    print(json.load(open('data.json', 'r', encoding='utf-8')))


def main():
    from temp import mycomponent

    # mycomponent()
    # remove_streamlit_marks(st)

    columns = st.columns(2)

    columns[0].image('https://images.unsplash.com/photo-1453728013993-6d66e9c9123a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8dmlld3xlbnwwfHwwfHw%3D&w=1000&q=80')
    columns[1].markdown("""
    <h4>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)</h4>
    """, unsafe_allow_html=True)

    st.selectbox("Select your choice", ["I am a doctor", "I am a patient"])

    doctor_details(st)

main()