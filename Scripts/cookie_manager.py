# import streamlit as st
# import extra_streamlit_components as stx
# from datetime import datetime, timedelta
import Scripts.constants as constants

# @st.experimental_singleton(suppress_st_warning=True)
# def get_manager():
#     return stx.CookieManager()


def get_user_cookies():
    COOKIES = constants.COOKIES.get(constants.COOKIE_ID, None)
    # print("COOKIES", COOKIES)

    if COOKIES != None:
        COOKIES = [x.strip() for x in COOKIES.split(";")]
        constants.CURR_USER = COOKIES[0]
        constants.CURR_USER_IS_DOC = eval(COOKIES[1])


def set_user_cookies(VALUE):
    # Set final date of expiry
    
    # set the cookie
    VALUE = ''.join([VALUE[0], ";", str(VALUE[1])])
    constants.COOKIES[constants.COOKIE_ID] = VALUE

    constants.COOKIES.save()








# def get_user_cookies():
#     COOKIES = constants.COOKIE_MANAGER.get_all()
#     COOKIE = COOKIES.get(constants.COOKIE_ID)

#     if COOKIE != None:
#         COOKIE = [x.strip() for x in COOKIE.split(";")]
#         constants.CURR_USER = COOKIE[0]
#         constants.CURR_USER_IS_DOC = eval(COOKIE[1])


# def set_user_cookies(VALUE):
#     # Set final date of expiry
#     EXPIRES_AT = datetime.now() + timedelta(days=constants.EXPIRES_IN_DAYS)
    
#     # set the cookie
#     constants.COOKIE_MANAGER.set(
#         cookie = constants.COOKIE_ID,
#         val = ''.join([VALUE[0], ";", str(VALUE[1])]),
#         expires_at = EXPIRES_AT
#     )

#     constants.CURR_USER = VALUE[0]
#     constants.CURR_USER_IS_DOC = VALUE[1]