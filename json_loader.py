import json 

def get_config():
    with open('config.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def save_personal(data):
    with open('user_data.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data))

def get_saved_location():
    with open('user_config', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data
    