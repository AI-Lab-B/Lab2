import numpy as np
import matplotlib.pyplot as plt

group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15, 40, 45, 50, 62]
group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]

# Creating plot
plt.boxplot(group_A)
plt.title('Box Plot of Group A Measurements')
plt.ylabel('Measurement Values')
plt.show()

plt.boxplot(group_B)
plt.title('Box Plot of Group B Measurements')
plt.ylabel('Measurement Values')
plt.show()