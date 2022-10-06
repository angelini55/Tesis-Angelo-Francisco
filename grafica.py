import matplotlib.pyplot as plt
import numpy as np 

fig, ax = plt.subplots()

x=[0,100,200,300,400,500,600,700]
y=[2,4,6,8,10,12,14,16]

ax.set_xlabel("Aumento de Temperatura ºF ", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel("Coefiiente de transfernecia de calor (hc o hr)")
ax.set_ylim([2,12])
ax.set_yticks(range(2, 12))

plt.plot(x,y)
plt.show()