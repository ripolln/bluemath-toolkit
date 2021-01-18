#!/usr/bin/env python
# -*- coding: utf-8 -*-

# common
import os
import os.path as op

# pip
import pandas as pd
import xarray as xr

# bluemath toolkit library
import sys
sys.path.insert(0, op.join(op.dirname(__file__), '..' ))

from bluemathtk.mda import maxdiss_simplified_no_threshold
from bluemathtk.rbf import rbf_reconstruction
from bluemathtk.rbf import rbf_validation


# data
p_data = op.abspath(op.join(op.dirname(__file__), '..', 'data'))
p_waves = op.join(p_data, 'waves_historical.nc')



# Use MDA to Generate a demo dataset and subset for RBF interpolation

# load demo waves dataset
dataset = xr.open_dataset(p_waves)  # > 300000 waves cases

# variables to use
vns = ['Hs', 'Tp', 'Dir']
dataset = dataset[vns].to_dataframe()[1:]  # remove nans from data

# subset size, scalar and directional indexes
n_subset = 125            # subset size
ix_scalar = [0, 1]        # hs, tp
ix_directional = [2]      # dir

# MDA algorithm
sel = maxdiss_simplified_no_threshold(
    dataset[vns].values[:], n_subset, ix_scalar, ix_directional,
    log=True,
)
subset = pd.DataFrame(data=sel, columns=vns)



# RBF statistical interpolation allows us to solve calculations to big datasets 
# that otherwise would be highly costly (time and/or computational resources)

# but for this demo we will build our interpolation target
# from a simple calculation 
subset['Fe'] = (subset.Hs**2 * subset.Tp)**(1.0/3)
subset['Tp_sq'] = subset.Tp**2 



# mount RBF subset
values_s = subset[['Hs', 'Tp']].values
ix_scalar_s = [0, 1]
ix_directional_s = []

# mount RBF dataset to interpolate
values_d = dataset[['Hs', 'Tp']].values

# mount RBF target
values_t = subset[['Fe','Tp_sq']].values
ix_scalar_t = [0, 1]
ix_directional_t = []


# RBF reconstrution
out = rbf_reconstruction(
    values_s, ix_scalar_s, ix_directional_s,
    values_t, ix_scalar_t, ix_directional_t,
    values_d,
)


print('\n RBF interpolation: output for entire dataset')
print(out)



# RBF Validation: using k-fold mean squared error methodology
test = rbf_validation(
    values_s, ix_scalar_s, ix_directional_s,
    values_t, ix_scalar_t, ix_directional_t,
    n_splits=3, shuffle=True,
)

print('\n RBF validation test')
print(test)
