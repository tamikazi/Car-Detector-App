# input_processing.py
# Tahmid Kazi, ENSF 592 P23
# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:
    valid_colour = ["green", "yellow", "red"]
    valid_decision = ["yes", "no"]
    valid_input = [1, 2, 3]
    light = "green"

    def __init__(self, light, pedestrian = "no", vehicle = "no"):
        self.light = light
        self.pedestrian = pedestrian
        self.vehicle = vehicle

    # update_status takes in 2 user inputs as arguments:
    #   "input1" is what the user selects based on if they would like to select 1: changes in the light colour, 2: changes in the pedestrian status, 3: changes in the vehicle status
    #   "status" is the second user input that determines what the change is, valid inputs for light are "green", "yellow" and "red" and for pedestrian and vehicle, they are "yes" and "no"
    # The if/else ladder passes the following and uses exception handling with the following:
    #   Setting self.light to the user input status by verifying which # input that the user has selected based on the valid_input list
    #   Setting self.pedestrian and self.vehicle to the user input status by ensuring that the user has input a valid status based on the valid_colour list for light and valid_decision for pedestrian and vehicle
    # For any invalid entires, the error message will print and print_message will run regardless of the the user input for status
    def update_status(self, input1, status):
        if input1 == 1 and status in self.valid_colour:
            self.light = status
        elif input1 == 2 and status in self.valid_decision:
            self.pedestrian = status
        elif input1 == 3 and status in self.valid_decision:
            self.vehicle = status
        else:
            print("Invalid vision change.")
        print_message(self) # ****-> should be in main****

# The sensor object is the argument passed into this print_message() function to print the action message and current status
#   "STOP" is printed if there are pedestrians or vehicles detected, or there is a red light
#   "Caution" is printed if the light is yellow and there are no pedestrians or vehicles
#   "Proceed" is printed if the light is green and and there are no pedestrians or vehicles
# The status of light, pedestrian and vehicle is printed after the action message
def print_message(sensor):
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("\nSTOP\n")
    elif sensor.light == "yellow":
        print("\nCaution\n")
    elif sensor.light == "green": #****since pedestrian and vehicle are yes/no, the conditions of no aren't required****
        print("\nProceed\n")
    print("""Light = {0} , Pedestrian = {1} , Vehicle = {2} .""".format(sensor.light, sensor.pedestrian, sensor.vehicle))

# This is the main of the program where the program begins, starting with the creation of the Sensor object
# The user is prompted to select 1 of 4 options initially:
#   0: ends the program
#   1: selects a change in the light status
#   2: selects a change in the pedestrian status
#   3: selects a change in the vehicle status
#   Any inputs other than the above will raise a ValueError, giving instructions and prompting the user to select a valid entry
# The user is then prompted to enter what the status change was for their selected choice
# Both inputs (input1 and status) are passed into the update_status() function - see comments above for how the inputs are handled
def main():
    print("\n***ENSF 592 Car Vision Detector Processing Program***")
    sensor = Sensor()
    print(sensor.light)
    while True:
        try:
            print("\nAre changes detected in the vision input?")
            input1 = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "))
            if input1 == 0:
                break
            elif input1 in sensor.valid_input:
                status = input("What change has been identified?: ")
                sensor.update_status(input1, status)
                #***print_message(sensor)****
            else:
                raise ValueError()
        except ValueError:
            print("You must select either 1, 2, 3 or 0.")

# Conventional Python code for running main within a larger program
if __name__ == '__main__':
    main()

