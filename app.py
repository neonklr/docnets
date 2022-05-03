# Main App for Web App

"""

File : app.py
File_Info : This file contains python streamlit code for Main app
Author : Hospitalized Trio

"""

# Dependencies

import streamlit as st
import Scripts.Utilities as Utils
import Scripts.constants as constants
import Scripts.cookie_manager as CMFunctions

from google.cloud import firestore


# ================================ SETTING STREAMLIT PAGE CONFIGURATIONS ================================ #

st.set_page_config(
    page_title="Docnets",
    layout="wide",
    page_icon=None, # DEPRECATED : constants.PAGE_ICON,
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help" : None,
        "Report A Bug" : None,
        "About" : None,
    }
)

if constants.FIREBASE_DATABASE == None:
    constants.FIREBASE_DATABASE = firestore.Client.from_service_account_info(
        Utils.get_credentials()
    )

Utils.set_env_variables()
Utils.remove_streamlit_marks(st)

constants.COOKIE_MANAGER = CMFunctions.get_manager()

if constants.CURR_USER == None:
    CMFunctions.get_user_cookies()


# Additional Overwriting of "My Account" Tag

if not constants.CURR_USER:
    login_name = "Login/Signup"
else:
    login_name = "My Account"

# ================================ Importing Intra-Scripts ================================ #

from Pages.home_page import show_home_page
from Pages.book_an_appointment_page import show_book_an_appointment_page
from Pages.ongoing_schedules_page import show_ongoing_schedules_page
from Pages.city_map_page import show_city_map_page
from Pages.announcements_page import show_announcements_page
from Pages.faqs_page import show_faqs_page
from Pages.contact_us_page import show_contact_us_page
from Pages.my_account_page import show_my_account_page


import hydralit_components as hc


def make_navbar():
    global login_name

    # specify the primary menu definition
    menu_data = [
        {'icon': "far fa-handshake", 'label':"Book An Appointment"}, #'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
        {'icon': "bi bi-calendar3", 'label':"Ongoing Schedules"},
        {'icon': "bi bi-geo-alt", 'label':"City Map"},
        {'icon':"bi bi-megaphone",'label':"Announcements"},
        {'icon': "bi bi-chat-left-text", 'label':"FAQs"},
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
        login_name=login_name,
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=True, #at the top or not
        sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
        key="current_page"
    )

    # TODO :- shift sidebar at top

# ================================ Main Functions ================================ #


def main():
    global login_name

    make_navbar()

    curr_page = st.session_state.get("current_page", None)

    if curr_page == None or curr_page == "Home":
        show_home_page(st)

    elif curr_page == "Contact Us":
        show_contact_us_page(st)

    elif curr_page == "Book An Appointment":
        show_book_an_appointment_page(st)

    elif curr_page == "Ongoing Schedules":
        show_ongoing_schedules_page(st)

    elif curr_page == "City Map":
        show_city_map_page(st)

    elif curr_page == "Announcements":
        show_announcements_page(st)

    elif curr_page == "FAQs":
        show_faqs_page(st)

    elif curr_page == "Login/Signup" or curr_page == "My Account":
        show_my_account_page(st)

main()