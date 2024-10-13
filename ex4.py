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


# arr_grades_a = [10,51,30,40]
# arr_grades_b = [11,-1,54,44]
# student = Student (2,arr_grades_a, arr_grades_b)
# print(student.is_improved())


def id_student(list_u):
  ids = []
  for students in list_u:
    if students.is_improved():
      ids.append(students.id)
  if ids:
    return f"{ids} They are the students who improved!"
  else:
    return "null"


student_0 = Student(5, [0, 51, 30, 40], [11, 0, 3, 44])
student_1 = Student(3, [10, 51, 30, 40], [11, -1, 00, 44])
student_2 = Student(4, [10, 51, 30, 40], [11, -1, 0, 44])

list_s = [student_0, student_1, student_2]

print(id_student(list_s))