#!/usr/bin/env python
# -*- coding: utf-8 -*-

# common
import os
import os.path as op

# pip
import xarray as xr

# bluemath toolkit library
import sys
sys.path.insert(0, op.join(op.dirname(__file__), '..' ))

from bluemathtk.mjo import categories
from bluemathtk.mjo import phases


# data
p_data = op.abspath(op.join(op.dirname(__file__), '..', 'data'))
p_mjo = op.join(p_data, 'mjo_historical.nc')

# load MJO 
mjo_hist = xr.open_dataset(p_mjo)


# get MJO categories (1-25) 
rmm1 = mjo_hist['rmm1']
rmm2 = mjo_hist['rmm2']
phase = mjo_hist['phase']

categ, d_rmm_categ = categories(rmm1, rmm2, phase)
mjo_hist['category'] = (('time',), categ)

print('\n MJO with categories simulation')
print(mjo_hist)


# get MJO phases
ph, dgr = phases(rmm1, rmm2)

print('\n MJO calculated phases (and degrees)')
out = xr.Dataset(
    {
        'phase' : (('time', ), ph),
        'angle' : (('time', ), dgr),
    },
    coords = {'time' : mjo_hist.time},
)
print(out)

