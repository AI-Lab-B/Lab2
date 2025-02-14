import numpy as np
import matplotlib.pyplot as plt

group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15, 40, 45, 50, 62]
group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.boxplot(group_A)
plt.title('Group A')
plt.ylabel('Measurement values')


plt.subplot(1, 2, 2)
plt.boxplot(group_B)
plt.title('Group B')
plt.ylabel('Measurement values')

print('Box plots for Group A and Group B')

plt.show()
