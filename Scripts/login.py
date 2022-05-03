# import json
import Scripts.cookie_manager as CMFunctions
import Scripts.constants as constants
import hashlib
from Scripts.data_loader import get_doctors_data, get_users_data
import Scripts.Utilities as Utils  # TODO: remove it 


def login(username, password, is_doctor):
    if is_doctor:
        data = get_doctors_data(doctor=username)
    else:
        data = get_users_data(user=username)

    # with open(CURR_FILE, 'r') as file:
    #     data = json.load(file)

    # data = Utils.get_firebase_data(CURR_FILE, username)
    
    if not data:
        raise Exception("Username doesn't exist")
    
    if data['password'] != hashlib.sha256(password.encode()).hexdigest():
        raise Exception("Wrong password")

    CMFunctions.set_user_cookies(
        [username, is_doctor]
    )