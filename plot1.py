# read file
with open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

# create data list
header = data[0]
students = data[1:]

# remove last line (empty line)
students.pop()

# total students
total_students = len(students)

# split header
header = header.split(",")
subjects = header[5:]

# split each student's info
for i in range(len(students)):
    students[i] = students[i].split(",")

# number of students did not take the exam or miss it
not_take_exam = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for student in students:
    for i in range(5,16):
        if student[i] == "-1":
            not_take_exam[i-5] +=1

# plot barchart
import matplotlib.pyplot as plt
import numpy 

figure, axis = plt.subplots()

# list from 0-11
y_pos = numpy.arange(len(subjects))

# plot the barchart using 2 list
plt.bar(y_pos, not_take_exam)

# change horizontal category name
plt.xticks(y_pos, subjects)

# set limit to vertical axis
axis.set_ylim(0,80000)

# label and title
plt.ylabel('# of Students')
plt.title('# of students missed or did not take the exam')

# Draw number of student on top of each bar
rects = axis.patches
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')

# show the plot
plt.show()