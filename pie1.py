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

# number of students who took 0,1,2.3,.... subjects
num_exam_taken = [0,0,0,0,0,0,0,0,0,0,0]

no_count_subjects = ["khtn", "khxh"]

for student in students:
    count = 0
    for i in range(11):
        current_subjects = subjects[i]
        if student[i+5] != "-1" and current_subjects not in no_count_subjects:
            count += 1
    num_exam_taken[count] += 1

# create pie chart
import matplotlib.pyplot as plt
import numpy as np

#data
labels = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
sizes = [1, 81, 242, 6610, 1171, 26345, 39993, 0, 1, 0]

# Group low percent subject to one group named "Others"
other_index = [0, 1, 2, 7, 8, 9] 
other_size = sum(np.array(sizes)[other_index])
sizes = np.delete(sizes, other_index)
labels = np.delete(labels, other_index)
labels = np.append(labels, "Others")
sizes = np.append(sizes, other_size)

# Start create pie chart
fig, ax = plt.subplots(figsize=(10,8))
ax.pie(sizes, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12})

# create annotations
bbox_props = dict(boxstyle="square,pad=0.3", fc="white", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(ax.patches):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB=90,rad=10".format(x)

    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.1*y),
                horizontalalignment=horizontalalignment, **kw)

plt.title("Number of subjects taken by students")
plt.axis('equal')
plt.show()