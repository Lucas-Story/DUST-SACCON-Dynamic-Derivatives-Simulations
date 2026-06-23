import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


# aerodynamic parameters
rho = 1.225  # kg/m^3
v_rolling = 43  # m/s
S = 0.77  # m^2
q_rolling = 1/2 * rho * v_rolling**2
AoA_rolling = [0,5,10]
ref_len = 0.769  # m (span/2)


# read and extract simulation data
column_names = ["t", "Fx", "Fy", "Fz", "Mx", "My", "Mz", "ref_mat_1", "ref_mat_2", "ref_mat_3", "ref_mat_4", "ref_mat_5", "ref_mat_6", "ref_mat_7", "ref_mat_8", "ref_mat_9", "ref_off_1", "ref_off_2", "ref_off_3"]
post_loads_rolling = []
t = [[],[],[]]
Cy = [[],[],[]]
Cn = [[],[],[]]
Cl = [[],[],[]]

roll_angle = []
for i in list(np.linspace(0,2*np.pi,161)):
    roll_angle.append(5*np.sin(i))

for i in AoA_rolling:
    post_loads_rolling.append(pd.read_table(f"post_loads_rolling_{i}.dat", skiprows = 4, sep=r"\s+", names=column_names))
    for j in range(len(roll_angle)):
        t[int(i/5)].append(post_loads_rolling[int(i/5)]["t"][160+j])
        Cy[int(i/5)].append(post_loads_rolling[int(i/5)]["Fy"][160+j]/(q_rolling*S))
        Cn[int(i/5)].append(post_loads_rolling[int(i/5)]["Mz"][160+j]/(q_rolling*S*ref_len))
        Cl[int(i/5)].append(post_loads_rolling[int(i/5)]["Mx"][160+j]/(q_rolling*S*ref_len))

post_loads_rolling_old = []
t_old = [[],[],[]]
Cy_old = [[],[],[]]
Cn_old = [[],[],[]]
Cl_old = [[],[],[]]

for i in AoA_rolling:
    post_loads_rolling_old.append(pd.read_table(f"post_loads_rolling_{i}_old.dat", skiprows = 0, sep=r"\s+", names=column_names))
    for j in range(len(roll_angle)):
        t_old[int(i/5)].append(float(post_loads_rolling_old[int(i/5)]["t"][160+j]))
        Cy_old[int(i/5)].append(float(post_loads_rolling_old[int(i/5)]["Fy"][160+j])/(q_rolling*S))
        Cn_old[int(i/5)].append(float(post_loads_rolling_old[int(i/5)]["Mz"][160+j])/(q_rolling*S*ref_len))
        Cl_old[int(i/5)].append(float(post_loads_rolling_old[int(i/5)]["Mx"][160+j])/(q_rolling*S*ref_len))


# read and extract experimental data
post_loads_rolling_exp = [[],[],[]]
Cy_exp = [[],[],[]]
Cy_roll = [[],[],[]]
Cn_exp = [[],[],[]]
Cn_roll = [[],[],[]]
Cl_exp = [[],[],[]]
Cl_roll = [[],[],[]]

for i in AoA_rolling:
    post_loads_rolling_exp[0].append(pd.read_excel(f"expCy_a{i}.xlsx", names=["roll angle","C"]))
    post_loads_rolling_exp[1].append(pd.read_excel(f"expCn_a{i}.xlsx", names=["roll angle","C"]))
    post_loads_rolling_exp[2].append(pd.read_excel(f"expCl_a{i}.xlsx", names=["roll angle","C"]))

for i in range(3):
    Cy_exp[i] = post_loads_rolling_exp[0][i]["C"]
    Cy_roll[i] = post_loads_rolling_exp[0][i]["roll angle"]
    Cn_exp[i] = post_loads_rolling_exp[1][i]["C"]
    Cn_roll[i] = post_loads_rolling_exp[1][i]["roll angle"]
    Cl_exp[i] = post_loads_rolling_exp[2][i]["C"]
    Cl_roll[i] = post_loads_rolling_exp[2][i]["roll angle"]


#plotting
fig, ax = plt.subplots(3,3, figsize=(16,16))
fig.suptitle("Develop Branch of DUST vs Master Branch of DUST vs Experimental Results: Dynamic Rolling")
fig.subplots_adjust(hspace=0.4)

ax[0][0].plot([5*np.sin((x-1)*2*np.pi) for x in t_old[0]], [x*10**3 for x in Cy_old[0]], color="blue", label="master")
ax[0][0].plot([5*np.sin((x-1)*2*np.pi) for x in t[0]], [x*10**3 for x in Cy[0]], color="green", label="develop")
ax[0][0].plot(Cy_roll[0], [x*10**3 for x in Cy_exp[0]], color="black", label="exp")
ax[0][0].set_xlabel("Roll Angle (degrees)")
ax[0][0].set_ylabel("Cy")
ax[0][0].set_ylim(bottom=-5,top=5)
ax[0][0].set_title("Cy (AoA 0)")
ax[0][0].grid()
ax[0][0].legend()

ax[1][0].plot([5*np.sin((x-1)*2*np.pi) for x in t_old[1]], [x*10**3 for x in Cy_old[1]], color="red", label="master")
ax[1][0].plot([5*np.sin((x-1)*2*np.pi) for x in t[1]], [x*10**3 for x in Cy[1]], color="orange", label="develop")
ax[1][0].plot(Cy_roll[1], [x*10**3 for x in Cy_exp[1]], color="black", label="exp")
ax[1][0].set_xlabel("Roll Angle (degrees)")
ax[1][0].set_ylabel("Cy")
ax[1][0].set_ylim(bottom=-5,top=5)
ax[1][0].set_title("Cy (AoA 5)")
ax[1][0].grid()
ax[1][0].legend()

