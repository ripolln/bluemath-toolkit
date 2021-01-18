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

from bluemathtk.statistical import copula_simulation


# data
p_data = op.abspath(op.join(op.dirname(__file__), '..', 'data'))
p_waves = op.join(p_data, 'waves_historical.nc')

# load demo waves dataset
dataset = xr.open_dataset(p_waves)
dataset = dataset.isel(time = slice(0,10000))

# variables to use
vns = ['Hs', 'Tp']
dataset = dataset[vns].to_dataframe()[1:]  # remove nans from data

print('\n dataset')
print(dataset)


# kernels to use in copula simulation 
kernels = ['KDE', 'ECDF']  # one kernel for each variable
num_sims = 50000  # number of samples to generate

# copula simulation 
out = copula_simulation(dataset[vns].values[:], kernels, num_sims)
simulation = pd.DataFrame(data=out, columns=vns)

print('\n simulation')
print(simulation)

