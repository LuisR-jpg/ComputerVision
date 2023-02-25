import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.ylabel('Eje y')
plt.xlabel('Eje x')
ax.scatter(x = [1, 2, 3], y = [3, 2, 1])
#plt.savefig('Diagrama de dispersion.png')
plt.show()