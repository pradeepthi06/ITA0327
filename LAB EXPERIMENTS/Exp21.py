# Experiment 21: Effect of the OFDMA Downlink Scheduler on User Throughput and Fairness
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
users = 5
resource_blocks = 100
channel_rates = np.random.uniform(0.5, 8.0, (resource_blocks, users))

# Round Robin scheduler
rr_throughput = np.zeros(users)
for rb in range(resource_blocks):
    rr_throughput[rb % users] += channel_rates[rb, rb % users]

# Proportional Fair scheduler
pf_throughput = np.zeros(users)
average_rate = np.ones(users)
for rb in range(resource_blocks):
    metric = channel_rates[rb] / average_rate
    selected_user = np.argmax(metric)
    pf_throughput[selected_user] += channel_rates[rb, selected_user]
    average_rate = 0.9 * average_rate + 0.1 * pf_throughput / (rb + 1)

# Maximum Throughput scheduler
mt_throughput = np.zeros(users)
for rb in range(resource_blocks):
    selected_user = np.argmax(channel_rates[rb])
    mt_throughput[selected_user] += channel_rates[rb, selected_user]

def jain_fairness(values):
    return (np.sum(values) ** 2) / (len(values) * np.sum(values ** 2))

print("OFDMA DOWNLINK SCHEDULER COMPARISON")
print("-----------------------------------")
print("User   Round Robin   Proportional Fair   Max Throughput")
for user in range(users):
    print(f"{user+1:4d}   {rr_throughput[user]:10.2f}   {pf_throughput[user]:17.2f}   {mt_throughput[user]:14.2f}")

print("\nTotal system throughput:")
print(f"Round Robin       : {np.sum(rr_throughput):.2f}")
print(f"Proportional Fair : {np.sum(pf_throughput):.2f}")
print(f"Max Throughput    : {np.sum(mt_throughput):.2f}")

print("\nJain's fairness index:")
print(f"Round Robin       : {jain_fairness(rr_throughput):.3f}")
print(f"Proportional Fair : {jain_fairness(pf_throughput):.3f}")
print(f"Max Throughput    : {jain_fairness(mt_throughput):.3f}")

labels = ["Round Robin", "Proportional Fair", "Max Throughput"]
throughput = [rr_throughput.sum(), pf_throughput.sum(), mt_throughput.sum()]
fairness = [jain_fairness(rr_throughput), jain_fairness(pf_throughput), jain_fairness(mt_throughput)]

plt.figure(figsize=(8, 5))
plt.bar(labels, throughput)
plt.ylabel("Total throughput (arbitrary units)")
plt.title("OFDMA Scheduler - System Throughput")
plt.xticks(rotation=10)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(labels, fairness)
plt.ylabel("Jain's fairness index")
plt.ylim(0, 1.05)
plt.title("OFDMA Scheduler - User Fairness")
plt.xticks(rotation=10)
plt.grid(axis="y")
plt.tight_layout()
plt.show()
