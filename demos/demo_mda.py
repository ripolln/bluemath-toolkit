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


# data
p_data = op.abspath(op.join(op.dirname(__file__), '..', 'data'))
p_waves = op.join(p_data, 'waves_historical.nc')

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

print(subset)

