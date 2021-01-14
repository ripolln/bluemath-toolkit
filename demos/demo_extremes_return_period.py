
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

from bluemathtk.extremes import return_period


# data
p_data = op.abspath(op.join(op.dirname(__file__), '..', 'data'))
p_waves = op.join(p_data, 'waves_historical.nc')

# load demo waves dataset
waves = xr.open_dataset(p_waves)

# calculate Hs annual maxima
def grouped_max(ds, vn=None, dim=None):
    return ds.isel(**{dim: ds[vn].argmax(dim)})

waves_amax = waves.groupby('time.year').apply(grouped_max, vn='Hs', dim='time')

# calculate Hs annual maxima return period
hs_amax = waves_amax['Hs']

hs_rp = return_period(hs_amax)

print("\n Return Period")
print(hs_rp)

