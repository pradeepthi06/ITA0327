# Experiment 18: Call Blocking Probability Using the Erlang B Formula
import math
import matplotlib.pyplot as plt

def erlang_b(traffic, channels):
    blocking = 1.0
    for n in range(1, channels + 1):
        blocking = (traffic * blocking) / (n + traffic * blocking)
    return blocking

channels = 20
traffic_values = [5, 10, 15, 20, 25, 30, 35, 40]
blocking_values = [erlang_b(a, channels) for a in traffic_values]

print("CALL BLOCKING PROBABILITY - ERLANG B")
print("------------------------------------")
print(f"Number of channels: {channels}")
print("Traffic (Erlangs)   Blocking Probability   Blocking (%)")
for traffic, probability in zip(traffic_values, blocking_values):
    print(f"{traffic:8.1f}            {probability:.6f}             {probability*100:.3f}%")

plt.figure(figsize=(8, 5))
plt.plot(traffic_values, np.array(blocking_values) * 100 if False else [x*100 for x in blocking_values], marker="o")
plt.xlabel("Offered traffic (Erlangs)")
plt.ylabel("Call blocking probability (%)")
plt.title(f"Erlang B Blocking Probability ({channels} Channels)")
plt.grid(True)
plt.tight_layout()
plt.show()
