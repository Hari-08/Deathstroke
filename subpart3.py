import pybullet as p
import pybullet_data
import time
import os
physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-10)
sub3StartPos = [2,2,1]
dabbaStartPos = [0,0,1]
sub3StartOrientation = p.getQuaternionFromEuler([0,0,0])
dabbaStartOrientation = p.getQuaternionFromEuler([0,0,0])
sub3Id = p.loadURDF("sub3.urdf",sub3StartPos, sub3StartOrientation)
dabbaId = p.loadURDF("dabba.urdf",dabbaStartPos, dabbaStartOrientation)
for i in range (10000):
    p.stepSimulation()
    p.setGravity(0.707*981*i,0.707*981*i,-10)
    time.sleep(1./24.)
sub3Pos, sub3Orn = p.getBasePositionAndOrientation(sub3Id)
dabbaPos, dabbaOrn = p.getBasePositionAndOrientation(dabbaId)
print(sub3Pos,sub3Orn)
print(sub3Pos,sub3Orn)
p.disconnect()