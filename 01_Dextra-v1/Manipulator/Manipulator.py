#Author-Raghav
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
# import ikpy.chain
def run(context):
    ui = None
    target_position = [0,0,0]
    # target_position[0]-=-33.923
    # target_position[1]-=38.217
    # target_position[2]-=226.457
    angles=[9.919407061998911e-16, -0.8150924007650445, 1.0689847356989566, -1.5707728846335733, 1.5707846872088334, 0.0]
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        root = design.rootComponent
        # my_chain = ikpy.chain.Chain.from_urdf_file("C:\Raghav random\Fusion 360\Manipulator\Manipulator.urdf")
        # angles = my_chain.inverse_kinematics(target_position)
        # Angles = list(angles)
        frames=200
        # ui.messageBox("Hello")
        joint1 = root.joints.itemByName("Revolute 1")
        joint3 = root.joints.itemByName('Revolute 3')
        joint4 = root.joints.itemByName('Revolute 4')
        joint5 = root.joints.itemByName('Revolute 5')
        joint6 = root.joints.itemByName('Revolute 6')
        revolute1 = adsk.fusion.RevoluteJointMotion.cast(joint1.jointMotion)
        revolute3 = adsk.fusion.RevoluteJointMotion.cast(joint3.jointMotion)
        revolute4 = adsk.fusion.RevoluteJointMotion.cast(joint4.jointMotion)
        revolute5 = adsk.fusion.RevoluteJointMotion.cast(joint5.jointMotion)
        revolute6 = adsk.fusion.RevoluteJointMotion.cast(joint6.jointMotion)
        current_position_angles=[revolute1.rotationValue,revolute3.rotationValue,revolute4.rotationValue,revolute5.rotationValue,revolute6.rotationValue]
        # # current_position = my_chain.forward_kinematics(current_position_angles)
        # Path1 = numpy.linspace(revolute1.rotationValue,angles[0],frames)
        # Path3 = numpy.linspace(revolute3.rotationValue,angles[1],frames)
        # Path4 = numpy.linspace(revolute4.rotationValue,angles[2],frames)
        # Path5 = numpy.linspace(revolute5.rotationValue,angles[3],frames)
        # Path6 = numpy.linspace(revolute6.rotationValue,angles[4],frames)
        # for i in range(frames):
        #     if revolute1.rotationValue==Path1[-1] or revolute3.rotationValue==Path3[-1] or revolute4.rotationValue==Path4[-1] or revolute5.rotationValue==Path5[-1] or revolute6.rotationValue==Path6[-1]:
        #         break
        #     revolute1.rotationValue=(Path1[i])
        #     revolute3.rotationValue=(Path3[i])
        #     revolute4.rotationValue=(Path4[i])
        #     revolute5.rotationValue=(Path5[i])
        #     revolute6.rotationValue=(Path6[i])
        #     adsk.doEvents()
        revolute1.rotationValue=angles[0]
        revolute3.rotationValue=angles[1]
        revolute4.rotationValue=angles[2]
        revolute5.rotationValue=angles[3]
        revolute6.rotationValue=angles[4]
        adsk.doEvents()
        ui.messageBox("Done")

        # revolute.cast()
        # ui.messageBox(str(math.degrees(revolute.rotationValue)%360)+" deg","Current rotation value")
        # for i in range(100):
        #     revolute.rotationValue += math.radians(0.2)
        #     # time.sleep(3)
        #     adsk.doEvents()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
