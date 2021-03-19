from typing import Union
from pyrep.robots.arms.arm import Arm
from pyrep.robots.end_effectors.gripper import Gripper
from pyrep.robots.end_effectors.suction_cup import SuctionCup


class Robot(object):
    """Simple container for the robot components.
    """

    def __init__(self, arm: Arm, gripper: Union[Gripper, SuctionCup]):
        self.arm = arm
        self.gripper = gripper

        # extend check open
        self.gripper.if_open = lambda: \
            (1.0 if self.gripper.get_open_amount()[0] > 0.9 else 0.0) \
                if self.is_grip() else \
                (1.0 if len(self.gripper.get_grasped_objects()) == 0 else 0.0)

    def is_grip(self):
        return isinstance(self.gripper, Gripper)
