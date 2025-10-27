import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import rebound 
import sys

#matplotlib settings:
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble']=r"\usepackage{amsmath}"
mpl.rcParams['font.sans-serif'] = ['Arial']
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.size'] = 16
mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['figure.dpi'] = 300

G = 6.67e-8 #gravitational constant, cgs
N = int(1e5)# number of simulations 
            # not all simulations end in a collision
            # so the resulting collision data will be some fraction of this number

plot_only = False #True if you only want to generate plots from the data in coll_file. False if you want to rerun the simulations
coll_file = 'coll_log.txt' #name of log file for writing results

e_max = 0.5         #maximum initial eccentricity of satellite orbit
m_ratio_min = 1e-5  #min/max mass of each satellite w.r.t. primary
m_ratio_max = 1e-1

R = (720/2)*100 #Dinkinesh radius in cm
rho = 2.4       #bulk density of primary and satellites , g/cc
M = (4*np.pi/3)*rho*R**3 #mass of primary

#we are randomly generating two satellites m1 and m2
#the are assumed to be equal mass and density
a2_array = R*np.random.uniform(low=3,high=20, size=N) #randomly generated semimajor axis of m2
m1_array = M*10**np.random.uniform(low=np.log10(m_ratio_min), high=np.log10(m_ratio_max), size=N) #randomly generate satellite mass in log space

if not plot_only:
    j=0
    while j < N:
        #iterate through simulations
        sys.stdout.write(f'    Progress:    {j}/{N} = {100.0*j/N:.2f}% \r')
        sys.stdout.flush()

        a2 = a2_array[j] #m2 satellite semimajor axis
        m1 = m1_array[j] #m1 satellite mass
        r1 = ((3*m1/4/np.pi)/rho)**(1./3) #m1 radius
        m2, r2 = m1, r1 #assuming both satellites to have equal masses and radii

        v_esc = np.sqrt(2*G*(m1+m2)/(r1+r2)) #mutual escape speed

        rHill = a2*(m1/3/M)**(1./3) #m2 satellite's hill sphere
        a1 = np.random.uniform(low=a2-rHill, high=a2+rHill) #generate m1's semimajor axis to be within 1 hill sphere (to ensure a collision occurs in short time)
        e1, e2 = e_max*np.random.rand(), e_max*np.random.rand() #randomly generate eccentricities up to e_max
        inc1, inc2 = 0.0, 0.0 #assume zero inclination, consistent with YORP spin up. 

        #set up simulation
        sim = rebound.Simulation()
        sim.G = G
        sim.integrator='ias15'
        primary=sim.add(m=M, r=R*2.42 - r1, hash="prim") #give the primary a radius = to the fluid roche limit. This will cause the code to throw an exception if a satellite crosses this.
        sim.add(m=m1, r=r1, a = a1, e = e1, inc=inc1, omega=2*np.pi*np.random.rand(), Omega=2*np.pi*np.random.rand(), f = 2*np.pi*np.random.rand(),   hash='sat1',primary=primary)
        sim.add(m=m2, r=r2, a = a2, e = e2, inc=inc2, omega=2*np.pi*np.random.rand(), Omega=2*np.pi*np.random.rand(), f = 2*np.pi*np.random.rand(),   hash='sat2',primary=primary)
        sim.N_active=3
        sim.move_to_com()
        sim.collision = "direct"
        sim.collision_resolve = "halt" #if collision occurs, stop simulation and throw an exception
        ps=sim.particles   
    
        if ps[1] ** ps[2] < 2*rHill:
            #if we initialize the two satellites too close, skip this simulation
            continue

        P_syn = np.abs(1./(1./ps[1].P - 1./ps[2].P))
        runtime = min(10*P_syn, 100*24*3600) #run for 10 of synodic periods but no more than 100 days

        try:
            #run simulation until end or until and exception is thrown
            #if simulation makes it to the end without a collision, then we don't care
            sim.integrate(runtime)

        except rebound.Collision as error:
            ps=sim.particles
            p0, p1, p2 = ps[0], ps[1], ps[2]
            pos0 = np.array([p0.x, p0.y, p0.z]) #particle positions
            pos1 = np.array([p1.x, p1.y, p1.z])
            pos2 = np.array([p2.x, p2.y, p2.z])


            v0 = np.array([p0.vx, p0.vy, p0.vz]) #particle velocities
            v1 = np.array([p1.vx, p1.vy, p1.vz])
            v2 = np.array([p2.vx, p2.vy, p2.vz])

            if np.linalg.norm(pos1-pos2) <= p1.r+p2.r:
                #check if the two satellites are in a collision
                #note: the distance between the two particles is often a bit less than the sum of their radii
                #(this means that these impact speeds are a very slight overestimate)

                v_rel = v1-v2     #relative speeds and positions
                r_rel = pos1-pos2
                vel = np.linalg.norm(v_rel)
                dist = np.linalg.norm(r_rel)
                assert(np.dot(v_rel, r_rel)<=0.0) #assert particles are approaching. 
                                                 #This is a sanity check to make sure collision detection is working correctly 

                theta = np.arccos(-np.dot(v_rel/vel, r_rel/dist)) #impact angle. This could optionally be recorded in text file
                
                #write to file:
                f = open(coll_file, 'a')
                f.write(f"{np.linalg.norm(v1-v2)/v_esc} {np.linalg.norm(pos0 -  (pos1+pos2)/2)/R} {m1/M} \n")
                f.close()
                j+=1

            elif np.linalg.norm(pos1-pos0) <= p1.r+p0.r:
                #collision between primary and sat1
                #ignore this run
                continue

            elif np.linalg.norm(pos2-pos0) <= p2.r+p0.r:
                #primary and sat2
                #ignore this run
                continue

            else:
                #simulation did not finish and no collision detected
                print("something is wrong")
                quit()




