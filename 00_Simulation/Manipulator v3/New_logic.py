import math
import numpy as np

l1 = 150 # Link_1 length
l2 = 92.5 # Link_2 length
Oo = 12.5 # Origin offset #U forgot to include this
Target_position = [5,5,5]
Intermediate_set = [150,100,50]
Intermediate_set[2]-=Oo
# d=0
# for i in Intermediate_set:
#     d+=i**2
# print(math.sqrt(d))

X=Intermediate_set[0]
Y=Intermediate_set[1]
Z=Intermediate_set[2]

q2_Num = X**2 + Z**2 -l1**2 - l2**2
q2_Den = 2*l1*l2
q2 = math.acos(q2_Num/q2_Den)

q1_tan_num = l2*(math.sin(q2))
q1_tan_den = l1 + l2*(math.cos(q2))
q1 = math.atan2(Z,X) - math.atan2(q1_tan_num,q1_tan_den)

q3 = math.atan2(Y,X)

Angles = [q1,q2,q3]
print(Angles)

# q1 == Revolute 2
# q2 == Revolute 3
# q3 == Revolute 1
