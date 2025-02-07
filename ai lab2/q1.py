import matplotlib.pyplot as plt

group_A=[12,15,14,13,16,18,19,15,14,20,17,14,15,40,45,50,62]
group_B=[12,17,15,13,19,20,21,18,17,16,15,14,16,15]

fig, ax = plt.subplots(1,2)
ax[0].boxplot(group_A)
ax[0].set_ylabel("Group_A values")
ax[0].set_title("Group_A")
ax[1].boxplot(group_B)
ax[1].set_ylabel("Group_B values")
ax[1].set_title("Group_B")

fig.suptitle("Ques:01 boxplot using subplots")

plt.show()