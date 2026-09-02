import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=42)

mean0 = [2, 3]
mean1 = [5, 6]
mean2 = [8, 1]
mean3 = [15, 4]
std0 = [0.8, 2.5]
std1 = [1.2, 1.9]
std2 = [0.9, 0.9]
std3 = [0.5, 2.0]

class0 = rng.normal(
    loc=mean0,
    scale=std0,
    size=(100, 2)
)
class1 = rng.normal(
    loc=mean1,
    scale=std1,
    size=(100, 2)
)
class2 = rng.normal(
    loc=mean2,
    scale=std2,
    size=(100, 2)
)
class3 = rng.normal(
    loc=mean3,
    scale=std3,
    size=(100, 2)
)

figure0 = plt.scatter(class0[:, 0], class0[:, 1], color='blue', label='Class 0')
figure1 = plt.scatter(class1[:, 0], class1[:, 1], color='orange', label='Class 1')
figure2 = plt.scatter(class2[:, 0], class2[:, 1], color='red', label='Class 2')
figure3 = plt.scatter(class3[:, 0], class3[:, 1], color='green', label='Class 3')
mean0_fig = plt.scatter(mean0[0], mean0[1], color='black', marker='x', s=100, label='Class Mean')
mean1_fig = plt.scatter(mean1[0], mean1[1], color='black', marker='x', s=100)
mean2_fig = plt.scatter(mean2[0], mean2[1], color='black', marker='x', s=100)
mean3_fig = plt.scatter(mean3[0], mean3[1], color='black', marker='x', s=100)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Synthetic Gaussian Data with Different Means and Standard Deviations')
plt.legend()
plt.savefig('synthetic_gaussian_data.png', dpi=300, bbox_inches='tight')
plt.show()