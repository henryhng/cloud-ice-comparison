import xarray as xr
import matplotlib.pyplot as plt


ds_am3 = xr.open_dataset('GFDL_am3_cli_2009_01.nc')
ds_am4 = xr.open_dataset('GFDL_am4_cli_2009_01.nc')


ds_am3 = ds_am3.rename({'plevDim': 'plev', 'latDim': 'lat', 'lonDim': 'lon'})
ds_am4 = ds_am4.rename({'plevDim': 'plev', 'latDim': 'lat', 'lonDim': 'lon'})


ds_am3 = ds_am3.assign_coords(plev=ds_am3['plev'].values)
ds_am4 = ds_am4.assign_coords(plev=ds_am4['plev'].values)


pressure_levels = [150, 600, 900]


# computing differences as a simple subtraction operation between 2 values
diff_cli = ds_am3.cli - ds_am4.cli


# subplots, 1 row 3 columns for each pressure level
fig, axs = plt.subplots(1, 3, figsize=(22, 6))


for ax, p in zip(axs, pressure_levels):
   diff_slice = diff_cli.sel(plev=p, method='nearest')
  
   mesh = ax.pcolormesh(ds_am3.lon, ds_am3.lat, diff_slice,
                        shading='auto', cmap='bwr')
   ax.set_title(f'Difference (AM3 - AM4) at {p} hPa')
   ax.set_xlabel('Longitude')
   ax.set_ylabel('Latitude')
   fig.colorbar(mesh, ax=ax, orientation='vertical', label='cli difference (units)')


plt.tight_layout()
plt.show()
