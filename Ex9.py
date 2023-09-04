class Student:
    student_name = "Jo"
    marks = 0


class_ = Student
print(f"Original name: {class_.student_name}, "
      f"Original marks : {class_.marks},")

class_.student_name = "John"
class_.marks = 12
print(f"Modified name: {class_.student_name}, "
      f"Modified marks: {class_.marks}")
