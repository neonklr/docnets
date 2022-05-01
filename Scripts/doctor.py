import Scripts.data_loader as data_loader
import Scripts.data_saver as data_saver 

# import data_loader 
# import data_saver 


appointment_data = None 
doctors_data = None 

def reload_appointment_data():
    global appointment_data 
    appointment_data = data_loader.get_appointment_data() 

def reload_doctors_data():
    global doctors_data 
    doctors_data = data_loader.get_doctors_data() 



def get_nearest_docs(loc):
    reload_doctors_data() 

    return sorted(
        doctors_data.keys(), 
        key = lambda doc_id: distance2(
            doctors_data[doc_id]["location"], loc
        )
    ) 

def distance2(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2   


def get_docs_sorted_by(criteria):
    assert(criteria in ["fees", "experience", "rating"])
    reload_doctors_data() 

    return sorted(
        doctors_data.keys(), 
        key = lambda doc_id: doctors_data[doc_id][criteria], 
        reverse = criteria != "fees"
    )

def get_docs_availiable_at(date_and_time, check_free = True):     
    reload_appointment_data() 

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

    assert(is_future_date(date_and_time)) 
    assert(check_if_booking_is_valid(doc_id, date_and_time))

    data_saver.add_booking(date_and_time, doc_id, patient_id) 

def check_if_booking_is_valid(doc_id, date_and_time):
    reload_appointment_data() 
    return has_appointment(doc_id, date_and_time)

def is_future_date(date_and_time):
    from datetime import datetime 
    
    return datetime.now() <= date_and_time 




if __name__ == '__main__':
    import datetime 

    for c in ["fees", "experience", "rating"]:
        print(c, get_docs_sorted_by(c))
    # date_times = [datetime.datetime(2022, 5, 2, 14), datetime.datetime(2022, 5, 3, 10)]

    # for date_and_time in date_times:
    #     print('Availiable Docs:', *get_docs_availiable_at(date_and_time)) 
    #     book(date_and_time, 2, 1013)


    # print(get_nearest_docs((400, 400)))

