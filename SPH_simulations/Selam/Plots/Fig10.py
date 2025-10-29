MODULE_PATH = "~/home/raducan/home0/Python_scripts/readerxdr.py"
MODULE_NAME = "readxdr"

import matplotlib.pyplot as plt
import readxdr as xdr
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.stats import gaussian_kde
from shapely.geometry import MultiPoint
from shapely.ops import triangulate, unary_union, polygonize


# Set up a pyplot figure 
fig, (ax, ax2) = plt.subplots(nrows=1, ncols=2,  figsize=(8.0,3.4))

xdrfile = (
"runs/str/0Pa/col_5_100_1.5/dump/out013.xdr",
"runs/str/1Pa/col_5_100_1.5/dump/out013.xdr",
"runs/str/10Pa/col_5_100_1.5/dump/out013.xdr",
"runs/str/50Pa/col_5_100_1.5/dump/out013.xdr")


cc = ('#7e5033', '#bd784c', '#dc8b59',  '#ffc77f')

label_name = ('0 Pa, 1.5$v_{esc}$', '1 Pa, 1.5$v_{esc}$', '10 Pa, 1.5$v_{esc}$', '50 Pa, 1.5$v_{esc}$')

for i in range(4):
	targetdata = xdr.read_xdr(xdrfile[i])

	print(f"title: {targetdata['title']}")
	print(f"Number of particles: {targetdata['numpart']}")
	print(f"time: {targetdata['time']}")
	print(f"stored variables: {targetdata['varnames']}")

	dat = targetdata['data']

	mass = dat['mass']
	strain = dat['strain']

	vel = (dat['vx']**2+dat['vy']**2+dat['vz']**2)**0.5

	mass, strain, vel = mass[vel<1e3], strain[vel<1e3], vel[vel<1e3]


	#####
	ind = np.argsort(strain)[::-1]
	pt = mass[ind]
	ejp = pt.cumsum()
	


	ax.plot(strain[ind], ejp/(np.sum(mass)), linestyle = '-', marker = '', color= cc[i], 	label = label_name[i])
	###

#####################
#####################

xdrfile = (
"runs/str/0Pa/col_5_100_1.5/dump/out013.xdr",
"runs/str/1Pa/col_5_100_1.75/dump/out013.xdr",
"runs/str/10Pa/col_5_100_2.0/dump/out013.xdr",
"runs/str/50Pa/col_5_100_2.5/dump/out013.xdr")

label_name = ('0 Pa, 1.5$v_{esc}$', '1 Pa, 1.75$v_{esc}$', '10 Pa, 2.0$v_{esc}$', '50 Pa, 2.5$v_{esc}$')

for i in range(4):
	targetdata = xdr.read_xdr(xdrfile[i])



	print(f"title: {targetdata['title']}")
	print(f"Number of particles: {targetdata['numpart']}")
	print(f"time: {targetdata['time']}")
	print(f"stored variables: {targetdata['varnames']}")

	dat = targetdata['data']


	mass = dat['mass']
	strain = dat['strain']


	vel = (dat['vx']**2+dat['vy']**2+dat['vz']**2)**0.5


	mass, strain, vel = mass[vel<1e3], strain[vel<1e3], vel[vel<1e3]


	#####
	ind = np.argsort(strain)[::-1]
	pt = mass[ind]
	ejp = pt.cumsum()
	

	ax2.plot(strain[ind], ejp/(np.sum(mass)), linestyle = '-', marker = '', color= cc[i], 	label = label_name[i])
	###



ax.set_ylim([1e-3, 1.8])
ax2.set_ylim([1e-3, 1.8])

ax.set_xlim([4e-3,10])
ax2.set_xlim([4e-3,10])
#ax.axis('equal')

ax.annotate(r'a', xy=(1e-3, 1.8), annotation_clip=False, fontsize = 14, weight='bold')
ax2.annotate(r'b', xy=(1e-3, 1.8), annotation_clip=False, fontsize = 14, weight='bold')


# Make axes log 
ax.set_xscale('log')
ax.set_yscale('log')

ax2.set_xscale('log')
ax2.set_yscale('log')

# Set axis labels 
ax.set_ylabel('Cum. mass, $m(>\epsilon)/\sum m$')
ax.set_xlabel('Strain, $\epsilon$')

ax2.set_ylabel('Cum. mass, $m(>\epsilon)/\sum(m)$')
ax2.set_xlabel('Strain, $\epsilon$')

#Save figure
# Apply tight layout
fig.tight_layout()

# Plot legend
ax.legend(loc = 'best', fontsize = 9.)
ax.grid(linestyle = '--', linewidth = 0.5)

ax2.legend(loc = 'best', fontsize = 9.)
ax2.grid(linestyle = '--', linewidth = 0.5)
	
# Here specify where the fig should be save. 
# This can be replaced by a variable
plt.savefig('Plots_output/strain_cohesion.png', bbox_inches='tight', dpi = 450)

#Close plot
plt.close(fig)

