import sys
import myTesla as mt


def user_prompt(question: str) -> bool:
    """ Prompt the yes/no-*question* to the user. """
    from distutils.util import strtobool

    while True:
        user_input = input(question + " [y/n]: ").lower()
        try:
            result = strtobool(user_input)
            return result
        except ValueError:
            print("Please use y/n or yes/no.\n")

def main(email, password):
    myTesla = mt.connect(email, password)

    myTesla.get_access_token(email=email, password= password)
    #
    print(myTesla.vehicles())
    print(myTesla.mobile_enabled())
    print(myTesla.charge_state())
    print(myTesla.climate_state())
    print(myTesla.drive_state())
    print(myTesla.gui_settings())
    print(myTesla.vehicle_state())
    print(myTesla.wake_up())
    print(myTesla.set_valet_mode())
    print(myTesla.reset_valet_pin())
    print(myTesla.charge_port_door_open())
    print(myTesla.charge_standard())
    print(myTesla.charge_max_range())
    print(myTesla.set_charge_limit(limit_value=80))
    print(myTesla.charge_start())
    print(myTesla.honk_horn())
    print(myTesla.door_unlock())
    print(myTesla.door_lock())
    print(myTesla.set_temps(driver_temp=75, passenger_temp=75))
    print(myTesla.auto_conditioning_start())
    print(myTesla.auto_conditioning_stop())
    print(myTesla.sun_roof_control(state="comfort"))
    print(myTesla.trunk_open(which_trunk="rear"))


## run
if '__main__' in __name__:
    resp = user_prompt("Are you absolutely sure to execute all the possible API calls on your vehicle? ")
    if(resp):
        ## username and password should be passed via system arguement
        main(sys.argv[1], sys.argv[2])


