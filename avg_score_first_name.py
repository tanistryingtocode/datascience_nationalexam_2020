# read file
with open("clean_data.csv", encoding="utf8") as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]

total_student = len(students)

# split header
header = header.split(",")
subjects = header[5:]

# split each student in list
for i in range(len(students)):
	students[i] = students[i].split(",")

# remove last student (empty student)
students.pop()
  # Tạo dictionary lưu trữ tổng điểm và số điểm theo họ
average_by_first_name = {}
for student in students:
    student_first_name = student[1].split(" ")[-1]  # Lấy tên
    if student_first_name not in average_by_first_name:
      average_by_first_name[student_first_name] = {"sum_score": 0, "count_score": 0}

    # Tính tổng điểm và số lượng điểm
    sum_score = 0
    count_score = 0 
    for i in range(11):
        if student[i+5] != "-1":
            count_score += 1
            sum_score += float(student[i+5].strip())

    # Cập nhật thông tin vào dictionary
    average_by_first_name[student_first_name]["sum_score"] += sum_score
    average_by_first_name[student_first_name]["count_score"] += count_score

  # Tính điểm trung bình cuối cùng
for first_name, info in average_by_first_name.items():
    if info["count_score"] > 0:
      average = info["sum_score"] / info["count_score"]
      average_by_first_name[first_name] = round(average, 2)
import heapq
  # Tìm 10 họ có điểm trung bình cao nhất
top_families = heapq.nlargest(
      10, [(average, first_name) for first_name, average in average_by_first_name.items()]
  )

  # In kết quả
for average, first_name in top_families:
    print(f"Họ: {first_name} - Điểm trung bình: {average}")