
import sys
sys.path.append("..")

from assistant.cyton.cyton import CytonGamma300
from spatialmath import SE3
from assistant.items.BaseItem import BaseItem
from assistant.cyton.cyton_controller import CytonController

def main():
    # Create a CytonGamma300 robot object
    robot = CytonGamma300()

    # Define the starting pose for the robot
    starting_pose = robot.qz

    # Create a CytonController object
    controller = CytonController(robot=robot, starting_pose=starting_pose, connect=True)

    # Create a cube object with a known pose
    cube_pose = SE3(0.5, 0.3, 0.1)  # Replace with the actual cube pose
    cube = BaseItem(pose=cube_pose)

    # Define a drop-off location
    dropoff_location = SE3(0.7, -0.3, 0.1)  # Replace with the desired drop-off location

    # Execute the pick-and-place sequence
    controller.pick_and_place(cube, dropoff_location)

    # Disconnect the robot
    robot.disconnect()

if __name__ == "__main__":
    main()

# This script creates a CytonGamma300 robot object, defines its starting pose, and creates a CytonController object. 

# It then creates a cube object with a known pose, defines a drop-off location, and executes the pick-and-place 
# sequence using the pick_and_place method of the CytonController class. Finally, it disconnects the robot.

# We will make sure to replace the actual cube pose and desired drop-off location in the SE3() constructors with the 
# correct values for our specific scenario.