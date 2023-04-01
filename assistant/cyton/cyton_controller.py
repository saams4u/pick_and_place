
import sys
sys.path.append("..")

from assistant.cyton.cyton import CytonGamma300
from spatialmath import SE3
from assistant.items.BaseItem import BaseItem
from roboticstoolbox import jtraj

class CytonController:
    """
    Management class for performing specific actions with the cyton gamma robot. Also provides an interface for
    sending commands to the robot
    """

    def __init__(self, robot: CytonGamma300 = None, starting_pose: SE3 = None, connect: bool = False):

        if robot is None:
            self.robot = CytonGamma300()

        if starting_pose is None:
            self.pose = self.robot.qz

        self.connect = connect

        if self.connect:
            self.establish_connection()

        print(f"Setting starting pose to {self.pose}")

        self.set_pose(self.pose)

    def establish_connection(self) -> bool:
        """
        Establishes a connection to the robot
        :return: True/False whether the connection was successful
        """
        print(f"Establishing Connection to {self.robot.name}")

        # Replace with actual robot connection function
        self.robot.connect()

    def set_pose(self, q: SE3):
        """
        Sets the pose for the robot. If connected, then it sets the robot's end effector pose.
        :param q: Pose (SE3)
        :return:
        """
        # Replace with the actual robot command function
        self.robot.set_pose(q)

    def open_gripper(self):
        """
        Opens the gripper
        :return: None
        """
        # Replace with the actual gripper control function
        self.robot.open_gripper()

    def close_gripper(self):
        """
        Closes the gripper
        :return: None
        """
        # Replace with the actual gripper control function
        self.robot.close_gripper()

    def pick_and_place(self, item: BaseItem, dropoff_location: SE3):
        """
        Executes a pick-and-place sequence with the robot.
        :param item: The object to be picked up
        :param dropoff_location: The drop-off location for the object
        :return: None
        """
        # Go to the object location
        self.goto_object(item)

        # Close the gripper to pick up the object
        self.close_gripper()

        # Move to the drop-off location
        self.goto_location(dropoff_location)

        # Open the gripper to drop off the object
        self.open_gripper()

    def goto_object(self, item: BaseItem):
        robot_object_pose = self.robot.ikine_LM(item.pose, q0=self.pose)
        traj = jtraj(self.pose, robot_object_pose, 100)

        # Replace with actual robot trajectory execution function
        self.robot.execute_trajectory(traj)

    def goto_location(self, location: SE3):
        robot_location_pose = self.robot.ikine_LM(location, q0=self.pose)
        traj = jtraj(self.pose, robot_location_pose, 100)

        # Replace with actual robot trajectory execution function
        self.robot.execute_trajectory(traj)


# In the updated version of our code, I've added the open_gripper, close_gripper, pick_and_place, goto_object, 
# and goto_location methods. These methods allow the Cyton robot to pick up and drop off a small cube by 
# going to the cube location, picking up the block by closing the gripper, and dropping off the block by 
# opening the gripper. Note that we still need to implement the actual gripper control and trajectory execution 
# in the TODO sections above.