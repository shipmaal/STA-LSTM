import xarray as xr
import pandas as pd

filepath = '/home/shipmaal/SWOT-ML/MissouriUpstream.nc'

with xr.open_dataset(filepath, group='Reach_Timeseries') as ds:
    print(ds.variables)
    width = ds.W
    discharge = ds.H
    flow_area = ds.P
    surface_elevation = ds.S
    surface_slop = ds.A


print(width.values)
