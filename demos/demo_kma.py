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

from bluemathtk.kma import kma_simple
from bluemathtk.kma import kma_regression_guided
from bluemathtk.kma import simple_multivariate_regression_model


# data
p_data = op.abspath(op.join(op.dirname(__file__), '..', 'data'))



## Principal Components KMeans simple classification
p_pca = op.join(p_data, 'pca_sst.nc')
pca = xr.open_dataset(p_pca)

# KMeans Classification
num_clusters = 6
repres = 0.9

kma = kma_simple(pca, num_clusters, repres)
print('\n KMeans Classification:')
print(kma)



## Principal Components KMeans regression guided classification 
p_waves = op.join(p_data, 'waves_historical.nc')
p_pca = op.join(p_data, 'pca_slp.nc')

waves = xr.open_dataset(p_waves)
pca = xr.open_dataset(p_pca)

# first calculate regression model between predictand and predictor
waves = waves.sel(time=pca.pred_time)
regr_vars = ['Hs', 'Tp']

yregres = simple_multivariate_regression_model(
    pca, waves, regr_vars,
)

# now classify using KMean regression guided
num_clusters = 36
repres = 0.7
alpha = 0.36

kma = kma_regression_guided(
    pca, yregres,
    num_clusters, repres, alpha,
)

print('\n KMeans Regression Guided Classification:')
print(kma)

