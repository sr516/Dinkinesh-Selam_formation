import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.optimize import curve_fit

# Set up a pyplot figure 
fig, (ax1, ax) = plt.subplots(nrows=1, ncols=2,  figsize=(8.5,4.0))

cc = ('#000000', '#3f2819', '#7e5033', '#9d643f', '#bd784c', '#dc8b59', '#fc9f65', '#ffc77f')

# Bi-lobe
vel = np.array([0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75])
ang = np.array([-75, -60, -45, -30, 0, 30, 45, 60, 75])


vel1 = np.array([1, 1, 1, 1, 1, 1])
ang1 = np.array([-75, -60, -45, 45, 60, 75])

vel2 = np.array([1.25, 1.25, 1.25, 1.25, 1.5])
ang2 = np.array([-75, -60, -45, 45, -75])


ax.plot(ang, vel, 's', color = cc[0], markersize = 12., label = 'Mergerging, bi-lobe')
ax.plot(ang1, vel1, 's', color = cc[0], markersize = 12.)	
ax.plot(ang2, vel2, 's', color = cc[0], markersize = 12.)	

vel = np.array([2, 2, 2, 2, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
ang = np.array([-45, -30, 0, 30, -60, -45, -30, 0, 30, 45])

vel2 = np.array([1.25, 1.25, 1.25, 1.0, 1.0, 1.0])
ang2 = np.array([-30, 0, 30, -30, 0, 30])

ax.plot(ang, vel, 's', color = cc[3], markersize = 12., label = 'Merging')
ax.plot(ang2, vel2, 's', color = cc[3], markersize = 12.)

vel = np.array([1.25, 1.25, 1.5, 1.5, 2, 2, 2, 2, 2])
ang = np.array([75, 60, 60, 75, 45, 60, 75, -75, -60])

ax.plot(ang, vel, 's', color = cc[6], markersize = 12., label = 'Non-merging')
	
	
vel = np.array([2.5, 2, 1.5, 1.25, 1.15, 1.00])
ang = np.array([30, 35, 51, 54, 80, 85])
	
coeff = np.polyfit(ang, vel, deg = 2)

# Polynomial Function
p2 = lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2]

# Points to evaluate
xp = np.linspace(min(ang), max(ang), 10)

# Plotting result
#plt.plot(xp, p2(xp), color='k', linestyle = '--')



###

vel = np.array([1.6, 1.9, 2.0, 2.5 ])
ang = np.array([-80, -65, -45, -40 ])
	
coeff = np.polyfit(ang, vel, deg = 2)

# Polynomial Function
p2 = lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2]

# Points to evaluate
xp = np.linspace(min(ang), max(ang), 10)

# Plotting result
#ax.plot(xp, p2(xp), color='k', linestyle = '--',  label='Boundary merger/non-merger')

	
######################################################
##
vel1 = np.array([1, 1, 1, 1])
ang1 = np.array([-75, -60, -45, 45])
	
vel2 = np.array([1.25, 1.25, 1.25, 1.25, 1.5])
ang2 = np.array([-75, -60, -45, 30, -75])
	
ax1.plot(ang1, vel1, 's', color = cc[0], markersize = 12., label = 'Merging, bi-lobe')
ax1.plot(ang2, vel2, 's', color = cc[0], markersize = 12.)		


#####

vel = np.array([2, 2, 2, 2, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
ang = np.array([-45, -30, 0, 30, -60, -45, -30, 0, 30, 45])

vel2 = np.array([1.25, 1.25, 1.25, 1.0, 1.0, 1.0])
ang2 = np.array([-30, 0, 30, -30, 0, 30])

ax1.plot(ang, vel, 's', color = cc[3], markersize = 12., label = 'Merging')
ax1.plot(ang2, vel2, 's', color = cc[3], markersize = 12.)

###
	
vel1 = np.array([1, 1, 1, 1])
ang1 = np.array([-75, -60, -45, 45])
	
vel2 = np.array([1.25, 1.25, 1.25, 1.25, 1.5])
ang2 = np.array([-75, -60, -45, 30, -75])
	
ax1.plot(ang1, vel1, 's', color = cc[0], markersize = 12.)
ax1.plot(ang2, vel2, 's', color = cc[0], markersize = 12.)		

	
##
vel = np.array([1, 1, 1.25, 1.25, 1.25, 1.5, 1.5, 1.5, 1.5, 2, 2, 2, 2, 2, 2])
ang = np.array([60, 75, 45, 60, 75, 30, 45, 60, 75, 30, 45, 60, 75, -75, -60])

ax1.plot(ang, vel, 's', color = cc[6], markersize = 12., label = 'Non-merging')

###

vel = np.array([2.5, 2, 1.5, 1.25, 1.15, 0.75])
ang = np.array([10, 13, 23, 38, 65, 80])
	
coeff = np.polyfit(ang, vel, deg = 2)

# Polynomial Function
p2 = lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2]

# Points to evaluate
xp = np.linspace(min(ang), max(ang), 10)

###

vel = np.array([1.6, 1.9, 2.0, 2.5 ])
ang = np.array([-80, -65, -45, -40 ])
	
coeff = np.polyfit(ang, vel, deg = 2)

# Polynomial Function
p2 = lambda x: coeff[0]*x**2 + coeff[1]*x + coeff[2]

# Points to evaluate
xp = np.linspace(min(ang), max(ang), 10)

# Plotting result
#ax1.plot(xp, p2(xp), color='k', linestyle = '--')

# Plot legends
ax.legend(loc=1, numpoints = 1, fontsize = 10, framealpha = 1, ncol = 2, columnspacing=0.6, labelspacing=0.5, handletextpad=0.4)
ax1.legend(loc=1, numpoints = 1, fontsize = 10, framealpha = 1, ncol = 2, columnspacing=0.6, labelspacing=0.5, handletextpad=0.4)

# Set axis labels 
ax.set_ylabel(r'Collision velocity, $v/v_{\rm esc}$')
ax1.set_ylabel(r'Collision velocity, $v/v_{\rm esc}$')

ax.set_xlabel(r'Collision angle, $\phi$ ($^\circ$)')
ax1.set_xlabel(r'Collision angle, $\phi$ ($^\circ$)')
				
	
# Set the axis limits
ax.set_ylim([0.65,2.5])
ax.set_xlim([-82,82])

ax1.set_ylim([0.65,2.5])
ax1.set_xlim([-82,82])
#ax.axis('equal')

ax.grid(linestyle = '--', linewidth = 0.4, color = 'gray')	
ax1.grid(linestyle = '--', linewidth = 0.4, color = 'gray')	
      
ax.set_title(r'$R_{\rm merger} > 4\,R_{\rm primary}$')      
ax1.set_title(r'$3.3\,R_{\rm primary} < R_{\rm merger} < 3.8\,R_{\rm primary}$')      
            
#Save figure
fig.tight_layout()


plt.savefig('Plots_output/merger.pdf', bbox_inches='tight', dpi = 250)

#Close plot
plt.close(fig)

