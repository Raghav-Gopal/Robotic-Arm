#Author-Raghav
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
# import ikpy.chain
def run(context):
    ui = None
    # target_position = [10,0,0]
    # target_position[0]-=-33.923
    # target_position[1]+=-255
    # target_position[2]-=226.457
    angles=[-7.1/04303530248728e-15, -0.8150924016239373, 1.0907703600722722, -1.5708059389319933, 1.570804254139342, 0.0]
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        root = design.rootComponent
        target_position=eval(ui.inputBox("Give a list for target_position","Coordinates","[0,0,0]")[0])
        # my_chain = ikpy.chain.Chain.from_urdf_file("C:\Raghav random\Fusion 360\Manipulator\Manipulator v2\Manipulator 4 link\Manipulatorv2.urdf")
        # angles = my_chain.inverse_kinematics(target_position,optimizer='scalar')
        # Angles = list(angles)
        frames=20
        # ui.messageBox("Hello")
        joint1 = root.joints.itemByName("Revolute 1")
        joint2 = root.joints.itemByName('Revolute 2')
        joint3 = root.joints.itemByName('Revolute 3')
        revolute1 = adsk.fusion.RevoluteJointMotion.cast(joint1.jointMotion)
        revolute2 = adsk.fusion.RevoluteJointMotion.cast(joint2.jointMotion)
        revolute3 = adsk.fusion.RevoluteJointMotion.cast(joint3.jointMotion)
        current_position_angles=[revolute1.rotationValue,revolute2.rotationValue,revolute3.rotationValue]
        # current_position = my_chain.forward_kinematics(current_position_angles)
        # Path1 = numpy.linspace(revolute1.rotationValue,angles[0],frames)
        # Path2 = numpy.linspace(revolute2.rotationValue,angles[1],frames)
        # Path3 = numpy.linspace(revolute3.rotationValue,angles[2],frames)
        # for i in range(frames):
        revolute1.rotationValue=angles[0]
        revolute2.rotationValue=angles[1]
        revolute3.rotationValue=angles[2]
        adsk.doEvents()
        # ui.messageBox("Done")
        # ui.messageBox(str(my_chain._urdf_metadata))

        # revolute.cast()
        # ui.messageBox(str(math.degrees(revolute.rotationValue)%360)+" deg","Current rotation value")
        # for i in range(100):
        #     revolute.rotationValue += math.radians(0.2)
        #     # time.sleep(3)
        #     adsk.doEvents()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
