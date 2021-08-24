import numpy as np
import matplotlib.pyplot as plt

scores = [12, 99, 65, 85, 42]
names = ["Andy", "Martin", "Zahara", "Vuyo", "Ziyaad"]

plt.bar(names, scores, color="blue")

# label the axis
plt.title("Python Marks for 5 students")
plt.xlabel("Names")
plt.ylabel("Marks (in %)")
plt.show()
