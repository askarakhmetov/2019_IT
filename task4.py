import numpy as np
import matplotlib.pyplot as plt

m=7
n=7
X=np.trunc(np.random.rand(n, m)*100)

def true_pareto(index, X):
    for i, vec in enumerate(X):
        if i != index and np.all(X[index, :] <= vec):
            return False
    return True

pareto = []
nopareto = []
for ind in range(X.shape[0]):
    if true_pareto(ind, X):
        pareto.append(ind)
    else:
        nopareto.append(ind)

fig, axes = plt.subplots(1, subplot_kw=dict(polar=True))

angle = 2 * np.pi * np.arange(0, 1 + 1 / m, 1 / m)
for i in pareto:
    axes.plot(angle, np.append(X[i], X[i, 0]))
plt.show()