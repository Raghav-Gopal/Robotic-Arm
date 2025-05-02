#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback,math,time

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        # ui.messageBox('Hello script')
        design = app.activeProduct
        root = design.rootComponent
        joint1 = root.joints.itemByName('Main')
        joint2 = root.joints.itemByName('Inverse 1')
        joint3 = root.joints.itemByName('Inverse 2')
        
        
        Main = adsk.fusion.RevoluteJointMotion.cast(joint1.jointMotion)
        Inverse_1 = adsk.fusion.RevoluteJointMotion.cast(joint2.jointMotion)
        Inverse_2 = adsk.fusion.RevoluteJointMotion.cast(joint3.jointMotion)
        lat_ang=0
        # Main.rotationValue = math.radians(180)
        # adsk.autoTerminate(False)
        for j in [-180,-90,0,90]:
            for i in range(0,181):
                Inverse_1.rotationValue=math.acos((2*math.cos(math.radians(i/2)) - 1))
                Inverse_2.rotationValue = -1*Inverse_1.rotationValue
                Main.rotationValue = -1*math.atan((math.tan(Inverse_1.rotationValue/2))/(math.sqrt(2))) + +math.radians(j)
                # time.sleep(0.05)/
                if i==90 or i==180:
                    time.sleep(2)
                adsk.doEvents()
            # time.sleep(0.05)
            Inverse_1.rotationValue=0
            Inverse_2.rotationValue=0
            Main.rotationValue=0
            
        adsk.terminate()
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
