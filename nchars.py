#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:04:30 2020

@author: emirimorita
"""

text_nchars = []
for i in range(len(text_list[7:])):
    nchars = len(text_list[i+7])
    text_nchars.append(nchars)

text_nchars

from statistics import mean
print(mean(text_nchars))

import numpy as np
from matplotlib import pyplot as plt

# create plot
text_nchars_array = np.array(text_nchars)
plt.hist(text_nchars_array)
plt.title('Number of Characters in Top 15 Recommended Company Profiles')
plt.xlabel('Number of Characters')
plt.ylabel('Number of Companies')
plt.show()