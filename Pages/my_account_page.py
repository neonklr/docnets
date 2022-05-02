from Scripts.data_saver import add_new_person
from Scripts.login import login
import Scripts.constants as constants
from Scripts.cookie_manager import set_user_cookies
import Scripts.Utilities as Utils


def get_location_input(container):
    # from shapely.geometry import Point, Polygon
    # import geopandas as gpd
    # import pandas as pd
    import geopy
    from geopy.geocoders import Nominatim
    from geopy.extra.rate_limiter import RateLimiter

    # street = container.text_input("Street")
    city = container.text_input("City", "Sonipat")
    province = container.text_input("Province", "Haryana")
    country = container.text_input("Country", "India")

    geolocator = Nominatim(user_agent="GTA Lookup")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    # location = geolocator.geocode(street+", "+city+", "+province+", "+country)
    location = geolocator.geocode(city + ", " + province + ", " + country)

    if location != None:
        return [location.latitude, location.longitude]




def show_login_form(login_form):
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
        except Exception as e:
            info_box.warning(str(e))


def show_register_form(register_form): 
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
            "fees": register_form.number_input("Please enter your fees", value=100, step=100),
            "phone": register_form.number_input("Please enter your phone number", step=1, max_value=10**11-1),
            "location": get_location_input(register_form),
            "slot_start": register_form.time_input("Please enter starting time of work"),
            "slot_end": register_form.time_input("Please enter ending time of work"),
            "time_per_patient": register_form.number_input("Please enter time per patient you would like to give (in minutes)", value=30, step=1, max_value=24*60-1),
            "specialization": register_form.text_input("Please enter your specialization"),
            "experience": register_form.number_input("Please enter your experience", value=0.0, step=0.1),
        }
        
    elif i_am_a == "I am a user":
        data = {
            "name": register_form.text_input("Please enter your name"),
            "location": get_location_input(register_form)
        }
        
    info_box = register_form.empty()

    if register_form.button("Register"):
        if i_am_a == "I am a doctor":
            if not (username and password and all(data.values())):
                info_box.warning("Please fill all the fields")
            else:
                try:
                    add_new_person(username, password, data)
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
                    add_new_person(username, password, data)
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
        st.warning(f"You are logged In as {constants.CURR_USER}")
        if Utils.center_button(st, "Logout"):
            logout()

        return None


    container = st.columns([1, 2, 1])[1]
    value = container.selectbox("", ["Login", "Register"])

    if value == "Login":
        show_login_form(container)
        
    elif value == "Register":
        show_register_form(container)