ax[2][0].plot([5*np.sin((x-1)*2*np.pi) for x in t_old[2]], [x*10**3 for x in Cy_old[2]], color="blue", label="master")
ax[2][0].plot([5*np.sin((x-1)*2*np.pi) for x in t[2]], [x*10**3 for x in Cy[2]], color="pink", label="develop")
ax[2][0].plot(Cy_roll[2], [x*10**3 for x in Cy_exp[2]], color="black", label="exp")
ax[2][0].set_xlabel("Roll Angle (degrees)")
ax[2][0].set_ylabel("Cy")
ax[2][0].set_ylim(bottom=-5,top=5)
ax[2][0].set_title("Cy (AoA 10)")
ax[2][0].grid()
ax[2][0].legend()

ax[0][1].plot([5*np.sin((x-1)*2*np.pi) for x in t_old[0]], [x*10**3 for x in Cn_old[0]], color="blue", label="master")
ax[0][1].plot([5*np.sin((x-1)*2*np.pi) for x in t[0]], [x*10**3 for x in Cn[0]], color="green", label="develop")
ax[0][1].plot(Cn_roll[0], [x*10**3 for x in Cn_exp[0]], color="black", label="exp")
ax[0][1].set_xlabel("Roll Angle (degrees)")
ax[0][1].set_ylabel("Cn")
ax[0][1].set_ylim(bottom=-5,top=5)
ax[0][1].set_title("Cn (AoA 0)")
ax[0][1].grid()
ax[0][1].legend()

ax[1][1].plot([5*np.sin((x-1)*2*np.pi) for x in t_old[1]], [x*10**3 for x in Cn_old[1]], color="red", label="master")
ax[1][1].plot([5*np.sin((x-1)*2*np.pi) for x in t[1]], [x*10**3 for x in Cn[1]], color="orange", label="develop")
ax[1][1].plot(Cn_roll[1], [x*10**3 for x in Cn_exp[1]], color="black", label="exp")
ax[1][1].set_xlabel("Roll Angle (degrees)")
ax[1][1].set_ylabel("Cn")
ax[1][1].set_ylim(bottom=-5,top=5)
ax[1][1].set_title("Cn (AoA 5)")
ax[1][1].grid()
ax[1][1].legend()

ax[2][1].plot([5*np.sin((x-1)*2*np.pi) for x in t_old[2]], [x*10**3 for x in Cn_old[2]], color="blue", label="master")
ax[2][1].plot([5*np.sin((x-1)*2*np.pi) for x in t[2]], [x*10**3 for x in Cn[2]], color="pink", label="develop")
ax[2][1].plot(Cn_roll[2], [x*10**3 for x in Cn_exp[2]], color="black", label="exp")
ax[2][1].set_xlabel("Roll Angle (degrees)")
ax[2][1].set_ylabel("Cn")
ax[2][1].set_ylim(bottom=-5,top=5)
ax[2][1].set_title("Cn (AoA 10)")
ax[2][1].grid()
ax[2][1].legend()

ax[0][2].plot([5*np.sin((x-1)*2*np.pi) for x in t_old[0]], [x*10**3 for x in Cl_old[0]], color="blue", label="master")
ax[0][2].plot([5*np.sin((x-1)*2*np.pi) for x in t[0]], [x*10**3 for x in Cl[0]], color="green", label="develop")
ax[0][2].plot(Cl_roll[0], [x*10**3 for x in Cl_exp[0]], color="black", label="exp")
ax[0][2].set_xlabel("Roll Angle (degrees)")
ax[0][2].set_ylabel("Cl")
ax[0][2].set_ylim(bottom=-5,top=5)
ax[0][2].set_title("Cl (AoA 0)")
ax[0][2].grid()
ax[0][2].legend()

ax[1][2].plot([5*np.sin((x-1)*2*np.pi) for x in t_old[1]], [x*10**3 for x in Cl_old[1]], color="red", label="master")
ax[1][2].plot([5*np.sin((x-1)*2*np.pi) for x in t[1]], [x*10**3 for x in Cl[1]], color="orange", label="develop")
ax[1][2].plot(Cl_roll[1], [x*10**3 for x in Cl_exp[1]], color="black", label="exp")
ax[1][2].set_xlabel("Roll Angle (degrees)")
ax[1][2].set_ylabel("Cl")
ax[1][2].set_ylim(bottom=-5,top=5)
ax[1][2].set_title("Cl (AoA 5)")
ax[1][2].grid()
ax[1][2].legend()

ax[2][2].plot([5*np.sin((x-1)*2*np.pi) for x in t_old[2]], [x*10**3 for x in Cl_old[2]], color="blue", label="master")
ax[2][2].plot([5*np.sin((x-1)*2*np.pi) for x in t[2]], [x*10**3 for x in Cl[2]], color="pink", label="develop")
ax[2][2].plot(Cl_roll[2], [x*10**3 for x in Cl_exp[2]], color="black", label="exp")
ax[2][2].set_xlabel("Roll Angle (degrees)")
ax[2][2].set_ylabel("Cl")
ax[2][2].set_ylim(bottom=-8,top=8)
ax[2][2].set_title("Cl (AoA 10)")
ax[2][2].grid()
ax[2][2].legend()

fig.savefig("plot.png")
fig.show()
plt.show()
