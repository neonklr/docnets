import Scripts.data_loader as data_loader
import Scripts.data_saver as data_saver 


appointment_data = None 

def update_data():
    global appointment_data 
    appointment_data = data_loader.get_appointment_data() 

def get_docs_availiable_at(date_and_time, check_free = True):     
    for doc_id in appointment_data.keys():
        if is_availiable(doc_id, date_and_time):
            if check_free and not has_appointment(doc_id, date_and_time):
                continue 

            yield doc_id 


def is_availiable(doc_id, date_and_time):
    # returns whether this doc works at this time  ?
    doctor = appointment_data[doc_id]

    checkup_time = doctor["time_per_patient"] 

    for start, end in doctor["time_slots"]:
        if start <= date_and_time.time() and (date_and_time + checkup_time).time() <= end:
            return True 
    
    return False 

def has_appointment(doc_id, date_and_time):
    assert(is_availiable(doc_id, date_and_time))

    schedule = appointment_data[doc_id]['schedule'] 

    if date_and_time.date() not in schedule:  # no appointments on whole day
        return True 
    
    return date_and_time.time() not in schedule[date_and_time.date()] 


def book(date_and_time, doc_id, patient_id):
    doc_id = str(doc_id)

    check_if_booking_is_valid()     
    data_saver.add_booking(date_and_time, doc_id, patient_id) 

def check_if_booking_is_valid(doc_id, date_and_time):
    update_data() 
    assert(has_appointment(doc_id, date_and_time))


if __name__ == '__main__':
    import datetime 
    date_and_time = datetime.datetime(2022, 5, 1, 15)  

    # print('Availiable Docs:', *get_docs_availiable_at(date_and_time)) 
    book(date_and_time, 1, 1011)

