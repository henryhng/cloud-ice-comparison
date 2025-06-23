import xarray as xr
import matplotlib.pyplot as plt


ds_am3 = xr.open_dataset('GFDL_am3_cli_2009_01.nc')
ds_am4 = xr.open_dataset('GFDL_am4_cli_2009_01.nc')


ds_am3 = ds_am3.rename({'plevDim': 'plev', 'latDim': 'lat', 'lonDim': 'lon'})
ds_am4 = ds_am4.rename({'plevDim': 'plev', 'latDim': 'lat', 'lonDim': 'lon'})


ds_am3 = ds_am3.assign_coords(plev=ds_am3.plev.values, lat=ds_am3.lat.values, lon=ds_am3.lon.values)
ds_am4 = ds_am4.assign_coords(plev=ds_am4.plev.values, lat=ds_am4.lat.values, lon=ds_am4.lon.values)


# avg cli over lat and long
cli_profile_am3 = ds_am3.cli.mean(dim=['lat', 'lon'])
cli_profile_am4 = ds_am4.cli.mean(dim=['lat', 'lon'])


# diff. between two datsets (AM3 - AM4)
diff_profile = cli_profile_am3 - cli_profile_am4


# cli vs. pressure
plt.figure(figsize=(6, 8))
plt.plot(diff_profile, diff_profile.plev, marker='o', label='AM3 - AM4')
plt.gca().invert_yaxis() 
plt.xlabel('cli Difference (units)')
plt.ylabel('Pressure (hPa)')
plt.title('Vertical Profile Difference of Cloud Ice (cli)')
plt.legend()
plt.tight_layout()
plt.show()
