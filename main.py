import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


# aerodynamic parameters
rho = 1.225  # kg/m^3
v_pitching = 43  # m/s
S = 0.77  # m^2
q_pitching = 1/2 * rho * v_pitching**2
q = 1/2 * rho * 50**2
AoA_pitching = [0,5,10]
ref_len = 0.479  # m (span/2)


# read and extract simulation data
column_names = ["t", "Fx", "Fy", "Fz", "Mx", "My", "Mz", "ref_mat_1", "ref_mat_2", "ref_mat_3", "ref_mat_4", "ref_mat_5", "ref_mat_6", "ref_mat_7", "ref_mat_8", "ref_mat_9", "ref_off_1", "ref_off_2", "ref_off_3"]
post_loads_pitching = []
t = [[],[],[]]
Cz = [[],[],[]]
Cx = [[],[],[]]
Cm = [[],[],[]]

pitch_angle = []
for i in list(np.linspace(0,2*np.pi,161)):
    pitch_angle.append(5*np.sin(i))

for i in AoA_pitching:
    post_loads_pitching.append(pd.read_table(f"post_loads_pitching_{i}_u43.dat", skiprows = 4, sep=r"\s+", names=column_names))
    for j in range(len(pitch_angle)):
        t[int(i/5)].append(post_loads_pitching[int(i/5)]["t"][160+j])
        Cz[int(i/5)].append(post_loads_pitching[int(i/5)]["Fz"][160+j]/(q_pitching*S))
        Cx[int(i/5)].append(post_loads_pitching[int(i/5)]["Fx"][160+j]/(q_pitching*S))
        Cm[int(i/5)].append(post_loads_pitching[int(i/5)]["My"][160+j]/(q_pitching*S*ref_len))

post_loads_pitching_old = []
t_old = [[],[],[]]
Cz_old = [[],[],[]]
Cx_old = [[],[],[]]
Cm_old = [[],[],[]]

for i in AoA_pitching:
    post_loads_pitching_old.append(pd.read_table(f"post_loads_pitching_{i}_old.dat", skiprows = 0, sep=r"\s+", names=column_names))
    for j in range(len(pitch_angle)):
        t_old[int(i/5)].append(float(post_loads_pitching_old[int(i/5)]["t"][160+j]))
        Cz_old[int(i/5)].append(float(post_loads_pitching_old[int(i/5)]["Fz"][160+j])/(q*S))
        Cx_old[int(i/5)].append(float(post_loads_pitching_old[int(i/5)]["Fx"][160+j])/(q*S))
        Cm_old[int(i/5)].append(float(post_loads_pitching_old[int(i/5)]["My"][160+j])/(q*S*ref_len))


# read and extract experimental data
post_loads_pitching_exp = [[],[],[]]
Cz_exp = [[],[],[]]
Cz_pitch = [[],[],[]]
Cx_exp = [[],[],[]]
Cx_pitch = [[],[],[]]
Cm_exp = [[],[],[]]
Cm_pitch = [[],[],[]]

for i in [5,10]:
    post_loads_pitching_exp[0].append(pd.read_excel(f"expCza{i}.xlsx", names=["pitch angle","C"]))
    post_loads_pitching_exp[1].append(pd.read_excel(f"expCxa{i}.xlsx", names=["pitch angle","C"]))
    post_loads_pitching_exp[2].append(pd.read_excel(f"expCma{i}.xlsx", names=["pitch angle","C"]))

for i in range(2):
    Cz_exp[i] = post_loads_pitching_exp[0][i]["C"]
    Cz_pitch[i] = post_loads_pitching_exp[0][i]["pitch angle"]
    Cx_exp[i] = post_loads_pitching_exp[1][i]["C"]
    Cx_pitch[i] = post_loads_pitching_exp[1][i]["pitch angle"]
    Cm_exp[i] = post_loads_pitching_exp[2][i]["C"]
    Cm_pitch[i] = post_loads_pitching_exp[2][i]["pitch angle"]


#plotting
fig, ax = plt.subplots(2,3, figsize=(16,10))
fig.suptitle("Develop Branch of DUST vs Master Branch of DUST vs Experimental Results: Dynamic Pitching")
fig.subplots_adjust(hspace=0.4)

