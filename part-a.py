# Latitude v. Longitude Maps at Different Altitudes

# xarray is a library to analyze datasets using visualization tools
import xarray as xr
import matplotlib.pyplot as plt


# open dataset
ds = xr.open_dataset('GFDL_am3_cli_2009_01.nc')


# rename for ease of use
ds = ds.rename({'plevDim': 'plev'})


# assign pressure vals -> coordinate for 'plev'
ds = ds.assign_coords(plev=ds['plev'].values)


# pressure thresholds
pressure_levels = [150, 600, 900]


fig, axs = plt.subplots(1, 3, figsize=(22, 6))


for ax, p in zip(axs, pressure_levels):
  # cli data selected at closest pressure level even if an exact match is not found
  cli_slice = ds.cli.sel(plev=p, method='nearest')
 
  # Scale the data to match 1e-5 units
  cli_slice_scaled = cli_slice * 1e5


  # pcolormesh plot using longitude and latitude vars.
  mesh = ax.pcolormesh(ds.lon, ds.lat, cli_slice_scaled, shading='auto', cmap='viridis')
  ax.set_title(f'cli at {p} hPa')
  ax.set_xlabel('Longitude')
  ax.set_ylabel('Latitude')
  plt.colorbar(mesh, ax=ax, orientation='vertical', label='cli (x1e-5 units)')


plt.tight_layout()
plt.show()