# make plots

data = np.genfromtxt(coll_file)
v = data[:, 0] #collision speed (in mutual escape speeds)
d = data[:, 1] #collision distance (in primary radii)
m = data[:, 2] #satellite-to-primary mass ratio
# theta = data[:,3]-

colorNorm = mpl.colors.Normalize(vmin=0.25, vmax=2.75, clip=True)
cmap = plt.get_cmap("viridis_r", 5)  

plt.scatter(d, m, c=v, cmap=cmap, norm=colorNorm, s=0.8, rasterized=True) 
cbar = plt.colorbar(label=r'$v/v_\text{esc}$', extend='max', pad=0.01)

v2       = 230**3 #volume of Selam (ignoring 4pi/3)
v2_sigma = 0.1*v2 #hand-wavy 10% uncertainty
v1       = 720**3 #volume of Dinkinesh
v1_sigma = 0.1*v1 

f = v2/v1 #volume fraction
f_sigma = f*np.sqrt((v1_sigma/v1)**2 + (v2_sigma/v2)**2) #crude error propagation

plt.ylim([1e-5,1e-1])
plt.xlim([3,20])
plt.xticks(np.arange(3,21,3))
xmin, xmax = plt.gca().get_xlim()

plt.fill_between([xmin,xmax], (v2-v2_sigma)/(v1+v1_sigma), (v2+v2_sigma)/(v1-v1_sigma), facecolor="gray", edgecolor="gray", alpha=0.5)#, hatch='///')
plt.text(xmax*0.99, 0.032, r"$\textbf{approx. lobe mass}$", ha='right', va='center', fontsize = 14, fontweight='bold', fontfamily='sans-serif', fontname='Arial')

plt.fill_between([xmin,xmax], 0.5*(v2-v2_sigma)/(v1+v1_sigma), 0.5*(v2+v2_sigma)/(v1-v1_sigma), facecolor="gray", edgecolor="gray", alpha=0.5)#, hatch='///')
plt.text(xmax*0.99, 0.032/2, r"$\textbf{approx. half lobe mass}$", ha='right', va='center', fontsize = 14, fontweight='bold', fontfamily='sans-serif', fontname='Arial')

plt.yscale('log')
plt.gca().xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(3))
plt.xlabel(r'$d/R_\text{primary}$')
plt.ylabel(r'$m/M_\text{primary}$')
plt.tight_layout()
plt.savefig('v_coll.pdf')
plt.close()
plt.show()

