from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")

fruits = [1,2,3,4,5]

st1 = [1,2,3,3,2]
st2 = [1,2,3,4,5]
labels = [st1,st2]
colors = ['green','pink']


plt.stackplot(fruits,st1,st2,labels=labels,colors=colors)
plt.legend(loc= 'upper left')
plt.show()



