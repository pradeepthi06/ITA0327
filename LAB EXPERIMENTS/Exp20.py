# Experiment 20: Code Division Multiple Access (CDMA) - Spreading and Despreading
import numpy as np
import matplotlib.pyplot as plt

data_bits = np.array([1, 0, 1, 1])
user_code = np.array([1, 1, 1, -1, 1, -1, -1, -1])
spreading_factor = len(user_code)

polar_data = 2 * data_bits - 1
spread_signal = np.concatenate([bit * user_code for bit in polar_data])
received_signal = spread_signal.copy()

despread_bits = []
for start in range(0, len(received_signal), spreading_factor):
    segment = received_signal[start:start + spreading_factor]
    correlation = np.sum(segment * user_code) / spreading_factor
    despread_bits.append(1 if correlation > 0 else 0)

despread_bits = np.array(despread_bits)

print("CDMA SPREADING AND DESPREADING")
print("-----------------------------")
print("Original data bits :", data_bits)
print("Spreading code     :", user_code)
print("Spread signal      :", spread_signal)
print("Despread bits      :", despread_bits)
print("Successful recovery:", np.array_equal(data_bits, despread_bits))

plt.figure(figsize=(10, 4))
plt.step(np.arange(len(spread_signal)), spread_signal, where="post")
plt.xlabel("Chip index")
plt.ylabel("Chip value")
plt.title("CDMA Spread Signal")
plt.yticks([-1, 1])
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.step(np.arange(len(data_bits)), data_bits, where="post", label="Original")
plt.step(np.arange(len(despread_bits)), despread_bits, where="post", linestyle="--", label="Despread")
plt.xlabel("Bit index")
plt.ylabel("Bit value")
plt.title("Original and Despread Data")
plt.yticks([0, 1])
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
