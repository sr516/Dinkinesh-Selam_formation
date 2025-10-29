import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import LineCollection


m1=7164042110.55478
m2=7164042110.55478
r1=89.32083197957208
r2=89.32083197957208

rc=359.5

vesc = np.sqrt(2.*6.67e-11*(m1+m2)/(r1+r2))

# Function to calculate relative position and velocity
def calculate_relative(df):
    x_rel = df['x_c1'] - df['x_c2']
    y_rel = df['y_c1'] - df['y_c2']
    z_rel = df['z_c1'] - df['z_c2']
    scaling_factor=np.linspace(0, 135 / 100, len(x_rel))
    df['vx_c1'] =  df['vx_c1']*(1 + np.sqrt(0.5)*scaling_factor)
    df['vy_c1'] =  df['vy_c1']*(1 + np.sqrt(0.5)*scaling_factor)
    df['vz_c1'] =  df['vz_c1']*(1 + np.sqrt(0.5)*scaling_factor)  
    vx_rel = df['vx_c1'] - df['vx_c2']
    vy_rel = df['vy_c1'] - df['vy_c2']
    vz_rel = df['vz_c1'] - df['vz_c2']
    
    distance_rel = np.sqrt(x_rel**2 + y_rel**2 + z_rel**2)
    speed_rel = np.sqrt(vx_rel**2 + vy_rel**2 + vz_rel**2)
  
    df['Relative_Position_(x)'] = x_rel
    df['Relative_Position_(y)'] = y_rel
    df['Relative_Position_(z)'] = y_rel
    df['Relative_Distance'] = distance_rel
    df['Relative_Velocity_(vx)'] = vx_rel
    df['Relative_Velocity_(vy)'] = vy_rel
    df['Relative_Velocity_(vz)'] = vz_rel
    df['Relative_Speed'] = speed_rel/vesc
    
    return df

# Load all files in the directory with specified naming pattern
file_pattern = 'sup*.txt'  # Adjust the pattern to match your file names
for filename in glob.glob(file_pattern):
    df = pd.read_csv(filename, delim_whitespace=True, header=None, names=['x_c1', 'y_c1', 'z_c1', 'x_c2', 'y_c2', 'z_c2', 'vx_c1', 'vy_c1', 'vz_c1', 'vx_c2', 'vy_c2', 'vz_c2'])
    relative_df = calculate_relative(df)
    
    # Save the results to a new file
    output_filename = filename.replace('sup', 'particle_data')
    relative_df.to_csv(output_filename, index=False, sep='\t')
    print(f"Processed and saved relative data for {filename} as {output_filename}")

    v1=np.sqrt(df['vx_c1']**2 + df['vy_c1']**2+ df['vz_c1']**2)
    v2=np.sqrt(df['vx_c2']**2 + df['vy_c2']**2+ df['vz_c2']**2)

    overall_min = np.min(np.concatenate((v1, v2)))
    overall_max = np.max(np.concatenate((v1, v2)))

    fig,ax= plt.subplots()
    ax.add_patch(Circle((0, 0), 1.0, edgecolor='black', facecolor='black'))
    ax.set_xlabel('X (Dinkinesh radius)')
    ax.set_xlabel('Y (Dinkinesh radius)')
    points = np.array([df['x_c1'], df['y_c1']]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap='gnuplot', norm=plt.Normalize(overall_min, overall_max))
    lc.set_array(np.array(v1))
    lc.set_linewidth(2)
    ax.add_collection(lc) 
    
    points = np.array([df['x_c2'], df['y_c2']]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap='gnuplot', norm=plt.Normalize(overall_min, overall_max))
    lc.set_array(np.array(v2))
    lc.set_linewidth(2)
    ax.add_collection(lc)

    ax.add_patch(Circle((df['x_c1'].iloc[-1], df['y_c1'].iloc[-1]), r1/rc, edgecolor='red', facecolor='red'))
    ax.add_patch(Circle((df['x_c2'].iloc[-1], df['y_c2'].iloc[-1]), r2/rc, edgecolor='blue', facecolor='blue'))
    
    ax.plot(df['x_c1'],df['y_c1'],lw=0)
    ax.set_aspect(1)
    plt.colorbar(lc, ax=ax, label="Orbital velocity")
    plt.show()
    
    fig,ax= plt.subplots()
    ax.set_xlabel('X (Dinkinesh radius)')
    ax.set_xlabel('Y (Dinkinesh radius)')
    
    vrel=np.array(df['Relative_Speed'])
    points = np.array([df['Relative_Position_(x)'], df['Relative_Position_(y)']]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap='gnuplot', norm=plt.Normalize(min(vrel), max(vrel)))
    lc.set_array(np.array(vrel))
    lc.set_linewidth(2)
    ax.add_collection(lc) 
    

    
    ax.add_patch(Circle((0., 0.), r1/rc, edgecolor='red', facecolor='red'))
    ax.add_patch(Circle((df['Relative_Position_(x)'].iloc[-1], df['Relative_Position_(y)'].iloc[-1]), r1/rc, edgecolor='blue', facecolor='blue'))
    
    ax.plot(df['Relative_Position_(x)'], df['Relative_Position_(y)'],lw=0)
    ax.set_aspect(1)
    plt.colorbar(lc, ax=ax, label="v_imp/v_esc")
    plt.show()
    
    print(vrel[-1])