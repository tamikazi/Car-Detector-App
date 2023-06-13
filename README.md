# Car Detector Simulation


## 💻 Program Specifications
Computer vision and the related data processing allows cars to detect obstacles in their path. This is a terminal-based application for determining a course of action depending on detected obstacles.

* Specifications:
  * Select 1 to update the detected traffic light colour, 2 to update whether a pedestrian is detected, 3 to update whether a vehicle is detected, 0 to end the program
  * If menu option 1, 2 or 3 are detected, the user is prompted to specify the detected change
    * A traffic light can be "green", "yellow", or "red"
    * Pedestrian status can be "yes" or "no"
    * Vehicle status can be "yes" or "no"
  * A course of action message is printed following the status change
    * Any scenario where a red light, a pedestrian or a vehicle are detected should display the message "STOP"
    * A green light with no pedestrian or vehicle detected should display the message "Proceed"
    * A yellow light with no pedestrian or vehicle detected should display the message "Caution"
  * After the action message, the current status of each monitored condition will be printed

