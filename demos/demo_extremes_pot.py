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

from bluemathtk.extremes import peaks_over_threshold


# data
p_data = op.abspath(op.join(op.dirname(__file__), '..', 'data'))
p_waves = op.join(p_data, 'waves_historical.nc')

# load demo waves dataset
waves = xr.open_dataset(p_waves)

hs_pot = peaks_over_threshold(waves, 'Hs', 99)
print('\n Peaks Over Threshold')
print(hs_pot)

