import requests
import yaml
import sys

devices = sys.argv[1]
todo = sys.argv[2]

# The (full) path to the config file
config_file = '/home/homeassi/.homeassistant/adguard_clients.yaml'

# The ip or hostname of the adguard instance
adg_ip = '192.168.111.33'
geturl = 'http://' + adg_ip + '/control/access/list'
seturl = 'http://' + adg_ip + '/control/access/set'

# Not sure if this is needed, but after adguard installation these entries are in Disallowed domains
adg_blocked_hosts = ["version.bind","id.server","hostname.bind"]

# You can create the base64-encoded data for username:password string here: https://www.base64encode.org/ 
headers = {
    'Authorization': 'Basic dXNlcjpwYXNzd29yZA==',
    'content-type': 'application/json'
}

def read_config_yaml():
    with open(config_file, 'r') as stream:
        try:
            config = yaml.load(stream, Loader=yaml.BaseLoader)
        except yaml.YAMLError as exc:
            print(exc)
    return config

def get_json():
    r = requests.get(geturl, headers=headers)
    return r.json()['disallowed_clients']

def post_json(json):
    r = requests.post(seturl, json=json, headers=headers)
    #print(str(r.status_code))

config = read_config_yaml()

#print(config.keys())
if devices in config.keys():
    adg_clients_list = get_json()
    set_devices = set(config[devices])
    set_adglist = set(adg_clients_list)

    if todo in ['state','on','off']:

        if todo == 'state':
            print(set_devices.issubset(set_adglist))

        elif todo == 'on':
            for device in config[devices]:
                adg_clients_list.append(device) if device not in adg_clients_list else adg_clients_list
            json = {"allowed_clients": [],"disallowed_clients": adg_clients_list,"blocked_hosts": adg_blocked_hosts}
            post_json(json)

        elif todo == 'off':
            for device in config[devices]:
                if device in adg_clients_list:
                    adg_clients_list.remove(device)
            json = {"allowed_clients": [],"disallowed_clients": adg_clients_list,"blocked_hosts": adg_blocked_hosts}
            post_json(json)
