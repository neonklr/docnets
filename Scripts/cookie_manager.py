import streamlit as st
import extra_streamlit_components as stx
from datetime import datetime, timedelta
import Scripts.constants as constants

@st.experimental_singleton(suppress_st_warning=True)
def get_manager():
    return stx.CookieManager(key="oof_cookie_manager")


def get_user_cookies():
    COOKIE = constants.COOKIES[constants.COOKIE_ID]

    if COOKIE != None:
        return [x.strip() for x in COOKIE.split(";")]


def set_user_cookies(VALUE):
    # Set final date of expiry
    EXPIRES_AT = datetime.now() + timedelta(days=constants.EXPIRES_IN_DAYS)
    
    # set the cookie
    constants.COOKIE_MANAGER.set(
        cookie = constants.COOKIE_ID,
        val = ''.join([VALUE[0], ";", VALUE[1]]),
        expires_at = EXPIRES_AT
    )

    constants.CURR_USER = VALUE
    constants.CURR_USER_IS_DOC = bool(VALUE[1])