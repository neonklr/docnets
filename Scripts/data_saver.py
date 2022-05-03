# import json 
import hashlib
from Scripts.constants import * 
import Scripts.Utilities as Utils


def add_booking(date_and_time, doc_id, patient_id):
    data = Utils.get_firebase_data(APPOINTMENT_FILE, doc_id)

    if not data:
        return None
    
    # with open(APPOINTMENT_FILE, 'r') as file:
    #     data = json.load(file)
    
    schedule = data['schedule'] 
    date = str(date_and_time.date()) 
    time = str(date_and_time.time()) 

    if date not in schedule:
        schedule[date] = {} 
    
    schedule[date][time] = patient_id

    # with open(APPOINTMENT_FILE, 'w') as file:
    #     json.dump(data, file)

    Utils.set_firebase_data(APPOINTMENT_FILE, doc_id, data)




def add_new_doctor(username, password, doc_data):
    
    # with open(CURR_FILE, 'r') as file:
    #     data = json.load(file)

    data = Utils.get_firebase_data(DOCTORS_FILE, username)
    
    if data:  # already exists
        raise Exception("Username already exists")

    # data = {}
    
    # data[username] = doc_data
    doc_data['password'] = hashlib.sha256(password.encode()).hexdigest()
    

    if doc_data["slot_start"] >=  doc_data["slot_end"]:
        raise Exception("Start time cannot be greater than less time")
    
    set_doc_appointment_detail(
        username,
        minutes_to_time(doc_data["time_per_patient"]),
        slot_preprocessing(doc_data["slot_start"], doc_data["slot_end"])
    )

    del doc_data["time_per_patient"], doc_data["slot_start"], doc_data["slot_end"]

    Utils.set_firebase_data(DOCTORS_FILE, username, doc_data)



def add_new_user(username, password, user_data):
        # with open(CURR_FILE, 'r') as file:
    #     data = json.load(file)

    data = Utils.get_firebase_data(USERS_FILE, username)
    
    if data:  # already exists
        raise Exception("Username already exists")

    # data is None right now. 
    # data = {}
    
    # data[username] = doc_data
    user_data['password'] = hashlib.sha256(password.encode()).hexdigest()


    Utils.set_firebase_data(USERS_FILE, username, user_data)



# def add_new_person(username, password, person_data):
#     # TODO: Break the Func  :'v 
#     if "specialization" in person_data:
#         CURR_FILE = DOCTORS_FILE
#     else:
#         CURR_FILE = USERS_FILE

    
#     with open(CURR_FILE, 'r') as file:
#         data = json.load(file)
    
#     if username in data:
#         print(data)
#         raise Exception("Username already exists")
    
#     data[username] = person_data
#     data[username]['password'] = hashlib.sha256(password.encode()).hexdigest()

    
#     if "specialization" in person_data:  # is_doctor 
#         # set_doc_appointment_detail(username, "00:30", ["00:00-23:59"])  # TODO:  Remove HardCoding

#         if data[username]["slot_start"] >=  data[username]["slot_end"]:
#             raise Exception("Start time cannot be greater than less time")
        
#         set_doc_appointment_detail(
#             username,
#             minutes_to_time(data[username]["time_per_patient"]),
#             slot_preprocessing(data[username]["slot_start"], data[username]["slot_end"])
#         )

#         del data[username]["time_per_patient"], data[username]["slot_start"], data[username]["slot_end"]

    
#     with open(CURR_FILE, 'w') as file:
#         json.dump(data, file)
    

def slot_preprocessing(start, end):
    return [f"{str(start)}-{str(end)}"]


def minutes_to_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60

    return f"{hours}:{minutes}"


def set_doc_appointment_detail(username, time_per_person, time_slots):
    new_data = {
        "time_per_patient": str(time_per_person), 
        "time_slots": time_slots,  # TODO: preprocess it 
        "schedule": {}
    }

    Utils.set_firebase_data(APPOINTMENT_FILE, username, new_data)

    # with open(APPOINTMENT_FILE_PATH, 'r') as file:
    #     data = json.load(file)

    # data[username] = new_data

    # with open(APPOINTMENT_FILE_PATH, 'w') as file:
    #     json.dump(data, file)
    
