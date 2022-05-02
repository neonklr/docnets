import json 
import datetime 

from Scripts.constants import * 


class TimePreProcessor:
    def preprocess_times(self, appointments: dict):
        for doctor in appointments.values():
            self.preprocess_doctor(doctor) 

    def preprocess_doctor(self, doctor: dict):
        doctor['time_per_patient'] = self.preprocess_time_to_timedelta(doctor['time_per_patient'])
        doctor['time_slots'] = self.preprocess_intervals(doctor['time_slots'])
        

    def preprocess_intervals(self, intervals):
        # intervals: a list of interval
        return tuple(map(
            self.preprocess_interval, intervals
        ))

    def preprocess_interval(self, interval):
        # interval should be like:  "12:40-15:20:30" 
        return tuple(map(
            self.preprocess_time, interval.split('-') 
        ))
    
    def preprocess_time_to_timedelta(self, time):
        time = self.preprocess_time(time) 
        return datetime.timedelta(
            hours=time.hour, 
            minutes=time.minute,
            seconds=time.second
        )

    def preprocess_time(self, time):
        # time should be like:  "2:50"  
        return datetime.time(*map(int, time.split(':')))

    
class SchedulePreProcessor:
    def preprocess_schedules(self, appointments):
        for doc_data in appointments.values():
            doc_data['schedule'] = self.get_preprocessed_schedule(doc_data['schedule'])

    def get_preprocessed_schedule(self, raw_schedule):
        schedule = {}  
        for date, schedule_of_day in raw_schedule.items():
            date = datetime.date(*map(int, date.split('-'))) 
            schedule_of_day = self.get_preprocessed_schedule_of_day(schedule_of_day)

            schedule[date] = schedule_of_day 
    
        return schedule 
    
    def get_preprocessed_schedule_of_day(self, raw_schedule_of_day):
        schedule_of_day = {} 
        for time, patient_id in raw_schedule_of_day.items():
            time = datetime.time(*map(int, time.split(':'))) 

            schedule_of_day[time] = patient_id 
        
        return schedule_of_day 




time_preprocessor = TimePreProcessor() 
schedule_preprocessor = SchedulePreProcessor() 



def get_appointment_data(preprocess_time = True, preprocess_schedule = True):
    with open(APPOINTMENT_FILE_PATH, 'r') as file:  # TODO: encoding = 'utf-8' or something  ?
        data = json.load(file) 
    
    if preprocess_time:
        time_preprocessor.preprocess_times(data) 
    
    if preprocess_schedule:
        schedule_preprocessor.preprocess_schedules(data)

    return data 


def get_doctors_data():
    with open(DOCTORS_FILE_PATH, 'r') as file:
        data = json.load(file) 
    
    return data 

def get_users_data():
    with open(USERS_FILE_PATH, 'r') as file:
        data = json.load(file) 
    
    return data 

if __name__ == '__main__':
    data = get_appointment_data() 

    for doc in data.values():
        print(*doc.values(), sep = '\n') 
        print('\n')