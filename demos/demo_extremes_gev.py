#!/usr/bin/env python
# -*- coding: utf-8 -*-

# common
import os
import os.path as op

# pip
import pandas as pd
import xarray as xr
import numpy as np
from scipy.stats import genextreme

# bluemath toolkit library
import sys
sys.path.insert(0, op.join(op.dirname(__file__), '..' ))

from bluemathtk.extremes import fit_gev_kma_frechet
from bluemathtk.extremes import smooth_gev_shape
from bluemathtk.extremes import acov


# data
p_data = op.abspath(op.join(op.dirname(__file__), '..', 'data'))
p_waves = op.join(p_data, 'waves_historical.nc')
p_kma = op.join(p_data, 'kma.nc')

# load demo waves dataset and kma bmus series
waves = xr.open_dataset(p_waves)
kma = xr.open_dataset(p_kma)

# waves and kma data must be same length
waves = waves.sel(time=slice(kma.time[0], kma.time[-1]))



## fit Hs series and KMA bmus data to GEV distributions
# for this demonstration we will fit the entire Hs dataset to GEV distributions 
# one GEV distribution for each detected KMA cluster

bmus = kma['bmus'].values[:]
hs = waves['Hs'].values[:]

gev_params = fit_gev_kma_frechet(bmus, hs)

# print GEV parameters for each cluster
print('\n GEV parameters (shape, location, scale)')
for k in gev_params.keys():
    print(k, gev_params[k])

# if needed, parse output from dictionary to numpy array 
np_gev_params = np.row_stack([gev_params[k] for k in sorted(gev_params.keys())])



## smooth GEV shape parameters for each KMA cluster, by promediation with neighbour EOFs
cenEOFs = kma.cenEOFs.values[:]
gev_shape = np_gev_params[:, 0]

gev_shape_smoothed = smooth_gev_shape(cenEOFs, gev_shape)
print('\n GEV shape smoothed')
print(gev_shape_smoothed)



## calculate asyntotic variance matrix (Fisher Information matrix inverse)

# select one example cluster
c_id = 6
ix = np.where((bmus==c_id))[0]

hs_c = hs[ix]
theta = gev_params[c_id]

ac = acov(genextreme.nnlf, theta, hs_c)
print('\n ACOV')
print(ac)

