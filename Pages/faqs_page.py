import Scripts.Utilities as Utils

question_answers = {

    "How to Book an Appointment  ?": 
    """
    After Logging in, Go To "Book An Appointment" Page and Find an availiable Doctor whom you wanna book an appointment with. 
    Enter a valid future date and time and click "Book My Appointment" Button to Book your appointment.
    """, 

    "Why does it say 'Date and Time is Not Valid' when booking  ?":
    """
    You can't enter a past date and time. 
    """, 
    
    "Why isn't it showing all doctors  ?":  # TODO:  Better wording of question
    """
    There are multiple filters applied on list of doctors shown.  Like..
        --> Selected creteria  (like Specilization) 
        --> Whether the Doctor sees patients on date and time you specified. 
        --> Whether the Doctor is already appointed to some patient.  
    """, 

    "Why do I need to Enter my Address/Location when Registering  ?":
    """
    For your convenience, your address/location is used to show the nearest doctors around you. 
    """, 

    "Why Cookies  ?": 
    """
    To help you provide a better user experience, we save your username in cookies after you log in.
    So that you won't have to enter them everytime you visit this website. 
    """, 

}


def show_faqs(st):
    for question, answer in question_answers.items():
        with st.expander(question, expanded=False):
            st.text("")  
            st.text(answer)
            st.text("")

    st.markdown("""
    <style>
        .streamlit-expanderHeader {
            font-size: 20px;
            font-weight: 600;
            color: #00B0FF;
        }
    </style>
    
    """, unsafe_allow_html=True)


def show_page_heading(st):
    Utils.website_heading(
        st,
        content="FAQ",
        symbol="s",
        font_size=60,
        color="green",
        text_align="center"
    )

    Utils.add_space(st)


def show_faqs_page(st):
    show_page_heading(st)
    show_faqs(st)