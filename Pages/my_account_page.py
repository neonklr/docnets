from Scripts.data_saver import add_new_user, add_new_doctor
from Scripts.login import login
import Scripts.constants as constants
from Scripts.cookie_manager import set_user_cookies
import Scripts.Utilities as Utils

import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def get_location_input(container):
    try:
        # from shapely.geometry import Point, Polygon
        # import geopandas as gpd
        # import pandas as pd

        # street = container.text_input("Street")
        city = container.text_input("City")
        province = container.text_input("Province")
        country = container.text_input("Country")

        geolocator = Nominatim(user_agent="GTA Lookup")
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        # location = geolocator.geocode(street+", "+city+", "+province+", "+country)
        location = geolocator.geocode(city + ", " + province + ", " + country)

        if location != None:
            return [location.latitude, location.longitude]

    except Exception:
        pass




def show_login_form(st, login_form):
    login_form.markdown("""
    <h1 style="text-align: center;">Please login...</h1>
    """, unsafe_allow_html=True)

    username = login_form.text_input("Please enter your username")
    password = login_form.text_input("Please enter your password", type="password")
    i_am_a = login_form.radio("Please define yourself", ["I am a user", "I am a doctor"])

    info_box = login_form.empty()

    if login_form.button("Login"):
        try:
            login(username, password, i_am_a == "I am a doctor")
            info_box.success("Successfully logged in")
            st.experimental_rerun()
        except Exception as e:
            info_box.warning(str(e))


def show_register_form(st, register_form): 
    register_form.markdown("""
    <h1 style="text-align: center;">Please Register...</h1>
    """, unsafe_allow_html=True)
    
    username = register_form.text_input("Please enter your username")
    password = register_form.text_input("Please enter your password", type="password")
    i_am_a = register_form.radio("Please define yourself", ["I am a user", "I am a doctor"])

    if i_am_a == "I am a doctor":

        data = {
            "name": register_form.text_input("Please enter your name"),
            "email": register_form.text_input("Please enter your email"),
            "fees": register_form.number_input("Please enter your fees", value=100, step=100, key="doc_fees", min_value=0),
            "phone": register_form.text_input("Please enter your phone number", max_chars=10),
            "location": get_location_input(register_form),
            "slot_start": register_form.time_input(
                "Please enter starting time of work",
                value = st.session_state.get("slot_starting", None),
                key="slot_starting"
            ),
            "slot_end": register_form.time_input(
                "Please enter ending time of work",
                value = st.session_state.get("slot_ending", None),
                key="slot_ending"
            ),
            "time_per_patient": register_form.number_input("Please enter time per patient you would like to give (in minutes)", value=30, step=5, max_value=24*60-1),
            "specialization": register_form.selectbox("Please enter your specialization", constants.ALL_SPECIALIZATIONS),
            "experience": register_form.text_input("Please enter your experience (in years)", max_chars=5)
        }
        
    elif i_am_a == "I am a user":
        data = {
            "name": register_form.text_input("Please enter your name"),
            "location": get_location_input(register_form),
            "phone": register_form.text_input("Please enter your phone number", max_chars=10)
        }
        
    info_box = register_form.empty()

    try:
        data["phone"] = int(data["phone"])
    except Exception as e:
        info_box.warning("You have entered an invalid phone number")
        return None

    if data["phone"] < 10**9:
        info_box.warning("You have entered an invalid phone number")
        return None

    try:
        if "experience" in data:
            data["experience"] = float(data["experience"])
    except Exception as e:
        info_box.warning("Experience can only be an integer or decimal value")
        return None


    if register_form.button("Register"):
        if i_am_a == "I am a doctor":
            if not (username and password and all(data.values())):
                info_box.warning("Please fill all the fields")
            else:
                try:
                    add_new_doctor(username, password, data)
                    info_box.success("Successfully registered")

                    constants.CURR_USER = username
                    constants.CURR_USER_IS_DOC = True

                    set_user_cookies(
                        [username, True]
                    )

                except Exception as e:
                    info_box.warning(str(e))

        else:
            if not (username and password and all(data.values())):
                info_box.warning("Please fill all the fields")
            else:
                try:
                    add_new_user(username, password, data)
                    info_box.success("Successfully registered")

                    constants.CURR_USER = username
                    constants.CURR_USER_IS_DOC = False

                    set_user_cookies(
                        [username, False]
                    )

                except Exception as e:
                    info_box.warning(str(e))


def logout():
    set_user_cookies(['', None])
    constants.CURR_USER = None
    constants.CURR_USER_IS_DOC = None


def show_my_account_page(st):
    
    if constants.CURR_USER:
        st.warning(f"You are logged In as {constants.CURR_USER} @{'DOCTOR' if constants.CURR_USER_IS_DOC else 'USER'}")
        if Utils.center_button(st, "Logout"):
            logout()
            st.experimental_rerun()

        return None


    container = st.columns([1, 2, 1])[1]
    value = container.selectbox("", ["Login", "Register"])

    if value == "Login":
        show_login_form(st, container)
        
    elif value == "Register":
        show_register_form(st, container)