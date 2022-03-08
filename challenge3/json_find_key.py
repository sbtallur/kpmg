import json

def find_key(key):
    with open('json_data.json', 'r') as json_file:
        json_load = json.load(json_file)
        print(json_load[key])


if __name__ == '__main__':
    key = input("What key would you like to find?\n")
    print(find_key(key))