# Experiment 19: Handoff Simulation with Hysteresis
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)
time = np.arange(0, 60)
serving_signal = -65 - 0.35*time + np.random.normal(0, 1.2, len(time))
target_signal = -88 + 0.38*time + np.random.normal(0, 1.2, len(time))

hysteresis_db = 3
handoff_state = np.zeros(len(time), dtype=int)
current_cell = 0
handoff_time = None

for t in range(len(time)):
    if current_cell == 0 and target_signal[t] > serving_signal[t] + hysteresis_db:
        current_cell = 1
        handoff_time = t
    handoff_state[t] = current_cell

print("HANDOFF SIMULATION WITH HYSTERESIS")
print("----------------------------------")
print(f"Hysteresis margin: {hysteresis_db} dB")
if handoff_time is not None:
    print(f"Handoff occurred at time step: {handoff_time}")
else:
    print("No handoff occurred during the simulation.")
print(f"Final serving cell: Cell {current_cell + 1}")

plt.figure(figsize=(9, 5))
plt.plot(time, serving_signal, label="Serving cell signal")
plt.plot(time, target_signal, label="Target cell signal")
if handoff_time is not None:
    plt.axvline(handoff_time, linestyle="--", label="Handoff")
plt.xlabel("Time step")
plt.ylabel("Received signal strength (dBm)")
plt.title("Handoff Decision Using Hysteresis")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 3))
plt.step(time, handoff_state + 1, where="post")
plt.yticks([1, 2], ["Cell 1", "Cell 2"])
plt.xlabel("Time step")
plt.ylabel("Serving cell")
plt.title("Serving Cell During Handoff")
plt.grid(True)
plt.tight_layout()
plt.show()
