import matplotlib.pyplot as plt
import numpy as np
import math as m
import matplotlib as mpl
# Need this for the colorbars we will make on the mirrored plot
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Set up a pyplot figure 
fig, (ax) = plt.subplots(nrows=1, ncols=1,  figsize=(5.0,3.8), sharex = True)



cc = ('#000000', '#3f2819', '#7e5033', '#9d643f', '#bd784c', '#dc8b59', '#fc9f65', '#ffc77f')


   
def col2(cc):
	return plt.cm.copper((11-cc)/22) 
	
	

mk = ['^', 'o', 'x']

ang0 = np.array([-15, -10, -5, -2.5, 0, 2.5, 5, 10]) 
ab0 = [1.08, 1.07, 1.13, 1.18, 1.20, 1.26, 1.36, 1.63] 
bc0 = [1.31, 1.39, 1.39, 1.36, 1.48, 1.52, 1.63, 1.83]  
 
 
abi = [0.91, 1.0, 1.1, 1.2, 1.3, 1.4] 
abf = [1.11, 1.2, 1.25, 1.35, 1.45, 1.51]   
 

bci = [0.91, 1.0, 1.1, 1.2, 1.3, 1.4] 
bcf = [1.83, 1.71, 1.68, 1.65, 1.61, 1.55]  
 


print ((15-ang0)/30)

for i in range(6):
	ax.errorbar(abi[i], abf[i], yerr = 0.07, marker = 'o', markersize = 4.8, c = 'k', linestyle = '' )
	
	ax.errorbar(bci[i], bcf[i], yerr = 0.07, marker = 'o', markersize = 4.8, c = 'k', mfc='w', linestyle = '' )
	

ax.errorbar(0, 0, xerr = 0.08, yerr = 0.07, marker = 'o', markersize = 4.8, c = 'k', linestyle = '', label = r'a/b')
ax.errorbar(0, 0, xerr = 0.08, yerr = 0.07, marker = 'o', markersize = 4.8, c = 'k', linestyle = '', mfc='w', label = r'a/c')

	
ax.set_xlim([0.8, 1.5])
ax.set_ylim([1.0, 2.0])
#ax.axis('equal')


# Label titles
ax.set_xlabel(r'Initial axes ratio')
ax.set_ylabel(r'Final axes ratio')	
	
	
#ax.set_ylabel(r'$m_b/\sum M_b$')

ax.grid(linestyle = '--', linewidth = 0.5)

#ax.set_ylabel(r'$M_b (v>v_{esc})$ [$\times 10^5$ kg]')

legend = ax.legend(loc = 4, fontsize = 10., frameon=True, handletextpad=0.1)
legend.get_frame().set_linewidth(0)

#ax.annotate('A', xy=(0.84, 1.98), annotation_clip=False, fontsize = 20)

#Save figure
fig.tight_layout() 
plt.savefig('Plots_output/nonsph.pdf', bbox_inches='tight', dpi=350)
