# read file
with open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

# create data list
header = data[0]
students = data[1:]

# total students
total_students = len(students)

# split header
header = header.split(",")
subjects = header[5:]

# split each student's info
for i in range(len(students)):
    students[i] = students[i].split(",")

# remove last line (empty line)
students.pop()

# create data

name = []
name_count = []

for student in students:
    student_name = student[1].split(" ")
    student_last_name = student_name[0]
    if student_last_name not in name:
        name.append(student_last_name)
        name_count.append(0)
        name_count[name.index(student_last_name)] +=1
    else:
        name_count[name.index(student_last_name)] +=1

# Create max_list
counted_max_num = []
sort_index = []
for i in range(len(name_count)):
    max_num = 0
    for j in range(len(name_count)):
        if name_count[j] > max_num and name_count[j] not in counted_max_num:
            max_num = name_count[j]
    counted_max_num.append(max_num)

# Find index of top last name
for max_num in counted_max_num:
    for i in range(len(name_count)):
        if name_count[i] == max_num:
            sort_index.append(i)
# DESC sort lastname
name_sorted = []
name_count_sorted = []

for index in sort_index:
    name_sorted.append(name[index])
    name_count_sorted.append(name_count[index])


# plot barchart
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = np.arange(10)

figure, axis = plt.subplots()

plt.bar(x, name_count_sorted[:10])

# change horizontal category name
plt.xticks(y, name_sorted[:10])

# set limit to vertical axis
axis.set_ylim(0,30000)

# label and title
plt.ylabel('# of Students')
plt.xlabel('Last Name')
plt.title('Top 10 Popular Last Name among Students')

# Draw number of student on top of each bar
rects = axis.patches
for rect, label in zip(rects, name_count_sorted):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

# show the plot
plt.show()


