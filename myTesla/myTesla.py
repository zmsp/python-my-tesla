import requests
from datetime import datetime

class connect:
    def __init__(self, email='', password='',
                vehicle_index=0,
                base_url="https://owner-api.teslamotors.com",
                access_token=None,
                tesla_backend_token_response=None,
                ownerapi_client_id="81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384",
                ownerapi_client_secret="c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3",
                ):
        '''
        The details of these parameters can be found on this page See https://tesla-api.timdorr.com/api-basics/authentication
        :param email: Your mytesla username
        :param password: Your mytesla password
        :param vehicle_index: Index of your vehicle, if you have multiple vehicle
        :param access_token:  # Access token can be used instead of email and password.
        :param tesla_backend_token_response: # A backend response can be used instead of email/password or accesss token. The format of the backend response is documented here https://tesla-api.timdorr.com/api-basics/authentication#response
        :param base_url: base_url is taken from https://timdorr.docs.apiary.io/#reference/authentication/tokens/get-an-access-token
        :param OWNERAPI_CLIENT_ID: OWNERAPI_CLIENT_ID is taken from https://tesla-api.timdorr.com/api-basics/authentication#post-oauth-token-grant_type-password
        :param OWNERAPI_CLIENT_SECRET:  OWNERAPI_CLIENT_SECRET is taken from https://tesla-api.timdorr.com/api-basics/authentication#post-oauth-token-grant_type-password
        '''

        self.base_url = base_url
        self.api_url = base_url + "/api/1"

        self.ownerapi_client_id = ownerapi_client_id
        self.ownerapi_client_secret = ownerapi_client_secret

        self.tesla_backend_token_response = tesla_backend_token_response

        if tesla_backend_token_response:
            access_token = tesla_backend_token_response['access_token']
            token_type = tesla_backend_token_response['token_type']

        if (access_token is None):
            access_token_resp = self.get_access_token(email=email, password=password)
        else: # Lets assume the user knows what he is doing. Assign the given token to auth header, assuming it is still type 'Bearer'
            self.headers = {"Authorization": "Bearer {}".format(access_token)}

        if vehicle_index is not None:
            self.select_vehicle(vehicle_index=vehicle_index)

    def select_vehicle(self, vehicle_index=None, vin=None, vehicle_id=None):
        vehicles = self.vehicles()
        if (vehicle_index is not None):
            self.vehicle_id = vehicles["response"][vehicle_index]["id"]
        elif (vin != None):
            for vehicle in vehicles["response"]:
                if (vehicle["vin"] == vin):
                    self.vehicle_id = vehicle["id"]
                    break
        elif (id is not None):
            self.vehicle_id = vehicle_id



    def get_access_token(self, email='', password='', force = False):
        '''
        :param email: Your mytesla username
        :param password: Your myTesla password
        :param force: Renew regardless of the expiry date
        '''
        if self.tesla_backend_token_response:
            if datetime.fromtimestamp(self.tesla_backend_token_response['created_at']+self.tesla_backend_token_response['expires_in']-5*86400) < datetime.utcnow(): # If our current access token is set to expire in the next 5 days we renew just to be save
                oauth_param = {
                    "grant_type": "refresh_token",
                    "client_id": self.ownerapi_client_id,
                    "client_secret": self.ownerapi_client_secret,
                    "refresh_token": self.tesla_backend_token_response['refresh_token'],
                }
            else: # Everything is fine with our current token so lets not make a redundant API call
                if force: # Unless the force is with us
                    oauth_param = {
                        "grant_type": "refresh_token",
                        "client_id": self.ownerapi_client_id,
                        "client_secret": self.ownerapi_client_secret,
                        "refresh_token": self.tesla_backend_token_response['refresh_token'],
                    }
                else:
                    return self.tesla_backend_token_response
        else:
            oauth_param = {
                "grant_type": "password",
                "client_id": self.ownerapi_client_id,
                "client_secret": self.ownerapi_client_secret,
                "email": email,
                "password": password,
            }

        try:
            # Note: This is 'sunny weather programming' assuming nothing goes ever wrong between your coder brain, the infrastructure in between and the APIs coder brain!!
            # tesla_api_response = requests.post(self.base_url + "/oauth/token", data=oauth_param).json()
            # Proper error handling was aadded based on  the note from @one4many
            r = requests.post(self.base_url + "/oauth/token",
                          data=oauth_param)
            r.raise_for_status()
            tesla_api_response = r.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        self.tesla_backend_token_response = tesla_api_response
        self.headers = {"Authorization": "{} {}".format(tesla_api_response['token_type'], tesla_api_response['access_token'])}
        return tesla_api_response

    def requests_get(self, *args, **kwargs):
        if self.tesla_backend_token_response and datetime.fromtimestamp(self.tesla_backend_token_response['created_at']+self.tesla_backend_token_response['expires_in']-5*86400) < datetime.utcnow():
            self.get_access_token()
        return(requests.get(*args, **kwargs))

    def requests_post(self, *args, **kwargs):
        if self.tesla_backend_token_response and datetime.fromtimestamp(self.tesla_backend_token_response['created_at']+self.tesla_backend_token_response['expires_in']-5*86400) < datetime.utcnow():
            self.get_access_token()
        data = {}
        if "data" in kwargs:
            data = kwargs.pop("data")
        return(requests.post(*args, **kwargs, json=data))

    # Vehicles
    def vehicles(self):
        '''

        :return: Retrieve a list of your owned vehicles
        '''
        return self.requests_get(self.api_url + "/vehicles", headers=self.headers).json()

    # state
    def get_data_request(self, state_name):
        '''
        Gets vehicle states
        :param state_name:
        :return:
        '''

        return self.requests_get(
            self.api_url + '/vehicles/{vehicle_id}/data_request/{state_name}'.format(vehicle_id=self.vehicle_id,
                                                                                     state_name=state_name),
            headers=self.headers).json()

    # State and Settings

    def mobile_enabled(self):
        '''
        Determines if mobile access to the vehicle is enabled.
        :return:
        '''
        return self.requests_get(self.api_url + '/vehicles/{vehicle_id}/mobile_enabled'.format(vehicle_id=self.vehicle_id),
                            headers=self.headers).json()

    def charge_state(self):
        '''
        Returns the state of charge in the battery.
        :return:
        '''
        return self.get_data_request("charge_state")

    def climate_state(self):
        '''
        Returns the current temperature and climate control state.
        :return:
        '''
        return self.get_data_request("climate_state")

    def drive_state(self):
        '''
        Returns the driving and position state of the vehicle.
        '''
        return self.get_data_request("drive_state")

    def gui_settings(self):
        '''
        Returns various information about the GUI settings of the car, such as unit format and range display.
        '''
        return self.get_data_request("gui_settings")

    def vehicle_state(self):
        '''
        Returns the vehicle's physical state, such as which doors are open.
        '''
        return self.get_data_request("vehicle_state")

    def nearby_charging_sites(self):
        '''
        Returns a list of nearby Tesla-operated charging stations. (Requires car software version 2018.48 or higher.)
        '''
        return self.get_data_request("nearby_charging_sites")
    # Vehicle Commands
    def post_command(self, command_name, data="", command_url="/vehicles/{vehicle_id}/command/{command_name}"):
        '''
        Helper method that posts requests to mytesla
        :param command_name:
        :param data:
        :param command_url:
        :return:
        '''
        return self.requests_post(
            self.api_url + command_url.format(vehicle_id=self.vehicle_id, command_name=command_name),
            headers=self.headers, data=data).json()

    def wake_up(self):
        '''
        Wakes up the car from the sleep state. Necessary to get some data from the car.
        '''
        return self.requests_post(self.api_url + "/vehicles/{vehicle_id}/wake_up".format(vehicle_id=self.vehicle_id),
                             headers=self.headers, data="").json()

    def set_valet_mode(self, on=False, password=None):
        '''
        Sets valet mode on or off with a PIN to disable it from within the car.
        :param on: boolean value whether to enable it. Example: true
        :param password: optional 4 digit pin. Example: 1234
        :return:
        '''
        data = {"on": on, "password": password}
        return self.post_command("set_valet_mode", data)

    def reset_valet_pin(self):
        '''
        Resets the PIN set for valet mode, if set.
        :return:
        '''
        return self.post_command("reset_valet_pin")

    def charge_port_door_open(self):
        '''
        Opens the charge port. Does not close the charge port (for now...). This endpoint also unlocks the charge port if it's locked.
        :return:
        '''
        return self.post_command("charge_port_door_open")

    def charge_standard(self):
        '''
        Set the charge mode to standard
        :return:
        '''
        return self.post_command("charge_standard")

    def charge_max_range(self):
        '''
        Set the charge mode to max range
        :return:
        '''
        return self.post_command("charge_max_range")

    def set_charge_limit(self, limit_value=None):
        '''
        Set the charge limit to a custom percentage.
        :param limit_value: number. Example: 80
        :return:
        '''
        return self.post_command("set_charge_limit",
                                 command_url="/vehicles/{vehicle_id}/command/{command_name}",
                                 data={"percent":limit_value})

    def charge_start(self):
        '''
        Start charging. Must be plugged in, have power available, and not have reached your charge limit.
        :return:
        '''
        return self.post_command("charge_start")

    def charge_stop(self):
        '''
        Stop charging. Must already be charging.
        :return:
        '''
        return self.post_command("charge_stop")

    def flash_lights(self):
        '''
        Flash the lights once.
        :return:
        '''
        return self.post_command("flash_lights")

    def honk_horn(self):
        '''
        Honk the horn once.
        :return:
        '''
        return self.post_command("honk_horn")

    def door_unlock(self):
        '''
        Unlock the car's doors.
        :return:
        '''
        return self.post_command("door_unlock")

    def door_lock(self):
        '''
        Lock the car's doors.
        :return:
        '''
        return self.post_command("door_lock")

    def set_temps(self, driver_temp=None, passenger_temp=None):
        '''
        Set the temperature target for the HVAC system.
        :param driver_temp: desired temperature on driver side. Example: 75
        :param passenger_temp: Example 75
        :return:
        '''
        return self.post_command("set_temps",
                                 command_url="/vehicles/{{vehicle_id}}/command/{{command_name}}?driver_temp={driver_temp}&passenger_temp={passenger_temp}".format(
                                     driver_temp=driver_temp, passenger_temp=passenger_temp))

    def auto_conditioning_start(self):
        '''
        Start the climate control system.
        :return:
        '''
        return self.post_command("auto_conditioning_start")

    def auto_conditioning_stop(self):
        '''
        Stop the climate control system.
        :return:
        '''
        return self.post_command("auto_conditioning_stop")

    def sun_roof_control(self, state="", percent=""):
        '''
        Controls the car's panoramic roof, if installed.
        :param state:  Required, The desired state of the panoramic roof. The approximate percent open values for each state are open = 100%, close = 0%, comfort = 80%, and vent = ~15% Exam
        :param percent: Optional, The percentage to move the roof to. Example: 50.
        :return:
        '''
        return self.post_command("sun_roof_control",
                                 command_url="/vehicles/{{vehicle_id}}/command/{{command_name}}?state={state}&percent={percent}".format(
                                     state=state, percent=percent))

    def remote_start_drive(self, password):
        '''
        Start the car for keyless driving. Must start driving within 2 minutes of issuing this request.
        :param password: the password to the authenticated my.teslamotors.com account. Example: edisonsux.
        '''
        return self.post_command("remote_start_drive",
                                 command_url="/vehicles/{{vehicle_id}}/command/{{command_name}}?password={password}".format(
                                     password=password))

    def trunk_open(self, which_trunk):
        '''
        Open the trunk or frunk. Call the endpoint again to close
        :param which_trunk: The trunk to open. rear and front are the only options Example: rear
        '''
        data = {"which_trunk": which_trunk}
        return self.post_command("trunk_open",command_url="/vehicles/{vehicle_id}/command/actuate_trunk", data = data)
