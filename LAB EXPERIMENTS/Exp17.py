# Experiment 17: Frequency (Co-channel) Reuse - Cluster Size, Capacity and S/I
import numpy as np
import matplotlib.pyplot as plt

i_values = np.arange(0, 6)
j_values = np.arange(0, 6)
N_values = []
for i in i_values:
    for j in j_values:
        if i == 0 and j == 0:
            continue
        N_values.append((i, j, i*i + i*j + j*j))

print("CO-CHANNEL FREQUENCY REUSE")
print("--------------------------")
print("Cluster combinations (i, j) and cluster size N:")
for i, j, n in N_values:
    print(f"(i={i}, j={j}) -> N={n}")

cell_radius_km = 1.0
path_loss_exponent = 4
reuse_factor = 3
channels_total = 420
users_per_channel = 1

D_R = np.sqrt(3 * reuse_factor)
cochannel_ratio = D_R ** path_loss_exponent / 6
capacity = channels_total / reuse_factor

print(f"\nSelected cluster size N : {reuse_factor}")
print(f"Reuse distance ratio D/R: {D_R:.3f}")
print(f"Approximate S/I         : {cochannel_ratio:.2f} ({10*np.log10(cochannel_ratio):.2f} dB)")
print(f"Total available channels: {channels_total}")
print(f"Channels per cell       : {capacity:.0f}")

cluster_sizes = np.array([1, 3, 4, 7, 9, 12, 13, 16, 19])
channels_per_cell = channels_total / cluster_sizes
plt.figure(figsize=(8, 5))
plt.plot(cluster_sizes, channels_per_cell, marker="o")
plt.xlabel("Cluster size (N)")
plt.ylabel("Channels per cell")
plt.title("Capacity per Cell vs Cluster Size")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(cluster_sizes, np.sqrt(3*cluster_sizes), marker="s")
plt.xlabel("Cluster size (N)")
plt.ylabel("Reuse distance ratio (D/R)")
plt.title("Frequency Reuse Distance vs Cluster Size")
plt.grid(True)
plt.tight_layout()
plt.show()
