import datetime
from Scripts.database_handler import load_database


def preprocess_time_intervals(time_intervals):
    for interval in time_intervals:
        start, end = interval.split('-') 
        yield (datetime.time(start), datetime.time(end)) 

doctors = None 
def update_doctors():
    global doctors 
    
    doctors = load_database()
    

def get_docs_availiable_at(time, check_free = True): 
    update_doctors()

    for doctor in doctors:
        if is_availiable_at(doctor, time, check_free):
            yield doctor


def is_availiable_at(doctor, time, check_free = True):
    time_intervals = doctors[doctor]["timeSlots"]
    timePerPatient = doctors[doctor]["timePerPatient"]
    occupiedTill = doctors[doctor]["occupied"]
    
    for start, end in time_intervals:
        if (start <= time <= end) and (check_free or (end - time) >= timePerPatient):
            return True
