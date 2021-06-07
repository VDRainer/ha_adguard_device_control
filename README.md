# ha_adguard_device_control
Allow/disallow devices in adguard home with home assistant.

I'm not a python developer, more a trial and error scripter, so please use my code at your own risk. :smile:

This reads a yaml config file, adds or removes device ip adresses to/from a list and posts them to the adguard home api.
The ip's are added/removed in the adguard DNS settings, blocked clients.
