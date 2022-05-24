import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
from spatialmath import SE3
# link lenths in mm
a1 = float(input("a1 = ")) # 50
a2 = float(input("a2 = ")) # 60
a3 = float(input("a3 = ")) # 50
a4 = float(input("a4 = ")) # 60
a5 = float(input("a5 = ")) # 50

# link mm to meters converter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)
a4 = mm_to_meter(a4)
a5 = mm_to_meter(a5)

# link limits converted to meters
lm3 = float(input("lm3 = ")) # 50
lm3 = mm_to_meter(lm3) #50         50, for testing

# Create Links
SCARA_Standard = DHRobot([
    RevoluteDH(a1,0,(0/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    PrismaticDH(0,a2,0,0,qlim=[0,0]),
    RevoluteDH(a3,0,(180/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    PrismaticDH(0,a4,0,0,qlim=[0,0]),
    PrismaticDH(0,0,0,a5,qlim=[0,lm3])
], name='SCARA_St')

print(SCARA_Standard)

# degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi


# q Paths
#for SCARA Standard Joint Variables =([ T1, 0, T2, 0, d3])
q0 = np.array([0,0,0,0,0])
q1 = np.array([ deg_to_rad(float(input("T1 = "))),0,          # 90 ,for testing
                deg_to_rad(float(input("T2 = "))),0,          # 270,for testing
                mm_to_meter(float(input("d3 = "))) #1st path  # 120,for testing
                ])
#q2 = np.array([ deg_to_rad(float(input("T1 = "))),0,
  #              deg_to_rad(float(input("T2 = "))),0,
  #              mm_to_meter(float(input("d3 = "))) #2nd path
  #              ])
#q3 = np.array([ deg_to_rad(float(input("T1 = "))),0,
   #             deg_to_rad(float(input("T2 = "))),0,
   #             mm_to_meter(float(input("d3 = "))) #3rd path
   #             ])                
#Trajectory command
traj1 = rtb.jtraj(q0,q1,10)#time vector or steps
print(traj1)
print(traj1.q)

#traj2 = rtb.jtraj(q1,q2,10)
#print(traj2)
#print(traj2.q)

#traj3 = rtb.jtraj(q2,q3,10)
#print(traj3)
#print(traj3.q)


#plot scale
x1 = -0.1
x2 = 0.1
y1 = -0.1
y2 = 0.1
z1 = -0.1
z2 = 0.1



# for Joint Variable vs Time(S) Table
rtb.qplot (traj1.q)
#rtb.qplot (traj2.q)
#rtb.qplot (traj3.q)

SCARA_Standard.plot(traj1.q,limits = [x1, x2, y1, y2, z1, z2])
#SCARA_Standard.plot(traj2.q,limits = [x1, x2, y1, y2, z1, z2])
#SCARA_Standard.plot(traj3.q,limits = [x1, x2, y1, y2, z1, z2])

#Plot Command
SCARA_Standard.teach(jointlabels=1) #for teach50