ax[0][0].plot([5*np.sin((x-1)*2*np.pi)+5 for x in t_old[1]], Cz_old[1], color="red", label="master")
ax[0][0].plot([5*np.sin((x-1)*2*np.pi)+5 for x in t[1]], Cz[1], color="orange", label="develop")
ax[0][0].plot(Cz_pitch[0], Cz_exp[0], color="black", label="exp")
ax[0][0].set_xlabel("Pitch Angle (degrees)")
ax[0][0].set_ylabel("Cz")
ax[0][0].set_ylim(bottom=0,top=1)
ax[0][0].set_title("Cz (AoA 5)")
ax[0][0].grid()
ax[0][0].legend()

ax[1][0].plot([5*np.sin((x-1)*2*np.pi)+10 for x in t_old[2]], Cz_old[2], color="blue", label="master")
ax[1][0].plot([5*np.sin((x-1)*2*np.pi)+10 for x in t[2]], Cz[2], color="pink", label="develop")
ax[1][0].plot(Cz_pitch[1], Cz_exp[1], color="black", label="exp")
ax[1][0].set_xlabel("Pitch Angle (degrees)")
ax[1][0].set_ylabel("Cz")
ax[1][0].set_ylim(bottom=0,top=1)
ax[1][0].set_title("Cz (AoA 10)")
ax[1][0].grid()
ax[1][0].legend()

ax[0][1].plot([5*np.sin((x-1)*2*np.pi)+5 for x in t_old[1]], Cx_old[1], color="red", label="master")
ax[0][1].plot([5*np.sin((x-1)*2*np.pi)+5 for x in t[1]], Cx[1], color="orange", label="develop")
ax[0][1].plot(Cx_pitch[0], Cx_exp[0], color="black", label="exp")
ax[0][1].set_xlabel("Pitch Angle (degrees)")
ax[0][1].set_ylabel("Cx")
ax[0][1].set_ylim(bottom=-0.2,top=0.2)
ax[0][1].set_title("Cx (AoA 5)")
ax[0][1].grid()
ax[0][1].legend()

ax[1][1].plot([5*np.sin((x-1)*2*np.pi)+10 for x in t_old[2]], Cx_old[2], color="blue", label="master")
ax[1][1].plot([5*np.sin((x-1)*2*np.pi)+10 for x in t[2]], Cx[2], color="pink", label="develop")
ax[1][1].plot(Cx_pitch[1], Cx_exp[1], color="black", label="exp")
ax[1][1].set_xlabel("Pitch Angle (degrees)")
ax[1][1].set_ylabel("Cx")
ax[1][1].set_ylim(bottom=-0.2,top=0.2)
ax[1][1].set_title("Cx (AoA 10)")
ax[1][1].grid()
ax[1][1].legend()

ax[0][2].plot([5*np.sin((x-1)*2*np.pi)+5 for x in t_old[1]], Cm_old[1], color="red", label="master")
ax[0][2].plot([5*np.sin((x-1)*2*np.pi)+5 for x in t[1]], Cm[1], color="orange", label="develop")
ax[0][2].plot(Cm_pitch[0], Cm_exp[0], color="black", label="exp")
ax[0][2].set_xlabel("Pitch Angle (degrees)")
ax[0][2].set_ylabel("Cm")
ax[0][2].set_ylim(bottom=0,top=0.05)
ax[0][2].set_title("Cm (AoA 5)")
ax[0][2].grid()
ax[0][2].legend()

ax[1][2].plot([5*np.sin((x-1)*2*np.pi)+10 for x in t_old[2]], Cm_old[2], color="blue", label="master")
ax[1][2].plot([5*np.sin((x-1)*2*np.pi)+10 for x in t[2]], Cm[2], color="pink", label="develop")
ax[1][2].plot(Cm_pitch[1], Cm_exp[1], color="black", label="exp")
ax[1][2].set_xlabel("Pitch Angle (degrees)")
ax[1][2].set_ylabel("Cm")
ax[1][2].set_ylim(bottom=0,top=0.05)
ax[1][2].set_title("Cm (AoA 10)")
ax[1][2].grid()
ax[1][2].legend()

fig.savefig("plot.png")
fig.show()
plt.show()
