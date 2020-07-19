# Install
You can install latest stable version from PyPI:

```pip3 install myTesla```

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
This program was build using API documentation listed on  [https://tesla-api.timdorr.com/](https://tesla-api.timdorr.com/.). The functions closely follow the API documentation. Please see this page for detailed information of the function parameters.

## Initiating connection
In order to initiate connection, the following information is needed.  

The arguements for initiating the connection is the following:  

```python
def __init__(self, email='', password='',
            vehicle_index=0,
            base_url="https://owner-api.teslamotors.com",
            access_token=None,
            tesla_backend_token_response=None,
            ownerapi_client_id="81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384",
            ownerapi_client_secret="c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3",
            )
```
### Connection arguement description descriptioons: 

The details of these parameters can be found on this page See https://tesla-api.timdorr.com/api-basics/authentication
* `email`: Your mytesla username
* `password`: Your mytesla password
* `vehicle_index`: Index of your vehicle, if you have multiple vehicles
* `access_token`:  # Access token can be used instead of email and password.
* `tesla_backend_token_response`: # A backend response can be used instead of email/password or accesss token. The format of the backend response is documented here https://tesla-api.timdorr.com/api-basics/authentication#response
* `base_url`: base_url is taken from https://timdorr.docs.apiary.io/#reference/authentication/tokens/get-an-access-token
* `OWNERAPI_CLIENT_ID`: OWNERAPI_CLIENT_ID is taken from https://tesla-api.timdorr.com/api-basics/authentication#post-oauth-token-grant_type-password
* `OWNERAPI_CLIENT_SECRET`:  OWNERAPI_CLIENT_SECRET is taken from https://tesla-api.timdorr.com/api-basics/authentication#post-oauth-token-grant_type-password


## Function Descriptions
* `myTesla.connect.get_access_token`: Returns access token information that could be used to authenticate instead of email/password.
* `myTesla.connect.select_vehicle`: Switches car based on index/vin/or vehicle_id if you have multiple vehicle on your account.
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
This program is provided as is. This program is not supported or endorsed by Tesla Motors. By using this software, you agree to not hold me (Zobair Shahadat ) and any of the contributers liable for anything.
