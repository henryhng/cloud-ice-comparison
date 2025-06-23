# plot Zonal Means on how cloud ice varies with pressure and latitude

import xarray as xr
import matplotlib.pyplot as plt


#netCDF format = a common format for climate model output.
ds = xr.open_dataset('GFDL_am3_cli_2009_01.nc')


# rename dimensions to shorter names
ds = ds.rename({'plevDim': 'plev', 'latDim': 'lat', 'lonDim': 'lon'})


# coords assigned using data; plev = pressure level, lat = latitude, lon = longitude
ds = ds.assign_coords(plev=ds.plev.values, lat=ds.lat.values, lon=ds.lon.values)


# avg cli vals for longitude
# zonal mean converts the data to a function of solely lat and plev instead of a 3d plot of lat, plev, long
# zonal mean uses an average for the longitude
cli_zonal = ds.cli.mean(dim='lon')


# plot for the zonal-mean cli, lat vs. plev
plt.figure(figsize=(8, 6))
mesh = plt.pcolormesh(cli_zonal.lat, cli_zonal.plev, cli_zonal, shading='auto', cmap='viridis')
plt.gca().invert_yaxis()  # lower pressures -> higher altitudes -> invert that to the top
plt.xlabel('Latitude')
plt.ylabel('Pressure (hPa)')
plt.title('Zonal Mean of Cloud Ice (cli)')
plt.colorbar(mesh, label='cli units')
plt.tight_layout()
plt.show()
