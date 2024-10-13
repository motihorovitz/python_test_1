class Student:
  def __init__(self, id, arr_grades_a, arr_grades_b):
    self.id = id
    self.arr_grades_a = arr_grades_a
    self.arr_grades_b = arr_grades_b

  def is_improved(self):
    for i in range(len(self.arr_grades_a)):
      if self.arr_grades_b[i] != -1 and self.arr_grades_b[i] < self.arr_grades_a[i]:
        return False
    return True

# אם אין אף מקצוע שנלמד בשני הסמסטרים הפעולה תחזיר
# False תתקן את זה
arr_grades_a = [-1,-1,-1,-1]
arr_grades_b = [-1,-1,-1,-1]
student = Student (2,arr_grades_a, arr_grades_b)
print(f"Does student improved - {student.is_improved()}")


def id_student(list_u):
  ids = []
  for students in list_u:
    if students.is_improved():
      ids.append(students.id)
  if ids:
    return f"{ids} They are the students who improved!"
  else:
    return "null"


student_0 = Student(5, [0, 51, 30, 40], [11, 60, 45, 44])
student_1 = Student(3, [10, 51, 30, 40], [11, -1, 80, 44])
student_2 = Student(4, [10, 51, 30, 40], [11, -1, 0, 44])

list_s = [student_0, student_1, student_2]

print(id_student(list_s))