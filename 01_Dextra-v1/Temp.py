import ikpy.chain
import numpy as np
import ikpy.utils.plot as plot_utils
import math

my_chain = ikpy.chain.Chain.from_urdf_file("C:\Raghav random\Fusion 360\Manipulator\Manipulator.urdf")

target_position = [ 245, -260, 220]
# print("The angles of each joints are : ", my_chain.inverse_kinematics(target_position))
# print(math.degrees(-6*10**(-16)))
angles = my_chain.inverse_kinematics(target_position)
Angles = list(angles)
for i in Angles:
    i = math.radians(i)
print(list(Angles))
