import pandas as pd
from matplotlib import pyplot as plt

rho = 1.225  # kg/m^3
v_static_alpha = 50  # m/s
S = 0.77  # m^2
q_static_alpha = 1/2 * rho * v_static_alpha**2
AoA_static_alpha = [0,3,6,9,12,15]
chord_ref = 0.479  # m

post_loads_static_alpha = []
column_names = ["t", "Fx", "Fy", "Fz", "Mx", "My", "Mz", "ref_mat_1", "ref_mat_2", "ref_mat_3", "ref_mat_4", "ref_mat_5", "ref_mat_6", "ref_mat_7", "ref_mat_8", "ref_mat_9", "ref_off_1", "ref_off_2", "ref_off_3"]
Cx = []
Cz = []
Cm = []

for i in AoA_static_alpha:
    post_loads_static_alpha.append(pd.read_table(f"post_loads_static_alpha_{i}.dat", skiprows = 4, sep=r"\s+", names=column_names))
    Cx.append(post_loads_static_alpha[int(i/3)]["Fx"][319]/(q_static_alpha*S))
    Cz.append(post_loads_static_alpha[int(i/3)]["Fz"][319]/(q_static_alpha*S))
    Cm.append(post_loads_static_alpha[int(i/3)]["My"][319]/(q_static_alpha*S*chord_ref))

post_loads_static_alpha_old = []
Cx_old = []
Cz_old = []
Cm_old = []

for i in AoA_static_alpha:
    post_loads_static_alpha_old.append(pd.read_table(f"post_loads_static_alpha_{i}_old.dat", sep=r"\s+", names=column_names))
    Cx_old.append(post_loads_static_alpha_old[int(i/3)]["Fx"][319]/(q_static_alpha*S))
    Cz_old.append(post_loads_static_alpha_old[int(i/3)]["Fz"][319]/(q_static_alpha*S))
    Cm_old.append(post_loads_static_alpha_old[int(i/3)]["My"][319]/(q_static_alpha*S*chord_ref))


fig, ax = plt.subplots(1, 3, figsize=(16,4))
fig.suptitle("Develop Branch of DUST vs Master Branch of DUST")

ax[0].plot(AoA_static_alpha, Cx, color="blue", label="develop",marker="o")
ax[0].plot(AoA_static_alpha, Cx_old, color="red", label="master",marker="x")
ax[0].set_xlabel("AoA (degrees)")
ax[0].set_ylabel("Cx")
ax[0].set_ylim(bottom=-0.15,top=0.05)
ax[0].set_title("Cx vs AoA")
ax[0].grid()
ax[0].legend()

ax[1].plot(AoA_static_alpha, Cz, color="blue", label="develop",marker="o")
ax[1].plot(AoA_static_alpha, Cz_old, color="red", label="master",marker="x")
ax[1].set_xlabel("AoA (degrees)")
ax[1].set_ylabel("Cy")
ax[1].set_ylim(bottom=-0.1,top=0.8)
ax[1].set_title("Cy vs AoA")
ax[1].grid()
ax[1].legend()

ax[2].plot(AoA_static_alpha, Cm, color="blue", label="develop",marker="o")
ax[2].plot(AoA_static_alpha, Cm_old, color="red", label="master",marker="x")
ax[2].set_xlabel("AoA (degrees)")
ax[2].set_ylabel("Cm")
ax[2].set_ylim(bottom=-0.01,top=0.1)
ax[2].set_title("Cm vs AoA")
ax[2].grid()
ax[2].legend()

fig.savefig("plot.png")
fig.show()
plt.show()
