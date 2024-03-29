# Bluemath Toolkit

Module collection for custom climate data analysis.

The main objective with this python package is to make available a set of
statististical custom tools, focused around climate data statistical classification
and prediction.

A set of climate data processing utils is also provided with the package. 

To ease understanding how to use these modules, simple demonstration scripts
and required data have been added to this repository.


## Main contents

- [extremes](./bluemathtk/extremes.py) Data Extremes Statistics
    - fit\_gev\_kma\_frechet 
    - smooth\_gev\_shape
    - acov
    - peaks\_over\_threshold
- [kma](./bluemathtk/kma.py) KMeans Classification and bmus utils
    - persistences 
    - cluster\_probabilities
    - change\_probabilities
    - sort\_cluster\_gen\_corr\_end
    - kma\_simple
    - kma\_regression\_guided
    - simple\_multivariate\_regression\_model
- [mda](./bluemathtk/mda.py) MaxDiss Classification library
    - normalize 
    - denormalize 
    - normalized\_distance
    - nearest\_indexes
    - maxdiss\_simplified\_no\_threshold
- [mjo](./bluemathtk/mjo.py) Madden-Julian Oscillation library 
    - categories 
    - phases 
- [rbf](./bluemathtk/rbf.py) Radial Basis Function library
    - rbfphi\_linear 
    - rbfphi\_cubic 
    - rbfphi\_gaussian 
    - rbfphi\_multiquadratic 
    - rbfphi\_thinplate 
    - rbf\_asemble 
    - cost\_eps 
    - rbf\_coefficient 
    - rbf\_interpolation 
    - rbf\_reconstruction 
    - rbf\_validation 
- [statistical](./bluemathtk/statistical.py) kernel CDFs, ICDFs and copula simulation
    - ksdensity\_cdf 
    - ksdensity\_icdf 
    - generalizedpareto\_cdf 
    - generalizedpareto\_icdf 
    - empirical\_cdf 
    - empirical\_icdf 
    - copulafit
    - copularnd
    - copula\_simulation
    - runmean 


## Documentation


## Install
- - -

The source code is currently hosted on GitLab at: https://gitlab.com/geoocean/bluemath/bluemathtk

### Install from sources

Install requirements. Navigate to the base root of [bluemathtk](./) and execute:

```
   pip install -r requirements/requirements.txt
```

Then install bluemathtk:

```
   python setup.py install
```

## Examples:
- - -

- [bmus series](./demos/demo_bmus_series.py) some bmus series tools
- [GEV extremes](./demos/demo_extremes_gev.py) GEV extremes distribution tools for cluster data 
- [POT extremes](./demos/demo_extremes_pot.py) peaks over threshold methodology
- [KMeans Classification](./demos/demo_kma.py) KMA classification por PCA and climate data 
- [MaxDiss Classification](./demos/demo_mda.py) MDA classification climate data 
- [Madden-Julian Oscillation](./demos/demo_mjo.py) MJO categories and phases calculation
- [Radial Basis Functions](./demos/demo_rbf.py) RBF Reconstruction and Kfold validation 
- [Copula Simulation](./demos/demo_copula_simulation.py) Statistical variables simulation  


## Contributors:


## Thanks also to:


## License

This project is licensed under the MIT License - see the [license](./LICENSE.txt) file for details

