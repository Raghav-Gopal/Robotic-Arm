#Author-
#Description-

import adsk, adsk.core, adsk.fusion, adsk.cam, traceback, math
# from numpy import linspace

def run(context):
    ui = None
    try:
        l1 = 150 # Link_1 length
        l2 = 92.5 # Link_2 length
        Oo = 12.5 # Origin offset #U forgot to include this
        def inverse_kinematics(Intermediate_set:list):        
            global a
            global b     
            Old_coords = []
            Target_position = [5,5,5]
            # Intermediate_set = [70,70,100]
            Intermediate_set[2]-=Oo
            d=0
            for i in Intermediate_set:
                d+=i**2
            droot = (math.sqrt(d))
            
            X=Intermediate_set[0]
            Y=Intermediate_set[1]
            Z=Intermediate_set[2]
            a = math.sqrt((X**2)+(Y**2))
            q3 = math.atan2(Y,X)
            a=abs(a)
            Z+abs(Z)
            q2_Num = a**2 + Z**2 -l1**2 - l2**2
            q2_Den = 2*l1*l2
            q2 = math.acos(q2_Num/q2_Den)
            q2=-q2
            # temp = abs(math.atan2(Z-Oo,X))4
            q1_tan_num = l2*(math.sin(q2))
            q1_tan_den = l1 + l2*(math.cos(q2))
            q1 = (math.atan2(Z,a)) - math.atan2(q1_tan_num,q1_tan_den)
            # if q1>math.radians(90):
            #     q1 = math.radians(180)-q1
            # if temp>math.radians(90):
            #     temp = math.radians(180)-temp
            # if q1>temp:
            #     q2=-q2


            

            Angles = [q1,q2,q3]
            return(Angles)
        # print(Angles)
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        root = design.rootComponent
        joint1 = root.joints.itemByName("Revolute 1")
        joint2 = root.joints.itemByName('Revolute 2')
        joint3 = root.joints.itemByName('Revolute 3')
        
        
        revolute1 = adsk.fusion.RevoluteJointMotion.cast(joint1.jointMotion)
        revolute2 = adsk.fusion.RevoluteJointMotion.cast(joint2.jointMotion)
        revolute3 = adsk.fusion.RevoluteJointMotion.cast(joint3.jointMotion)
        theta1 = revolute1.rotationValue
        theta2 = revolute2.rotationValue
        theta3 = revolute3.rotationValue
        old_X = l2*(math.cos(theta2+theta3))*(math.cos(theta1)) + l1*(math.cos(theta2))*(math.cos(theta1))
        old_Y = l2*(math.cos(theta2+theta3))*(math.sin(theta1)) + l1*(math.cos(theta2))*(math.sin(theta1))
        old_Z = l2*(math.sin(theta2+theta3)) + l1*(math.sin(theta2))
        old_Z+=Oo
        for i in range(0,200):
            Angles = inverse_kinematics([old_X-i/3,old_Y+i,old_Z-i/5])
            if Angles[1]<-95:
                ui.statusMessage = "What is this?"
            revolute1.rotationValue=Angles[2]
            revolute2.rotationValue=Angles[0]
            revolute3.rotationValue=Angles[1]
            adsk.doEvents()
        #     # time.sleep(0.05)
        # jointOriginList = root.jointOrigins
        # test_1 = jointOriginList.itemByName("Revolute 1")  # Replace with actual joint origin name
        # ui.messageBox(str([old_X,old_Y,old_Z]))
        # Angles = inverse_kinematics([50,0,50])
        # revolute1.rotationValue=Angles[2]
        # revolute2.rotationValue=Angles[0]
        # revolute3.rotationValue=Angles[1]
        # adsk.doEvents()
        # Angles = list(map(math.degrees,Angles))
        # ui.messageBox(str([a,b]))
        adsk.terminate()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.forma9t(traceback.format_exc()))
