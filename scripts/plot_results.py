#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: Keivan Zavari
"""

# imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as fig

import rospkg 


# get an instance of RosPack with the default search paths
rospack = rospkg.RosPack()
# get the folder path for the package where the measurement report is
folder_name = rospack.get_path('performance_tests')

files = ['subscriber_cpp_from_cpp_publisher',
'subscriber_cpp_from_py_publisher',
'subscriber_py_from_cpp_publisher',
'subscriber_py_from_py_publisher']

data = []
# The complete absolute path to the file
for i in range(len(files)):
    file_path = folder_name + '/data_saved/' + files[i] + '.txt'
    data.append(np.loadtxt(file_path))


# ----------------------------------------------------------------------
# From here on should be automatic
# ----------------------------------------------------------------------


# -------------------------
## Plot the data
# -------------------------
plt.close('all')

# plt.figure('Loop period at subscriber vs test number')
# plt.grid(True)
# plt.hold(True)
clr_sensor = [(0.1,0.0,0.8), (0.6,0.1,0.6), (0.8,0.0,0.1), (0.8,0.0,0.1)]
clr_mk_sensor = [(0.1,0.9,0.9), (0.9,0,0), (0.2,0.2,0.2), (0.2,0.2,0.2)]
line_width = 1.0




f, ax = plt.subplots(2,2,sharex=True)
f.suptitle('Loop period (50 Hz) at subscriber vs test number')

i=0
j=0
ax[i,j].plot( range(len(data[i])),data[i], 'r-')
ax[i,j].set_ylabel(files[i*2+j])
# ax[i,j].axis([0,500,0.0195,0.0205])

i=0
j=1
ax[i,j].plot( range(len(data[i])),data[i], 'k-')
ax[i,j].set_ylabel(files[i*2+j])
# ax[i,j].axis([0,500,0.0195,0.0205])

i=1
j=0
ax[i,j].plot( range(len(data[i])),data[i], 'b-')
ax[i,j].set_ylabel(files[i*2 + j])
# ax[i,j].axis([0,500,0.0195,0.0205])


i=1
j=1
ax[i,j].plot( range(len(data[i])),data[i], 'g-')
ax[i,j].set_ylabel(files[i*2+j])
# ax[i,j].axis([0,500,0.0195,0.0205])



plt.show()

