# Cloud Ice Profiles - cli versus pressure

import xarray as xr
import matplotlib.pyplot as plt


ds = xr.open_dataset('GFDL_am3_cli_2009_01.nc')
ds = ds.rename({'plevDim': 'plev', 'latDim': 'lat', 'lonDim': 'lon'})
ds = ds.assign_coords(plev=ds.plev.values, lat=ds.lat.values, lon=ds.lon.values)


# average cli over lat & long
cli_profile = ds.cli.mean(dim=['lat', 'lon'])


# how cli changes in height vs pressure
plt.figure(figsize=(6, 8))
plt.plot(cli_profile, cli_profile.plev, marker='o')
plt.gca().invert_yaxis()  # invert
plt.xlabel('Average cli (units)')
plt.ylabel('Pressure (hPa)')
plt.title('Vertical Profile of Cloud Ice (cli)')
plt.tight_layout()
plt.show()
