import numpy as np
from matplotlib import pyplot as plt
plt.style.use('grayscale')
val = [1,2,3,4]
x = np.arange(len(val))
width = 0.25
mal = [112,334,556,332]
maps = [114,223,443,445]
malp = [124,564,543,689]

plt.bar(x - width,maps,width=width,color = "green",label ='data')

plt.bar(x,malp,color ='b',width=width, label='student')

plt.bar(x + width,mal,color ='k',width=width, linestyle ='--' ,label='teacher')
plt.xlabel("roll")
plt.ylabel("salary")
plt.xticks(ticks=x,labels=val)
plt.legend()

plt.title("Salary distribution")

plt.grid(True)
plt.tight_layout()
plt.show()


