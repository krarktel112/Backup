import SmartThings

token = '372563b7-09f8-485b-8c95-261793424ad9'
ST = SmartThings.Account(token)
ST.control_device(ST.devices['Home']['Ashley idle'], capability=None, command=None, arguments=None)
# Reference the SmartThings API documentation for information regarding the
# format of capabilities, commands, and arguments

"""ST.execute_scene(ST.scenes[LOCATION_NAME][DEVICE_NAME])
"""
