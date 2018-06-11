
# Usage:

```python

import myTesla

my_model_s = myTesla.connect('test@example.com', 'MySecurePassword')
charge_state = my_model_s.charge_state()
door_lock = my_model_s.door_lock()
my_model_s.honk_horn()
print(charge_state)
print(door_lock)
```

# Documentation: 
This program was build using API documentation listed on  https://timdorr.docs.apiary.io/#. The functions closely follow the API documentation. Please see this page for detailed information.

## Function Descriptions
* `myTesla.connect.vehicles`: Retrieve a list of your owned vehicles
* `myTesla.connect.mobile_enabled`: Determines if mobile access to the vehicle is enabled.
* `myTesla.connect.charge_state`: Returns the state of charge in the battery.
* `myTesla.connect.climate_state`: Returns the current temperature and climate control state.
* `myTesla.connect.drive_state`: Returns the driving and position state of the vehicle.
* `myTesla.connect.gui_settings`: Returns various information about the GUI settings of the car, such as unit format and range display.
* `myTesla.connect.vehicle_state`: Returns the vehicle's physical state, such as which doors are open.
* `myTesla.connect.wake_up`: Wakes up the car from the sleep state. Necessary to get some data from the car.
* `myTesla.connect.set_valet_mode`: Sets valet mode on or off with a PIN to disable it from within the car.
* `myTesla.connect.reset_valet_pin`: Resets the PIN set for valet mode, if set.
* `myTesla.connect.charge_port_door_open`: Opens the charge port.
* `myTesla.connect.charge_standard`: Set the charge mode to standard
* `myTesla.connect.charge_max_range`: Set the charge mode to max range
* `myTesla.connect.set_charge_limit`:Set the charge limit to a custom percentage.
* `myTesla.connect.charge_start`: Start charging. Must be plugged in, have power available, and not have reached your charge limit.
* `myTesla.connect.charge_stop`: Stop charging. Must already be charging.
* `myTesla.connect.honk_horn`: Honk horn
* `myTesla.connect.door_unlock`:  Unlock the car's doors.
* `myTesla.connect.door_lock`: Lock the car doors.
* `myTesla.connect.set_temps`: Set the temperature target for the HVAC system.
* `myTesla.connect.auto_conditioning_start`: Start the climate control system. Will cool or heat automatically, depending on set temperature.
* `myTesla.connect.auto_conditioning_stop`: Stop the climate control system.
* `myTesla.connect.sun_roof_control`: Controls the car's panoramic roof, if installed.
* `myTesla.connect.remote_start_drive`: Start the car for keyless driving. Must start driving within 2 minutes of issuing this request.
* `myTesla.connect.trunk_open`: Open the trunk or frunk. Call the endpoint again to close (this only works on rear powered trunks)





# Legal Agreement/ Disclaimer
This program is provided as is. This program is not supported or endorsed by Tesla Motors. By using this software, you agree to not hold me (Zobair Shahadat ) liable for anything.
