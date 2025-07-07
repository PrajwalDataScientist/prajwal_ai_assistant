import json

def get_profile_data():
    with open('config/profile.json', 'r', encoding='utf-8') as file:
        profile = json.load(file)
    return json.dumps(profile, indent=2)

def get_about():
    with open('config/profile.json', 'r', encoding='utf-8') as file:
        profile = json.load(file)
    return profile.get('about', 'Sorry, no about information found.')
