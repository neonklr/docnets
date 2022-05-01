import json 

from Scripts.constants import * 


def add_booking(date_and_time, doc_id, patient_id):
    with open(APPOINTMENT_FILE_PATH, 'r') as file:
        data = json.load(file)  
    
    schedule = data[doc_id]['schedule'] 
    date = str(date_and_time.date()) 
    time = str(date_and_time.time()) 

    if date not in schedule:
        schedule[date] = {} 
    
    schedule[date][time] = patient_id 

    with open(APPOINTMENT_FILE_PATH, 'w') as file:
        json.dump(data, file) 


def add_new_person(username, password, person_data):
    # TODO: Break the Func
    if "specialization" in person_data:
        CURR_FILE = DOCTORS_FILE_PATH
    else:
        CURR_FILE = USERS_FILE_PATH
    
    with open(CURR_FILE, 'r') as file:
        print(CURR_FILE)
        data = json.load(file)
    
    if username in data:
        raise Exception("Username already exists")
    
    data[username] = person_data
    data[username]['password'] = password  # TODO:  Encrypt it.  :'v 
    
    if "specialization" in person_data:
        set_doc_appointment_detail(username, "00:30", ["00:00-23:59"])  # TODO:  Remove HardCoding
    
    with open(CURR_FILE, 'w') as file:
        json.dump(data, file)
    
    


def set_doc_appointment_detail(username, time_per_person, time_slots):
    new_data = {
        "time_per_patient": str(time_per_person), 
        "time_slots": time_slots,  # TODO: preprocess it 
        "schedule": {}
    }

    # TODO: How to simply append  ??   !!  HELPP  !! 

    with open(APPOINTMENT_FILE_PATH, 'r') as file:
        data = json.load(file)

    data[username] = new_data

    with open(APPOINTMENT_FILE_PATH, 'w') as file:
        json.dump(data, file)
    
