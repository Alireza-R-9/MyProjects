import numpy as np
import matplotlib.pyplot as plt

n = 1000

random_variables = np.random.rand(n)

mean_random_variables = np.cumsum(random_variables) / np.arange(1, n + 1)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(mean_random_variables)
plt.title('Law of Large Numbers')
plt.xlabel('Number of Variables')
plt.ylabel('Cumulative Mean')

num_experiments = 1000
sums = [np.sum(np.random.rand(n)) for _ in range(num_experiments)]

plt.subplot(1, 2, 2)
plt.hist(sums, bins=30, density=True, alpha=0.6, color='g')

mean_sum = np.mean(sums)
std_sum = np.std(sums)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = np.exp(-((x - mean_sum) ** 2) / (2 * std_sum ** 2)) / (np.sqrt(2 * np.pi) * std_sum)
plt.plot(x, p, 'k', linewidth=2)
plt.title('Central Limit Theorem')
plt.xlabel('Sum of Variables')
plt.ylabel('Density')

plt.tight_layout()
plt.show()
