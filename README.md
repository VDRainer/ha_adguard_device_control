# ha_adguard_device_control
Allow/disallow devices in adguard home with home assistant.

This is my first github repository.

I'm not a python developer, more a trial and error scripter, so please use my code at your own risk. :smile:

❗ I have no clue if this works with the adguard addon in a supervised HA installation.  
I'm one of the 4.2% HA Core users 🙂

This reads a yaml config file, adds/removes device ip adresses to/from a list and posts them to the adguard home api.  
The ip's are added/removed in adguard > Settings > DNS settings > Disallowed clients.

## Installation
Copy the adgaurd_clients.yaml to your home assistant config directory and edit it for your needs.

Copy the adguard_clients.py to your home assistant config directory (i have it in a subfolder 'scripts') and edit the path to the adguard_clients.yaml file.  
Also change the ip (or hostname, if your local dns is running properly) to your adguard instance.  
Create a base64-encoded data for your username:password string to access adguard api and copy it in the adguard_clients.py.  
You can do this here: https://www.base64encode.org/ 

## Testing the script
Open a terminal in ha, activate your python venv, go to your config directory.  
Now you can run the script with:
```
python path/to/adguard_clients.py key_from_config state/on/off
```
See the example command_line switches in the home_assistant_config.yaml file.

Browse to your adguard DNS Setting and see if the ip's of the clients are added/removed from the 'Disallowed Clients' setting. (Reload the browser tab)

If this works, add the command_line switches to your HA config.

Suggestions and improvements are highly appreciated!

Adguard Home API: https://github.com/AdguardTeam/AdGuardHome/tree/master/openapi
