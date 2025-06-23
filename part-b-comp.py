import xarray as xr
import matplotlib.pyplot as plt


ds_am3 = xr.open_dataset('GFDL_am3_cli_2009_01.nc')
ds_am4 = xr.open_dataset('GFDL_am4_cli_2009_01.nc')


ds_am3 = ds_am3.rename({'plevDim': 'plev', 'latDim': 'lat', 'lonDim': 'lon'})
ds_am4 = ds_am4.rename({'plevDim': 'plev', 'latDim': 'lat', 'lonDim': 'lon'})


ds_am3 = ds_am3.assign_coords(plev=ds_am3.plev.values, lat=ds_am3.lat.values, lon=ds_am3.lon.values)
ds_am4 = ds_am4.assign_coords(plev=ds_am4.plev.values, lat=ds_am4.lat.values, lon=ds_am4.lon.values)


# zonal (longitude) mean for each dataset
cli_zonal_am3 = ds_am3.cli.mean(dim='lon')
cli_zonal_am4 = ds_am4.cli.mean(dim='lon')


# diff in zonal means(AM3 minus AM4)
diff_zonal = cli_zonal_am3 - cli_zonal_am4


# lat vs. plev plot
plt.figure(figsize=(8, 6))
mesh = plt.pcolormesh(diff_zonal.lat, diff_zonal.plev, diff_zonal,
                       shading='auto', cmap='bwr')
plt.gca().invert_yaxis() 
plt.xlabel('Latitude')
plt.ylabel('Pressure (hPa)')
plt.title('Difference in Zonal Mean Cloud Ice (AM3 - AM4)')
plt.colorbar(mesh, label='cli difference (units)')
plt.tight_layout()
plt.show()
