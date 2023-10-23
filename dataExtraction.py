import numpy as np
import xarray as xr

filepath = '/home/shipmaal/SWOT-ML/MissouriUpstream.nc' # replace with filepath of the data file

with xr.open_dataset(filepath, group='Reach_Timeseries') as ds:
    width = np.array(ds.W)
    discharge = np.array(ds.Q)
    average_area = np.array(ds.A)
    surface_elevation = np.array(ds.H)
    surface_slop = np.array(ds.S)

dataset = np.stack((width, discharge, average_area, surface_elevation, surface_slop), axis=1)

print(dataset)
print(dataset.shape)
