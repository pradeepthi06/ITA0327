# Experiment 16: Free-Space Path Loss and Received Power
import numpy as np
import matplotlib.pyplot as plt

c = 3e8
frequency_mhz = 900
transmit_power_dbm = 30
transmit_gain_dbi = 2
receive_gain_dbi = 2

distance_km = np.linspace(0.1, 10, 100)
frequency_ghz = frequency_mhz / 1000

fspl_db = 32.44 + 20 * np.log10(distance_km) + 20 * np.log10(frequency_mhz)
received_power_dbm = (transmit_power_dbm + transmit_gain_dbi + receive_gain_dbi) - fspl_db

print("FREE-SPACE PATH LOSS AND RECEIVED POWER")
print("---------------------------------------")
print(f"Frequency             : {frequency_mhz} MHz")
print(f"Transmit power        : {transmit_power_dbm} dBm")
print(f"Transmit antenna gain : {transmit_gain_dbi} dBi")
print(f"Receive antenna gain  : {receive_gain_dbi} dBi")
print(f"FSPL at 1 km          : {32.44 + 20*np.log10(frequency_mhz):.2f} dB")
print(f"Received power at 1 km: {received_power_dbm[np.argmin(abs(distance_km-1))]:.2f} dBm")

plt.figure(figsize=(8, 5))
plt.plot(distance_km, fspl_db, label="Free-space path loss")
plt.xlabel("Distance (km)")
plt.ylabel("Path loss (dB)")
plt.title("Free-Space Path Loss vs Distance")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(distance_km, received_power_dbm, color="green", label="Received power")
plt.xlabel("Distance (km)")
plt.ylabel("Received power (dBm)")
plt.title("Received Power vs Distance")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
