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
average_by_last_name = {}
for student in students:
    student_last_name = student[1].split(" ")[0]  # Lấy họ
    if student_last_name not in average_by_last_name:
      average_by_last_name[student_last_name] = {"sum_score": 0, "count_score": 0}

    # Tính tổng điểm và số lượng điểm
    sum_score = 0
    count_score = 0 
    for i in range(11):
        if student[i+5] != "-1":
            count_score += 1
            sum_score += float(student[i+5].strip())

    # Cập nhật thông tin vào dictionary
    average_by_last_name[student_last_name]["sum_score"] += sum_score
    average_by_last_name[student_last_name]["count_score"] += count_score

  # Tính điểm trung bình cuối cùng
for last_name, info in average_by_last_name.items():
    if info["count_score"] > 0:
      average = info["sum_score"] / info["count_score"]
      average_by_last_name[last_name] = round(average, 2)
import heapq
  # Tìm 10 họ có điểm trung bình cao nhất
top_families = heapq.nlargest(
      10, [(average, last_name) for last_name, average in average_by_last_name.items()]
  )

  # In kết quả
for average, last_name in top_families:
    print(f"Họ: {last_name} - Điểm trung bình: {average}")
