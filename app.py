# Main App for Web App

"""

File : app.py
File_Info : This file contains python streamlit code for Main app
Author : Hospitalized Trio

"""

# Dependencies

import streamlit as st
import Scripts.Utilities as Utils

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


Utils.remove_streamlit_marks(st)


# ================================ Importing Intra-Scripts ================================ #

from Pages.home_page import show_home_page
from Pages.contact_us_page import show_contact_us_page

from Pages.book_an_appointment_page import show_book_an_appointment_page
from Pages.my_account_page import show_my_account_page



def make_navbar(st):
    import hydralit_components as hc
    import datetime

    # specify the primary menu definition
    menu_data = [
        {'icon': "far fa-handshake", 'label':"Book An Appointment"}, #'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
        {'icon': "bi bi-calendar3", 'label':"Ongoing Schedules"},
        {'icon': "bi bi-geo-alt", 'label':"City Map"},
        {'icon':"bi bi-megaphone",'label':"Announcements"},
        {'icon': "bi bi-chat-left-text", 'label':"Forum"},
        {'icon': "bi bi-telephone", 'label':"Contact Us"},
        # {'icon': "fa-solid fa-radar",'label':"Dropdown1", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"},{'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}]},
    ]

    over_theme = {'txc_inactive': '#FFFFFF', 'menu_background':'#00B9FF', 'txc_active':'grey'}
    # over_theme = {'txc_inactive': 'white','menu_background':'inherit','txc_active':'yellow','option_active':'orange'}
    # font_fmt = {'font-class':'h2','font-size':'150%'}
    
    hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        home_name='Home',
        login_name='My Account',
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=True, #at the top or not
        sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
        key="current_page"
    )


# ================================ Main Functions ================================ #


def main():
    make_navbar(st)

    curr_page = st.session_state.get("current_page", None)

    if curr_page == None or curr_page == "Home":
        show_home_page(st)

    elif curr_page == "Contact Us":
        show_contact_us_page(st)

    elif curr_page == "Book An Appointment":
        show_book_an_appointment_page(st)

    elif curr_page == "My Account":
        show_my_account_page(st)

main()