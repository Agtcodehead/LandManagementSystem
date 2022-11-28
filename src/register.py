import json

def write_json_user(new_data, filename='user_stats.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["user_stats"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def update_json_property(new_data, prop):
    with open("property_stats.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data[prop]["owner"] = new_data
    with open("property_stats.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)

def register_users():
    while(True):
        username = input("Register a username: ")
        password = input("Make a password: ")
        temp = input("Do you have any previously owned properties? [y/n] ")
        if(temp=="y"): properties_owned = input("Enter all previously owned properties seperated with no spaces: ")
        else: properties_owned = None

        y = {
                "username": username,
                "password": password,
                "properties_owned": properties_owned
            }
        write_json_user(y)

        z = properties_owned
        if(z!=None):
            x = []
            x[:0] = z

            for owned in x:
                prop = "Property " + owned
                update_json_property(username, prop)

        more = input("Do you wish to register more users?[y/n] ")
        if(more=="n"):
            break