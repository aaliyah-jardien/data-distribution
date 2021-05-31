import numpy as np
import matplotlib.pyplot as plt

marks = np.array([70, 95, 90, 101, 64, 70])
names = np.array(["Memphis","Godwin", "Thando", "Thabo", "Aaliyah", "Uthmaan"])

plt.bar(names, marks, color="orange")
# label the axis
plt.xlabel("Names")
plt.ylabel("Marks (in %)")
plt.title("Marks of Students")
plt.show()
