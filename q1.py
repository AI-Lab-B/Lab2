import matplotlib.pyplot as plt
import numpy as np
group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15,40,45,50,62]
group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]
fig, (g1, g2) = plt.subplots(1, 2, figsize=(12, 6))


g1.boxplot(group_A)
g1.set_title("Group A")
g1.set_ylabel("Measurement Values")

#
g2.boxplot(group_B)
g2.set_title("Group B")
g2.set_ylabel("Measurement Values")

fig.suptitle("GROUP A & B's measurements")
plt.show()





