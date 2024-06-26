import matplotlib.pyplot as plt
import numpy as np

def moving_std(data, window_size):
    rolling_std = np.zeros_like(data)
    for i in range(len(data) - window_size + 1):
        rolling_std[i + window_size - 1] = np.std(data[i:i + window_size])
    return rolling_std

# Generate example data
np.random.seed(42)
data = np.random.randn(100)

# Set the window size for the moving standard deviation
window_size = 10

# Calculate the moving standard deviation
std_dev = moving_std(data, window_size)

# Plot the original data and the moving standard deviation
plt.figure(figsize=(10, 6))
plt.plot(data, label='Original Data', alpha=0.7)
plt.plot(np.arange(window_size - 1, len(data)), std_dev[window_size - 1:],
label=f'Moving Standard Deviation (window={window_size})', color='orange',
linewidth=2)
plt.title('Moving Standard Deviation Example')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.savefig("sample.pdf")
# plt.show()
#
