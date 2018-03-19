import numpy as np
import math
a = np.ones((2, 2))
print(a)
print(np.exp(a))
print(math.exp(1.0))
a = np.ones((2, 2))
print(a)
print(np.exp(-a))
print(1.0 / (1.0 + np.exp(-a)))


print(np.random.uniform(-0.1, 0.1,
            (3, 2)))
print(np.zeros((3, 1)))

input_array = np.ones((2, 1)) + +5.0
b = np.ones((3, 1)) + 2.0
weight = np.ones((3, 2)) + 2.0;
print("dot>>")
print(np.dot(weight, input_array) + b)
weighted_input = np.ones((2, 2)) - 0.1
print(1.0 / (1.0 + np.exp(-weighted_input)))
print(weighted_input)

output = np.ones((2, 2)) + 5.0
label = np.ones((2, 2)) + 1.0
print(output * label)
print(":???")
print(0.5 * ((label - output) * (label - output)).sum())
label = np.ones((5, 3)) + 3.0
print(label.shape[0])
print(label.shape[1])
print(np.random.uniform(-1e-4, 1e-4,
            (3, 2,4)))
print(-1e-4)
x = np.array([[1, 0], [2, 5]])
y = np.array([[10, 20], [40, 20]])
x = np.array([[1, 0,3], [2, 5,2]])
print(x.shape[0])
print(x.shape[1])
state =np.random.uniform(1, 10,
            (5, 1))
print(state)
print(state[:,0])