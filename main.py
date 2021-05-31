import numpy
from scipy import stats

marks_of_students = [90, 72, 83, 90, 69, 19, 23, 30, 45, 5]

# calculating the mean
my_mean = numpy.mean(marks_of_students)
print("The mean of the marks is", my_mean)

# calculating median (the middle number)
my_median = numpy.median(marks_of_students)
print("The median of the marks is", my_median)

# calculating mode (value with highest frequencies) the number that apppears the most
my_mode = stats.mode(marks_of_students)
print("The mode of the marks is", my_mode)

# calculating range
my_range = numpy.ptp(marks_of_students)
print("The range of the marks is", my_range)

my_quartile = numpy.percentile(marks_of_students, 25)
print(my_quartile)

my_variance = numpy.var(marks_of_students)
print("The variance of the marks is", my_variance)
