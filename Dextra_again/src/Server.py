import socket
import json
import time
from sympy import symbols, cos, sin, Eq, solve, simplify, atan2, sqrt, acos
from sympy.abc import x,y
import math
import numpy
import sys
# MODE = 0 - Angle Command; 1- Straightness test (H); 2- Straightness test (V); 3- Coordinate Mode; 4- Offline movement
mode = 4

L_1 = 250 #mm Link length 1 
L_2 = 250 #mm Link length 2


pathX = numpy.concatenate(([50]*200,numpy.linspace(50,500,num=200), numpy.linspace(500,50, num=200)))
pathY = [0]*len(pathX)

#Max angle = 76
#Min angle = 9

jsonStep = {"topServoAngle":10,"bottomServoAngle":90, "detachTop":0, "detachBase":0, "iter":0, "total":0}
oldBaseAngle = 10
oldTopAngle = 10
oldDetachTop = 0
oldDetachBase = 0
iter_var = 0
Handshake = 0
serverPower = 1


def map_range(x, in_min=0, in_max=180, out_min=500, out_max=2400):
    mapped = ((x - in_min) * (out_max - out_min) / (in_max - in_min)) + out_min
    print(max(min(mapped, out_max), out_min))
    return max(min(mapped, out_max), out_min)
def invKin(x,y):
    q2 = (acos((x**2 + y**2 -L_1**2 - L_2**2)/(2*L_1*L_2)))
    q1 = (-atan2(y,x) - atan2((L_2*sin(q2)),(L_1 + L_2*cos(q2))))
    q2 = (math.degrees(q2))
    q1 = abs(math.degrees(q1))
    # print(q1,q2)
    q1_servo = (round(map_range((q1-4.5)/0.375)))
    q2_servo = (round(map_range((q2))))
    return [q1_servo, q2_servo]
def connect():
    global client_socket, client_address
    while True:
        try:
            print("Waiting for client to connect")
            client_socket, client_address = server.accept()
            print(f"Client connected from {client_address}")
            break
        except Exception as e:
            print("Error accepting connection:",e)
            time.sleep(1)
def Mode0(client_socket, jsonStep):
    global oldDetachBase
    global oldBaseAngle
    global oldDetachTop
    global oldTopAngle
    global Handshake
    if Handshake==0:
        client_socket.sendall("1\n".encode('utf-8')) # Declaring OTA mode
        Handshake=1
        print(b'Sending 1\n')
        time.sleep(0.5)
    val = (input("Bottom Servo angle: "))
    if val.isnumeric():
        jsonStep["bottomServoAngle"] = int(map_range(int(val)))
        oldBaseAngle = val
    else:
        jsonStep["bottomServoAngle"] = oldBaseAngle
        if oldDetachBase == 1:
            jsonStep["detachBase"] = 0
            oldDetachBase = 0
        else:
            jsonStep["detachBase"] = 1
            oldDetachBase = 1
    val = (input("Top Servo angle: "))
    if val.isnumeric():
        jsonStep["topServoAngle"] = int(map_range((int(val))))
        oldTopAngle = val
    else:
        jsonStep["topServoAngle"] = oldTopAngle
        if oldDetachTop == 1:
            jsonStep["detachTop"] = 0
            oldDetachTop = 0
        else:
            jsonStep["detachTop"] = 1
            oldDetachTop = 1
def Mode1(client_socket, jsonStep):
    global oldDetachBase
    global oldBaseAngle
    global oldDetachTop
    global oldTopAngle
    global Handshake
    global iter_var
    if Handshake == 0:
        client_socket.sendall("1\n".encode('utf-8')) # Declaring OTA mode
        Handshake = 1
        time.sleep(0.5)
    if iter_var==1:
        time.sleep(2)
    test_pointsX = numpy.linspace(100,500,num=200)
    test_pointsY = [0]*len(test_pointsX)
    iksol = invKin(test_pointsX[iter_var],test_pointsY[iter_var])
    jsonStep["topServoAngle"] = iksol[1]
    jsonStep["bottomServoAngle"] = iksol[0]
    jsonStep["iter"] = iter_var
    if(iter_var<len(test_pointsX)-1):
        iter_var+=1
        iter_var = iter_var%len(test_pointsX)
def Mode2(client_socket, jsonStep):
    global oldDetachBase
    global oldBaseAngle
    global oldDetachTop
    global oldTopAngle
    global Handshake
    global iter_var
    if Handshake == 0:
        client_socket.sendall("1\n".encode('utf-8')) # Declaring OTA mode
        Handshake = 1
        time.sleep(0.5)
    if iter_var==1:
        time.sleep(2)
    test_pointsY = numpy.linspace(-150,500,num=300)
    test_pointsX = [350]*len(test_pointsY)
    iksol = invKin(test_pointsX[iter_var],test_pointsY[iter_var])
    jsonStep["topServoAngle"] = iksol[1]
    jsonStep["bottomServoAngle"] = iksol[0]
    jsonStep["iter"] = iter_var
    if(iter_var<len(test_pointsX)-1):
        iter_var+=1
        iter_var = iter_var%len(test_pointsX)
def Mode3(client_socket, jsonStep):
    global Handshake
    if Handshake==0:
        client_socket.sendall("1\n".encode('utf-8')) # Declaring OTA mode
        Handshake = 1
        time.sleep(0.5)
    valX = float(input("X axis input: "))
    valY = float(input("Y axis input: "))
    iksol = invKin(valX,valY)
    # print(iksol)
    jsonStep["topServoAngle"] = iksol[1]
    jsonStep["bottomServoAngle"] = iksol[0]
def Mode4(client_socket, jsonStep, pathX, pathY):
    global Handshake
    global iter_var
    global serverPower
    if iter_var<=len(pathX)-1:
        if Handshake==0:
            client_socket.sendall("0\n".encode('utf-8')) # Declaring Offline mode
            Handshake = 1
            time.sleep(0.5)
        iksol = invKin(pathX[iter_var], pathY[iter_var])
        jsonStep["topServoAngle"] = iksol[1]
        jsonStep["bottomServoAngle"] = iksol[0]
        jsonStep["iter"] = iter_var
        jsonStep["total"] = len(pathX)-1
        iter_var+=1
    else:
        print("Finished sending all path points")
        serverPower = 0
    
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 2023


server.bind((host, port))
server.listen(1)
client_socket = None
client_address = None


connect()

try:
    while True:
        try:
            match mode:
                case 0:
                    Mode0(client_socket, jsonStep)
                case 1:
                    Mode1(client_socket, jsonStep)
                case 2:
                    Mode2(client_socket, jsonStep)
                case 3:
                    Mode3(client_socket, jsonStep)
                case 4:
                    Mode4(client_socket, jsonStep, pathX, pathY)
            
                
            if serverPower: 
                json_string = json.dumps(jsonStep) + "\n"
                client_socket.sendall(json_string.encode("utf-8"))
                print(f'Sending {json_string}')
                time.sleep(0.01)
            else:
                time.sleep(5)
                print("Server shutting down.")
                if client_socket:
                    client_socket.close()
                server.close()
                sys.exit()
        except(socket.timeout, BrokenPipeError, ConnectionResetError):
            print("Client disconnected.")
            Handshake = 0
            print("Handshake event reset")
            client_socket.close()
            connect()
except KeyboardInterrupt:
    print("Server shutting down.")
finally: 
    if client_socket:
        client_socket.close()
    server.close()
