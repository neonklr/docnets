import json
import Scripts.cookie_manager as CMFunctions
import Scripts.constants as constants

def login(username, password, is_doctor):
    if is_doctor:
        CURR_FILE = constants.DOCTORS_FILE_PATH
    else:
        CURR_FILE = constants.USERS_FILE_PATH



    with open(CURR_FILE, 'r') as file:
        data = json.load(file)
    
    if username not in data:
        raise Exception("Username doesn't exist")
    
    if data[username]['password'] != password:
        raise Exception("Wrong password")

    CMFunctions.set_user_cookies(
        [username, is_doctor]
    )