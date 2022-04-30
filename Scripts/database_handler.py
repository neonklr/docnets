import json 

def load_database():
    database = open('data.json', 'r', encoding='utf-8')
    return json.load(database)