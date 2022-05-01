import json 

files_loc = 'Data/'
APPOINTMENT_FILE_PATH = files_loc + 'appointments.json' 
## DOCTORS_FILE_PATH = files_loc + 'doctors.json' 


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
    