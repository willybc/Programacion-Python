# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 02:52:36 2020

@author: WILLY
"""

import matplotlib.pyplot as plt
import numpy as np

temperaturas = np.loadtxt('../Data/Temperaturas.npy')

plt.hist(temperaturas,bins=25)
