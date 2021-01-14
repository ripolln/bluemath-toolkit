#!/usr/bin/env python
# -*- coding: utf-8 -*-

# common
import os
import os.path as op

# pip
import xarray as xr
import numpy as np

# bluemath toolkit library
import sys
sys.path.insert(0, op.join(op.dirname(__file__), '..' ))

from bluemathtk.kma import persistences
from bluemathtk.kma import cluster_probabilities
from bluemathtk.kma import change_probabilities


# data
p_data = op.abspath(op.join(op.dirname(__file__), '..', 'data'))
p_kma = op.join(p_data, 'kma.nc')

# load kma bmus series
kma = xr.open_dataset(p_kma)
bmus = kma['bmus'].values[:]
set_clusters = np.unique(bmus)


# calculate bmus persistences for each cluster
d_pers = persistences(bmus)

print('\n cluster series persistences')
for k in d_pers.keys(): print(k, d_pers[k])


# calculate bmus probabilities 
cl_probs = cluster_probabilities(bmus, set_clusters)
print('\n cluster series probabilities')
print(cl_probs)

# calculate change counts and probabilities for each cluster
ch_counts, ch_probs = change_probabilities(bmus, set_clusters)
print('\n cluster series change probabilities')
print(ch_probs)

