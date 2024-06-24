# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:57:36 2024

@author: tcolomb
"""

from pyKoalaRemote import client
import numpy as np
import matplotlib.pyplot as plt

stack_range_cm = 10
stack_step_cm = 1
totalNumberOfDistances = 50


#create instance to class pyRemote
remote = client.pyKoalaRemoteClient()
#Connect and Login
remote.Connect("localhost")
remote.Login("admin")

#remote.OpenConfig(140)

remote.LoadHolo(r'C:\Users\tcolomb\Documents\Projects\pykoalaremote\example\data\holo.tiff',1)
remote.OpenHoloWin()
remote.OpenIntensityWin()
remote.OpenPhaseWin()

actual_distance = remote.GetRecDistCM()

distCM_Min = actual_distance-stack_range_cm/2
distCM_Max = actual_distance+stack_range_cm/2
distCM_step = stack_step_cm
savePath = r'C:\tmp_remote_test'
## In place of None you can give a number of steps to define the stack between minimal and maximal value
d_stack = remote.SaveStackRecDistCM(distCM_Min, distCM_Max, distCM_step, savePath, totalNumberOfDistances = totalNumberOfDistances)
print(d_stack)
Stacks = remote.GetStackRecDistCM(distCM_Min, distCM_Max, distCM_step, totalNumberOfDistances = totalNumberOfDistances)
IntensityLambda1Stack = Stacks[0]
PhaseLambda1Stack = Stacks[1]
d_stack = Stacks[6]
print(d_stack)

WavefrontStacks = IntensityLambda1Stack*np.exp(1j*PhaseLambda1Stack)

plt.figure()
plt.imshow(np.real(WavefrontStacks[:,:,4]))

remote.Logout()