from matplotlib import pyplot as plt
plt.style.use('grayscale')
val = [1,2,3,4]
mal = [112,334,556,332]
maps = [114,223,443,445]
malp = [124,564,543,689]
plt.plot(val,maps,color = "green",label ='data')

plt.plot(val,malp,color ='b',marker = '.', label='student')

plt.plot(val,mal,color ='k', linestyle ='--' ,linewidth = 3,label='teacher')
plt.xlabel("roll")
plt.ylabel("salary")
#plt.legend(['student','teacher'])

plt.legend()

plt.title("Salary distribution")

plt.grid(True)
plt.tight_layout()
plt.show()
