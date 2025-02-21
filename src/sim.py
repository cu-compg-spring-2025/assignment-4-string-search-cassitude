import matplotlib.pyplot as plt

n = range(1, 100)
n_squared = [i**2 for i in n]

x_range = range(100, 1000)
m_values = [10, 50, 100]

for m in m_values:
    # naive
    # plt.plot(x_range, [(i - m + 1) for i in x_range], label=f"Best-case for m = {m}")
    # boyer-moore
    plt.plot(x_range, [i / (2 * m) for i in x_range], label=f"Best-case for m = {m}")

plt.xlabel("Input size")
plt.ylabel("Time")
plt.legend()
plt.show()
